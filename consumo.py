from prettytable import PrettyTable
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Criando uma lista vazia para os equipamentos
equipamentos = []

print('''Programa para calcular consumo
de equipamentos elétricos em reais''')
concessionaria = input('Nome da concessionaria: ')
valor_kwh_mes = float(input('Valor do KWh/m em R$: ').replace(',', '.'))

while True:
    # Pedindo ao usuário para inserir o nome do equipamento
    equipamento = input('Digite o equipamento (ou "sair" para terminar): ')
    
    
    # Se o usuário digitar 'sair', o loop será interrompido
    if equipamento == 'sair':
        limpar_tela()
        print('Lista de equipamentos:')
        break
    

    # Pedindo ao usuário para inserir os detalhes do equipamento
    quantidade = int(input(f'Quantidade de {equipamento}: '))
    potencia = int(input('Potência do equipamento em W: '))
    potencia_total = quantidade * potencia
    hora_dia = float(input('Quantidade de horas por dia: ').replace(',', '.'))
    dias_mes = int(input('Dias de uso por mês: '))

    # Calculando o consumo do equipamento
    calculo = (potencia_total * hora_dia * dias_mes) / 1000
    consumo = calculo * valor_kwh_mes

    print(f'O consumo mensal do equipamento {equipamento} é R$ {consumo:.2f}')

    # Adicionando o equipamento e seu consumo à lista
    equipamentos.append([equipamento, quantidade, potencia_total, hora_dia, dias_mes, consumo])

# Calculando o valor total
valor_total = sum(item[5] for item in equipamentos)

# Criando uma tabela
tabela = PrettyTable()

# Definindo os cabeçalhos da tabela
tabela.field_names = ["Equipamento", "Quantidade", "Potência Total (W)", "Horas por Dia", "Dias por Mês", "Consumo Mensal (R$)"]

# Adicionando dados à tabela com formatação de duas casas decimais para o consumo mensal
for item in equipamentos:
    equipamento, quantidade, potencia_total, hora_dia, dias_mes, consumo = item
    tabela.add_row([equipamento, quantidade, potencia_total, hora_dia, dias_mes, f'{consumo:.2f}'])

print(f'O valor do KW/h na {concessionaria} é R$ {valor_kwh_mes}')
# Exibindo a tabela
print(tabela)
print(f"O total do consumo dos equipamentos em reais é R$ {valor_total:.2f}")
print('* Não está incluso a taxa de iluminação pública')