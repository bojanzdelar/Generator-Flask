import flask
from flask import Blueprint
from app import mysql

{{entitet}} = Blueprint('{{entitet}}', __name__)

@{{entitet}}.route("/", methods=["GET"])
def get_all_{{entitet}}():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM {{entitet}}")
    return flask.jsonify(cursor.fetchall())

@{{entitet}}.route("/<int:id>", methods=["GET"])
def get_{{entitet}}(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM {{entitet}} WHERE id=%s", (id,))
    {{entitet}} = cursor.fetchone()
    return flask.jsonify({{entitet}}) if {{entitet}} else ("", 404)

@{{entitet}}.route("/", methods=["POST"])
def create_{{entitet}}():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO {{entitet}}({% for atribut in atributi %}{{atribut.naziv}}{% if loop.index != loop.length %}, {% endif %}{% endfor %}) "
            "VALUES({% for atribut in atributi %}%({{atribut.naziv}})s{% if loop.index != loop.length %}, {% endif %}{% endfor %})", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

@{{entitet}}.route("/<int:id>", methods=["PUT"])
def update_{{entitet}}(id):
    {{entitet}} = flask.request.json
    {{entitet}}["id"] = id
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE {{entitet}} SET {% for atribut in atributi %}{{atribut.naziv}}=%({{atribut.naziv}})s{% if loop.index != loop.length %}, {% endif %}{% endfor %} "
            "WHERE id=%(id)s", {{entitet}})
    db.commit()
    cursor.execute("SELECT * FROM {{entitet}} WHERE id=%s", (id,))
    return flask.jsonify(cursor.fetchone()), 200

@{{entitet}}.route("/<int:id>", methods=["DELETE"])
def delete_{{entitet}}(id):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM {{entitet}} WHERE id=%s", (id,))
    db.commit()
    return ""
