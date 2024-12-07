from conversor import Conversor

conversor = Conversor()

# Cadastro de moedas
conversor.adicionar_moeda("Dólar", 6.09)
conversor.adicionar_moeda("Euro", 6.44)
conversor.adicionar_moeda("Libra", 7.76)

print("Bem-vindo ao conversor de moedas!")
valor_em_reais = float(input("Digite o valor em reais que deseja converter: R$ "))

# Exibir moedas disponíveis com seus índices
print("Moedas disponíveis:")
moedas = conversor.listar_moedas()
for i, moeda in enumerate(moedas, start=1):
    print(f"{i}. {moeda}")

# Selecionar moeda pelo número
try:
    opcao = int(input("Escolha uma moeda pelo número: "))
    if opcao < 1 or opcao > len(moedas):
        raise ValueError("Opção inválida.")
    moeda_destino = moedas[opcao - 1]
except ValueError as e:
    print("Entrada inválida. Tente novamente.")


# Realizar a conversão
resultado = conversor.converter_para_moeda(valor_em_reais, moeda_destino)

# Exibir o resultado
if isinstance(resultado, str):
    print(resultado)
else:
    print(f"R$ {valor_em_reais:.2f} equivalem a {resultado:.2f} {moeda_destino}.")
