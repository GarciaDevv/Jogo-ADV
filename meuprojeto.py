import random # importa o módulo random para gerar números aleatorios

numero = random.randint(1,100) # gera um numero aleatório entre 1 e 100
tentativas = 0 # inicializa a variável " tentativas"

print("Bem-vindo ao jogo da adivinhaçao!")
print("Eu escolhi um número entre 1 e 100. Vc tem 10 tentativas.")

while tentativas < 10: # inicia um looo que continua enquanto o número de tentativas for menor que 10
    palpite =int(input("Digite seu palpite")) # solicita ao jogador para inserir seu palpite
    tentativas += 1# incrementa o número de tentativas em 1

    if palpite == numero: 
       print(f"Parabens! Vc acertou em {tentativas} tentativas")
       break


    elif palpite < numero:print("o numero é maior. tente novamente")
     
    else: print("o numero é menor. tente novamente")
else: print(f" voce perdeu. o numero era { numero}.")

