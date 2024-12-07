# conversor.py
from moeda import Moeda

class Conversor:
    def __init__(self, moedas):
        self.moedas = moedas
    
    def converter(self, valor, moeda_origem, moeda_destino):
        # Encontrar as moedas com base no nome
        moeda_origem_obj = next((moeda for moeda in self.moedas if moeda.get_nome() == moeda_origem), None)
        moeda_destino_obj = next((moeda for moeda in self.moedas if moeda.get_nome() == moeda_destino), None)
        
        if moeda_origem_obj is None or moeda_destino_obj is None:
            return "Moeda não encontrada."
        
        # Converter o valor para a moeda destino
        valor_convertido = valor * (moeda_destino_obj.get_valor() / moeda_origem_obj.get_valor())
        return valor_convertido
