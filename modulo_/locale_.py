import calendar
import locale

locale.setlocale(locale.LC_ALL, 'ru_MD')

print(calendar.calendar(2022))

#Comados de terminal para ver os locale locale -a|grep 'pt' 