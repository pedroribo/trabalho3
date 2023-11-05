import hashlib

# Definindo a senha para a comparacao
definedPassword_file = open("definedPassword.txt", "w")
password = "strongPassword"
hashing_definedPassword = hashlib.sha256()
hashing_definedPassword.update(password.encode('utf-8'))
definedPassword_hash = hashing_definedPassword.hexdigest()
definedPassword_file.write(definedPassword_hash)
definedPassword_file.close()

definedPassword_file = open("definedPassword.txt", "r")
definedPassword = definedPassword_file.read()
definedPassword_file.close()
#print(definedPassword)

# Definindo a senha informada para ser comparada com a senha definida
informedPassword_file = open("informedPassword.txt", "w")
informedPassword_file.write("blablabla")
informedPassword_file.close()

informedPassword_file = open("informedPassword.txt", "r")
informedPassword = informedPassword_file.read()
informedPassword_file.close()
#print(informedPassword)

# Gerando hash da senha informada
hashing_informedPassword = hashlib.sha256()
hashing_informedPassword.update(informedPassword.encode('utf-8'))
informedPassword_hash = hashing_informedPassword.hexdigest()
#print(informedPassword_hash)

# Apresentando a senha informada presente no arquivo de texto
print(f'A senha informada foi: {informedPassword}.')

# Comparando senhas
if informedPassword_hash == definedPassword:
    print("Senha correta.")
else:
    print("Senha incorreta.")
