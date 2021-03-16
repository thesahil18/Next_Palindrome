def palindrome(num):
    while not is_palindrome(num):
        num += 1
    return num

def is_palindrome(num):
    return str(num) == str(num)[::-1]

if __name__ == '__main__':
    no_of_input = int(input("Enter Test cases : "))
    numbers = []
    for i in range(no_of_input):
        numbers.append(int(input(f'Enter number {i+1} : ')))
    
    for i in range(no_of_input):
        print(f'Next Palindrome of {numbers[i]} : {palindrome(numbers[i])}')
