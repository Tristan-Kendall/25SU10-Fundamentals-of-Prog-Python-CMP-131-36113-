# Prompting user for input
n = int(input('Insert an integer value:'))

# Looping
counter = 2
while counter <= n:
    if counter % 7 == 0:
        print(f'{counter} is a multiple of 7')
    counter += 1