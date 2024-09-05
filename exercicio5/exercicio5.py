def inverter_string(s):
    invertida = ""
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

def principal():
    string_original = input("Digite a string a ser invertida: ")
    string_invertida = inverter_string(string_original)
    print(f"String invertida: {string_invertida}")

if __name__ == "__main__":
    principal()