import os
import string
import random
import time
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

    for char in passw:
        print(char, end="", flush=True)
        time.sleep(0.1)
    print("\n")
    os.system("clear")
    
    if input(str("\n\033[36m[!] Want to write to a file? (Y or N)? ")) == 'Y' or 'y':
        filename = input(str("\033[36m[*] Enter file name: "))
        arq = open(filename, 'w')
        arq.write(passw)
        arq.close()
        print("\033[33m[*] Ready! Your password has been recorded in ", filename)
        print("\033[33m[^_^] Your password: ", passw)
        
    else:
        os.system("clear")
        print("\033[33m[^_^] Your password: ", passw)
    pass


random_password_generator()

        
         

