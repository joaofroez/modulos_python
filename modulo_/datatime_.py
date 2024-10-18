# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime
from pytz import timezone

data_str = '2024-04-20 07:49:23'
data_str_format = '%Y-%m-%d %H:%M:%S'

data = datetime(2024,10,8,16,00,00)
print(data)
data_str_new = datetime.strptime(data_str, data_str_format)
print(data_str)

data_tokyo = datetime.now(timezone('Asia/Tokyo'))
print(data_tokyo)

print(data.timestamp())#maneira de salvar na base de dados
print(datetime.fromtimestamp(1728414000.0))