user_vars = {
    'x': 4,
    'y': 'hello'
}

cmd = input()

cmd = cmd.replace(r'\n', '\n')
for var in user_vars.keys():
    cmd = cmd.replace(f'\\{var}\\', f'{user_vars[f"{var}"]}')



print(cmd)