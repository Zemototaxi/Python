from datetime import date
year = int(input('Digite um ano: '))
if year == 0 :
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'O ano {year} é BISSEXTO! 📅')
else:
    print(f'O ano {year} nao é BISSEXTO!')