
unit = input('Do you want to convert temperature from Kelwin(k) or Celcius (c)?')

if unit not in ['k', 'c']:
    raise Exception('Please enter units properly (k/c)')
temperature = int(input('Enter temperature in chosen unit: '))
kalwin_constant = 273.15;

if unit == 'k':
    result = temperature - kalwin_constant
elif unit == 'c':
    result = temperature + kalwin_constant

print('Result is: ' + str(result))
# add farenheit
