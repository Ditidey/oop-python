# clean the data and show output 'a e i o u'

data = 'aNeUreIodhu/n/t>>'

low_data = data.lower()
output_data = ''

for char in low_data:
    if(char == 'a') or (char == 'e') or (char == 'i') or (char == 'o') or (char == 'u'):
        output_data += char + ' '

# print(output_data)

# Encript data

data1 = 'encript'
shift = 1
output_data1 = ''

for char in data1:
    output_data1 += chr(ord(char)+ shift % 26 )

# print(output_data1)

#finding number
from time import sleep

print('Guess a number')
sleep(3)

print('Multiple with 2')
sleep(3)

print('Add with 8')
sleep(3)

print('Divide with 2')
sleep(3)

print('Minus with the number')
sleep(3)

print('Your number is 4')
 

