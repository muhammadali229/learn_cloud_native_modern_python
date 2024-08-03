# input
# user_input:str = input("Enter your name: ")
# print(f'Welcome to Certified AI Generative Course {user_input}')

# console inputs
import sys
from typing import List, Dict, Union
print('line_1')
print('line_2')
print(type(sys.argv))
print(sys.argv)
print('List: ', [i for i in dir(list) if 'iter' in i])
print('Tuple: ', [i for i in dir(tuple) if 'iter' in i])
print('String: ', [i for i in dir(str) if 'iter' in i])
print('Set: ', [i for i in dir(set) if 'iter' in i])
print('Int: ', [i for i in dir(int) if 'iter' in i])

# print(sys.argv)
if len(sys.argv) > 1 and sys.argv[1] == '-s':
    data: List[Dict[str, Union[str, int]]] = [
        # {'name': 'ali', 'age': 28, 'education': 'computer engineering', 'university': 'bahria'},
        # {'name': 'saif', 'age': 26, 'education': 'computer science', 'university': 'smit'},
        # {'name': 'umair', 'age': 28, 'education': 'computer science', 'university': 'fast'}
    ]

    is_system_on: bool = True
    while is_system_on:
        name: str = input('Enter your name: ')
        age: int = int(input('Enter your age: '))
        education: str = input('Enter your education: ')
        university: str = input('Enter your university: ')
        data.append({
            'name': name.title(),
            'age': age,
            'education': education.title(),
            'university': university.title() 
        })
        if input('Do you want to add more students? (Y for Yes or Anything to exit) ').lower() != 'y':
            is_system_on = False
    print(data)

print('Break at 6')
for i in range(1, 11):
    if i == 6:
        break
    print(f'2 X {i} = {2 * i}')
    
print('Continue at 6')
for i in range(1, 11):
    if i == 6:
        continue
    print(f'2 X {i} = {2 * i}')
    
for i in range(1, 1000):
    # write logic
    pass

# prompt:str = """
#     Enter something...
# """
# user_input:str = input(prompt)
# print(user_input)

lst: List[str] = ['ali', 'haris', 'yasir']
while lst:
    print(lst)
    lst.pop()