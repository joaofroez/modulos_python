import locale

# Define a localidade para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Número que você deseja formatar
numero = 1666667

# Formata o número
numero_formatado = locale.format_string('%.2f', numero / 100, grouping=True)

print(numero_formatado)
