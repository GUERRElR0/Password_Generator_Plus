import string
from random import choice

def letters(d=8):

    digitos = int(d)
    valores = string.ascii_letters
    senha = ""

    for i in range(digitos):
        senha += choice(valores)
    return senha

def LowerCase(d=8):

    digitos = int(d)
    valores = string.ascii_lowercase
    senha = ""

    for i in range(digitos):
        senha += choice(valores)
    return senha

def UpperCase(d=8):

    digitos = int(d)
    valores = string.ascii_uppercase
    senha = ""

    for i in range(digitos):
        senha += choice(valores)
    return senha

def numbers(d=8):

    digitos = int(d)
    valores = string.digits 
    senha = ""

    for i in range(digitos):
        senha += choice(valores)
    return senha

def symbols(d=8):

    digitos = int(d)
    valores = string.punctuation
    senha = ""

    for i in range(digitos):
        senha += choice(valores)
    return senha

def todos(d=8):

    digitos = int(d)
    valores = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    senha = ""
    for i in range(digitos):
        senha += choice(valores)
    return senha

def NumSymLow(d=8):

    digitos = int(d)
    valores = string.ascii_lowercase + string.punctuation + string.digits
    senha = ""

    for i in range(digitos):
        senha += choice(valores)
    return senha

def NumSymUpp(d=8):

    digitos = int(d)
    valores = string.ascii_uppercase + string.punctuation + string.digits
    senha = ""

    for i in range(digitos):
        senha += choice(valores)
    return senha

def NumLow(d=8):

    digitos = int(d)
    valores = string.ascii_lowercase + string.digits
    senha = ""

    for i in range(digitos):
        senha += choice(valores)
    return senha

def NumUpp(d=8):

    digitos = int(d)
    valores = string.ascii_uppercase + string.digits
    senha = ""

    for i in range(digitos):
        senha += choice(valores)
    return senha

def NumLet(d=8):

    digitos = int(d)
    valores = string.ascii_letters + string.digits
    senha = ""

    for i in range(digitos):
        senha += choice(valores)
    return senha

def NumSym(d=8):

    digitos = int(d)
    valores = string.punctuation + string.digits
    senha = ""

    for i in range(digitos):
        senha += choice(valores)
    return senha

def LowSym(d=8):

    digitos = int(d)
    valores = string.punctuation + string.ascii_lowercase
    senha = ""

    for i in range(digitos):
        senha += choice(valores)
    return senha

def UppSym(d=8):

    digitos = int(d)
    valores = string.punctuation + string.ascii_uppercase
    senha = ""

    for i in range(digitos):
        senha += choice(valores)
    return senha

def LetSym(d=8):

    digitos = int(d)
    valores = string.punctuation + string.ascii_letters
    senha = ""

    for i in range(digitos):
        senha += choice(valores)
    return senha