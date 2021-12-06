#data = str(input("Ingrese nujero: "))
#print(len(data)," digitos")
# Best practice
from server import start


condicion = False
x = 1 if condicion else 0
print(x)

num1,num2 = 1_000_000_000, 200_000_000
total = num1 + num2
print(f'{total:,}')

# Read a file
with open('text.txt','r') as f:
    file_contents = f.read()

words = file_contents.split('\n')
words_lines = len(words)

names = ['Marcos','Corey','Jenh']
heroes = ['Spiderman','Superman','Flash']
power = [70,98,85]
for index, name in enumerate(names, start=1):
    print(index,name)

for name, hero, pow in zip(names,heroes,power):
    print(f'{name} es {hero} con poder de {pow}')

# Unpacking

a,b,*_,finalValue = (2,5,3,6,4,8)
print(a,b,finalValue)



