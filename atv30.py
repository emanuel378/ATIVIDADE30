# crie uma duncao que calcule a nota a media de 3 notas em seguida verifique se ele esta aprovado ou reprovado para notas acima de 7


def nota(nota1,nota2,nota3):
    nota1 = int(input("Digite sua primeira nota:"))
    nota2 = int(input("Digite sua segunda nota:"))
    nota3 = int(input("Digite sua terceira nota:"))
    media = (nota1 + nota2 + nota3)/3
    print( "sua media e",media)
    if media >=7:
        return"aprovado"
    else:
        return"Reprovado"
        

resultado =nota()
print(resultado)

    
