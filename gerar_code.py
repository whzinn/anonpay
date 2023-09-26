from random import randint

abc = ""
for x in range(97,123):
    abc+=chr(x)
    
ABC = ""
for x in range(65,91):
    ABC+=chr(x)
    
num = "0123456789"

nu = num + ABC + abc + num

senha = ""
for x in range(5):
    n = randint(0,72)
    senha+=nu[n]
print(senha)