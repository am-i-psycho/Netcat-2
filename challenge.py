import re

FLAG = open('flag.txt').read()

inp = input('Enter your secret key :  ')

if re.search(r'\d', inp) or eval(inp) != 1337:
    print('Nope')
else:
    print(FLAG)