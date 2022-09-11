import os

if __name__ == '__main__': 
    if os.name == 'nt': os.system('shutdown /p')
    elif os.name == 'posix': os.system('sudo shutdown -h now')