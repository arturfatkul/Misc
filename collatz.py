def collatz(number):
    
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1

number_input = input("Enter the number: ")

while number_input != 1:
    try:
        number_input = collatz(int(number_input))
    except ValueError:
        print('not an int')
        break
