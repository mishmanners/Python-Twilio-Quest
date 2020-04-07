import sys

first_num = int(sys.argv[1])
second_num = int(sys.argv[2])
add_numbers = first_num + second_num

if add_numbers <= 0:
    print('You have chosen the path of destitution')
elif add_numbers >= 1 and add_numbers <= 100:
    print('You have chosen the path of plenty')
elif add_numbers >= 101:
    print('You have chosen the path of excess')
