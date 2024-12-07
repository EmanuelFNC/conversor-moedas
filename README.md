# Conversor de Moedas

Este projeto do curso Talento Tech-PR consiste em um sistema simples para converter valores em Reais (BRL) para outras moedas estrangeiras. O sistema permite cadastrar novas moedas e seus respectivos valores em relação ao Real, além de realizar a conversão de forma interativa.

## Objetivos do Projeto

O objetivo deste projeto é praticar os conceitos de:

- **Programação Orientada a Objetos (POO)**: Uso de classes e encapsulamento.
- **Uso do GitHub**: Organização e versionamento do código.

## Funcionalidades Implementadas

1. **Cadastro de Moedas**:
   - Permite cadastrar moedas, definindo seu nome e valor em relação ao Real.
2. **Listagem de Moedas**:
   - Exibe uma lista das moedas disponíveis para conversão.
3. **Conversão**:
   - Converte um valor em Reais para a moeda estrangeira selecionada pelo usuário.
4. **Seleção por Índice**:
   - O usuário escolhe a moeda desejada pelo número correspondente.

## Estrutura de Arquivos

- **moeda.py**: Contém a classe `Moeda`, responsável por representar cada moeda, com seus atributos privados e métodos de acesso (getters).
- **conversor.py**: Contém a classe `Conversor`, que gerencia as moedas cadastradas e realiza as operações de conversão.
- **principal.py**: Interface interativa com o usuário, onde são realizadas as interações e exibidos os resultados.

## Exemplo de Uso

### Entrada:
```plaintext
Digite o valor em reais que deseja converter: R$ 10
Moedas disponíveis:
1. Dólar
2. Euro
3. Libra
Escolha uma moeda pelo número: 1
```

### Saída:
```plaintext
R$ 10.00 equivalem a 1.89 Dólar.
```

Caso o usuário insira uma entrada inválida:
```plaintext
Entrada inválida. Tente novamente.
```

## Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/EmanuelFNC/conversor-moedas
   cd conversor-moedas
   ```

2. Certifique-se de ter o Python instalado. Execute o arquivo principal:
   ```bash
   python3 main.py
   ```

3. Siga as instruções no terminal para converter valores.

## Possíveis Melhorias

- Adicionar suporte para converter entre quaisquer moedas, não apenas de Real para outras.
- Implementar um sistema de cadastro de moedas pelo usuário diretamente via interface.
- Utilizar uma API para obter taxas de câmbio em tempo real.

## Benefícios do Uso do GitHub

- **Branches organizadas**: Cada funcionalidade foi desenvolvida separadamente, utilizando branches.
- **Commits frequentes**: Foram realizados commits sempre que uma funcionalidade era concluída, garantindo um histórico detalhado.
- **Merge seguro**: A integração entre as funcionalidades foi feita com cuidado para evitar conflitos.
