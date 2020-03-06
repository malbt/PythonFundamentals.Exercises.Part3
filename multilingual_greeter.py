def language_input():
    return input("Prefered language: French, Spanish or English\n"
                 "Idioma preferido: francés, ESPANOL o inglés\n"
                 "Langue préférée: FRANÇAIS, espagnol ou anglais:\n")


language = language_input()
if language.upper() == "ENGLISH":
    def greet(name: str)->None:
        print("hello " + name)

    def name_input() -> str:
        return input("Please enter your name:\n")
    name = name_input()
    greet(name)
elif language.upper() == "FRANCAIS":
    def greet(name:str)->None:
        print("Bonjour " + name)


    def name_input() ->str:
        return input("S'il vous plaît entrez votre nom:\n")
    name = name_input()
    greet(name)
elif language.upper() == "ESPANOL":
    def greet(name: str)->None:
        print("Ola" + name)

    def name_input() -> str:
        return input("Por favor, escriba su nombre:\n")
    name = name_input()
    greet(name)
else :
    print("?")
