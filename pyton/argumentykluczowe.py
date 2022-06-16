'''Argumenty kluczowe i pozycyjne
kluczowy - w postaci : klucz - wartość ( domyślny)
pozycyjne - takich, których lidzy się kolejność przy wywołaniu'''


def greet(name, message, separator=' '):
    print(message, name, sep=separator)


greet("Arek", 'Witajcie', "\n")
