# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import locale
#MINHA TENTATIVA
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

valor_emprestimo = 1000000
data_inicio = datetime(2022, 12, 20)
delta = relativedelta(years = 5)
delta2 = relativedelta(months = 1)
data_fim = data_inicio + delta
qnt_meses = delta.years*12
valor_parcelas = valor_emprestimo/qnt_meses
valor_parcelas_fmt = locale.format_string('%.2f', valor_parcelas, grouping=True)

for i in range(0, qnt_meses):
    data_vencimento = data_inicio + delta2
    print(f'{data_vencimento.strftime('%d/%m/%Y')} R${valor_parcelas_fmt}')
    
    delta2 += relativedelta(months = 1)

#CORREÇÃO DO INSTRUTOR
# valor_total = 1_000_000
# data_emprestimo = datetime(2020, 12, 20)
# delta_anos = relativedelta(years=5)
# data_final = data_emprestimo + delta_anos
# data_parcelas = []
# data_parcela = data_emprestimo

# while data_parcela < data_final:
#     data_parcelas.append(data_parcela)
#     data_parcela += relativedelta(months=+1)

# numero_parcelas = len(data_parcelas)
# valor_parcela = valor_total / numero_parcelas

# for data in data_parcelas:
#     print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}')

# print()
# print(
#     f'Você pegou R$ {valor_total:,.2f} para pagar '
#     f'em {delta_anos.years} anos '
#     f'({numero_parcelas} meses) em parcelas de '
#     f'R$ {valor_parcela:,.2f}.'
# )