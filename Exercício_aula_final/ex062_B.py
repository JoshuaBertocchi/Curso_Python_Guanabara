primeiro_termo = int(input("Me diga o Primeiro Termo:"))
razao = int(input("Me informe a Razão:"))





while True:

    termo_final = int(input("Quantos termos deseja ver:"))

    for i in range(termo_final):
        pa = primeiro_termo + ((i + 1) - 1) * razao
        print(pa, end=" => ")

    primeiro_termo = pa
    print("Primeiro termo", primeiro_termo)

    deseja_continuar = input(
        """
        1 - VEJA MAIS TERMOS CONTINUANDO DE ONDE PAROU
        0 - SAIR
        """
    )
    if deseja_continuar == "1":
        
        continue
    else:
        print("Obrigado :), volte nunca")
        break
