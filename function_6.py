#!/usr/bin/python3

def external(language):
    dic = { "pt": "Olá", "pi": "Ahoy", "en": "Hello" }

    def internal(name):
        print("{0} {1}".format(dic[language, name]))
    return internal

func = external("pi")    
func("Paloma")
func("Kenji")
func("Julia")
