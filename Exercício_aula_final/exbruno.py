resposta = input("Olá, tudo bem?")

if resposta.upper() == "SIM":
    print("Que bom")
elif resposta.upper() == "NAO":
    resposta = input("Por que?")
else:
    print("Nao posso te ajdudar")