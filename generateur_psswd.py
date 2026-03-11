import string
import random

mixed= string.ascii_letters + string.digits
psswd="".join(random.choice(caractere) for i in range(9))
print(f'mot de passe: {psswd}')