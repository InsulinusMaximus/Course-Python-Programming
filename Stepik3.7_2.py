#2

# Принимаем ключи
key_encrypt = input()
key_decrypt = input()

# Принимаем значения, которые нужно зашифровать и расшифровать
go_encrypt = input()
go_decrypt = input()

#Создаем словарь с ключем key_encrypt, а значением key_decrypt
key_value = {}
for mean in range(len(key_encrypt)):
    key_value.update({key_encrypt[mean] : key_decrypt[mean]})

# Зашифровываю go_encrypt
encrypt = []
i = 0
while i != len(go_encrypt):
    for mean in key_value:
        if go_encrypt[i] == mean:
            encrypt.append(key_value[mean])
    i += 1
    
print(*encrypt, sep = '')

# Расшифровываю go_decrypt
decrypt = []
j = 0
while j != len(go_decrypt):
    for key, mean in key_value.items():
        if go_decrypt[j] == mean:
            decrypt.append(key)
    j += 1
        

print(*decrypt, sep = '')