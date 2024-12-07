# moeda.py
class Moeda:
    def __init__(self, nome, valor):
        self.__nome = nome  # Atributo realmente privado
        self.__valor = valor  # Atributo realmente privado
    
    # Métodos Getter
    def get_nome(self):
        return self.__nome
    
    def get_valor(self):
        return self.__valor
    
    # Métodos Setter
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_valor(self, valor):
        self.__valor = valor
    
    def __str__(self):
        return self.get_nome()
