f = 0
print('fahrenheit celsius')
while f <= 250:
    celsius = (f - 32) / 1.8
    print('{:5d}{:7.2f}'.format(f,celsius))
    f = f + 25
