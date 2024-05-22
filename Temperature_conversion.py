def cel(temp):
    print(temp,'°C in Fahrenheit is',(temp*9/5)+32,'°F')
    print(temp,'°C in Kelvin is',temp+273.15,'°K\n')
def fah(temp):
    print(temp,'°F in Celsius is',5/9*(temp-32),'°C')
    print(temp,'°F in Kelvin is',(temp-32)*5/9+273.15,'°K\n')
def kel(temp):
    print(temp,'°K in Celsius is',temp-273.15,'°C')
    print(temp,'°K in Fahrenheit is',(temp-273.15)*9/5+32,'°F\n')


unit = input("Choose your unit (C for Celcius, F for fahrenheit, K for Kelvin) \n").lower()
if unit == 'c':
        temp = int(input('\ntemperature: '))
        cel(temp)
elif unit == 'f':
        temp = int(input('\ntemperature: '))
        fah(temp)
elif unit == 'k':
        temp = int(input('\ntemperature: '))
        kel(temp)
else:
        print('your input is invalid')
        
