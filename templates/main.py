import flask
from flask import Flask
from flaskext.mysql import MySQL, pymysql

{% for entitet in entiteti %}from {{entitet}} import {{entitet}}
{% endfor %}

app = Flask(__name__, static_url_path="")

app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "root"
app.config["MYSQL_DATABASE_DB"] = "{{projekat}}"

mysql = MySQL(app, cursorclass=pymysql.cursors.DictCursor)

{% for entitet in entiteti %}app.register_blueprint({{entitet}}, url_prefix="/api/{{entitet}}")
{% endfor %}

@app.route("/")
def index():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    app.run()
