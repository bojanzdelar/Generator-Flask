from jinja2 import Template

def data():
    projekat = input("Unesite ime projekta: ")
    print("--------------------------")
    broj_entiteta = int(input("Unesite broj entiteta: "))
    entiteti = []
    atributi = []
    for i in range(broj_entiteta):
        print("--------------------------")
        entitet = input(f"Unesite entitet br. {i+1}: ")
        entiteti.append(entitet)

        broj_atributa = int(input("Unesite broj atributa: "))
        atributi_entiteta = []
        for i in range(broj_atributa):
            atribut = {}
            atribut["naziv"] = input(f"Unesite ime atributa broj {i + 1}: ")
            atributi_entiteta.append(atribut)

        atributi.append(atributi_entiteta)

    return projekat, entiteti, atributi


def main(projekat, entiteti):
    with open(f"templates/main.py.j2", 'r') as input, \
            open(f"../output/main.py", "w") as output:
        template_string = input.read()
        template = Template(template_string)
        result = template.render(projekat=projekat, entiteti=entiteti)
        output.writelines(result)

def entitet(entitet, atributi):
    with open(f"templates/entitet.py.j2", 'r') as input, \
            open(f"../output/{entitet}.py", "w") as output:
        template_string = input.read()
        template = Template(template_string)
        result = template.render(entitet=entitet, atributi=atributi)
        output.writelines(result)

if __name__ == "__main__":
    projekat, entiteti, atributi = data()
    
    main(projekat, entiteti)

    for i in range(len(entiteti)):
        entitet(entiteti[i], atributi[i])