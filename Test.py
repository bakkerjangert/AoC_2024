print('00123'.lstrip('0'))
print('00000'.lstrip('0'))

string = '0000'

string = string.lstrip('0') if string.count('0') != len(string) else '0'
print(string)