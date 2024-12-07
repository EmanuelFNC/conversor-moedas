from moeda import Moeda

class Conversor:
    def __init__(self):
        self.moedas = []  # Lista de moedas disponíveis

    def adicionar_moeda(self, nome, valor):
        self.moedas.append(Moeda(nome, valor))

    def listar_moedas(self):
        return [moeda.get_nome() for moeda in self.moedas]

    def converter_para_moeda(self, valor_em_reais, moeda_destino):
        moeda_destino_obj = next((moeda for moeda in self.moedas if moeda.get_nome() == moeda_destino), None)
        
        if moeda_destino_obj is None:
            return f"Moeda {moeda_destino} não encontrada."
        
        # Converte o valor de Reais para a moeda destino
        valor_convertido = valor_em_reais / moeda_destino_obj.get_valor()
        return valor_convertido
