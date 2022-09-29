
def main(numbers: list, loopRange: int, responses: list) -> None:
    for i in range(1, loopRange+1):
        if all(i % flag == 0 for flag in numbers):
            print(responses[0])
        elif any(i % flag == 0 for flag in numbers):
            for j in numbers:
                if i % j == 0:
                    if j == numbers[0]:
                        print(responses[1])
                        break
                    elif j == numbers[1]:
                        print(responses[2])
                        break
                    elif j == numbers[2]:
                        print(responses[3])
                        break
        else:
            print(i)    

if __name__ == '__main__':
    main([3, 5], 100, ['FizzBuzz', 'Fizz', 'Buzz', 'Fuzz', 'Bizz', 'Biff'])

'''
def main() -> None:
    for i in range(1, 100+1):
        if i % 5 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

if __name__ == '__main__':
    main()
'''

'''
def main() -> None:
    for i in range(1, 100+1):
        if i % 3 == 0:
            if i % 5 == 0:
                print('FizzBuzz')
            else:
                print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

if __name__ == '__main__':
    main()
'''