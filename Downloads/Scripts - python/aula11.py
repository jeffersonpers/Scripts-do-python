a = input('Digite algo: ')
print('O tipo primitivo desse valor é' , type(a))
print('Só tem espaços? ', a.isspace())              # Para verificar se tem espaços se tiver ele vai retornar TRUE se não vai retornar False
print('É um número?', a.isnumeric())                # Verifica se é numero
print('É uma letra do alfabeto ?', a.isalpha())     # Verifica se e letra do alfabeto
print('É alfanúmerico ?', a.isalnum())              # Verifica se é alphanúmerico
print('É Maiúscula as Letras ?', a.isupper())       # Verifica se é Maiúsculas
print('É Minúscula as Letras ?', a.islower())       # Verifica se é Minúsculas
print('Éstá Capitalizada as Letras ?', a.istitle()) # Verifica se é Capitalizada