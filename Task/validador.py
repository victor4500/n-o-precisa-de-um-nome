#validador de senhas

print('uma senha valida seria uma senha que tem no minimo 8 caracteres e uma letra maiuscula e um caractere espcial.')

senha = (input('Vamos ver se a sua senha é valida: '))

def validar_Ncaract(senha):
    return len(senha) >= 8
    
def validar_nume(senha):
    for letra in senha:
        if letra.isdigit():
            return True

    return False

especiais = "!@#$%&."

def valirdar_caract(senha):
    for especial in senha:
        if especial in especiais:
            return True
    
    return False
            
resltado = validar_Ncaract(senha) and validar_nume(senha) and valirdar_caract(senha)

if resltado:
    print('a senha valida')
else:
    print('senha não valida')