string = input("Digite uma string: ")

reversed_string = ""
for i in range(len(string)-1, -1, -1):
    reversed_string += string[i]

print("A string invertida é:", reversed_string)
