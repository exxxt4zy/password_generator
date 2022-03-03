import os
import string
import random
import time
os.system("clear")
banner = """
██████╗  █████╗ ███████╗███████╗ ██████╗ ███████╗███╗   ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██╔════╝████╗  ██║
██████╔╝███████║███████╗███████╗██║  ███╗█████╗  ██╔██╗ ██║
██╔═══╝ ██╔══██║╚════██║╚════██║██║   ██║██╔══╝  ██║╚██╗██║
██║     ██║  ██║███████║███████║╚██████╔╝███████╗██║ ╚████║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
"""
print(banner, end="\n")
def random_password():
    scale = input('\033[36m[!] Enter password size: ')
    final = int(scale.split(' ')[0])

    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password_gen = ''.join(random.choice(chars) for x in range(final))
    return password_gen 

def random_password_generator():
    passw = random_password()
    if len(passw) > 15:
        ts = 0.03
    else:
        ts = 0.1

    for char in passw:
        print(char, end="", flush=True)
        time.sleep(ts)
    print("\n")
    os.system("clear")

    choise = input(str("\n\033[36m[!] Want to write to a file? (Y or N)? "))
    
    if choise.upper() == "Y":
        filename = input(str("\033[36m[*] Enter file name: "))
        arq = open(filename, 'w')
        arq.write(passw)
        arq.close()
        print("\033[33m[*] Ready! Your password has been recorded in ", filename)
        print("\033[33m[^_^] Your password: ", passw)        
    elif choise.upper() == "N":
        os.system("clear")
        print("\033[33m[^_^] Your password: ", passw)


random_password_generator()

        
         

