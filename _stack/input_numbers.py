if __name__ == '__main__':
    first_input = input('Input some letters: ')
    first_list = first_input.split(' ')
    
    second_input = input('Input some numbers: ')
    second_list = second_input.split(' ')
    for num in second_list:
        second_list[second_list.index(num)] = int(num)
        
    third_list = []
    for num in second_list:
        third_list.append(first_list[num])
        
    print(f'The letters are: {third_list}')
