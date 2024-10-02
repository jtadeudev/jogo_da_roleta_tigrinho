import random

simbolos = ['🍒', '🍋', '🍊', '🍉', '⭐', '💎'] #símbolos para aparecer na máquina
bobinas = 3  #número de bobinas

def girar_roleta(): #função que gira a roleta com as bobinas
    return [random.choice(simbolos) for _ in range(bobinas)] #sempre retorna 3 elementos. o choice() faz parte da biblioteca random e vai dar um valor aleatório 3 vezes. loop com placeholder

def checar_vitoria(resultado_roleta): # função que checa se os 3 símbolos são iguais
    if all(simbolo == resultado_roleta[0] for simbolo in resultado_roleta): #método igual ao every() do javascript. vai iterar sobre cada elemento de resultado_roleta e comparar
        return True #retorna um booleano
    return False #retorna um booleano

def printar_resultado_roleta(resultado_roleta): #função que mostra o resultado do giro da roleta na tela
    print(" | ".join(resultado_roleta))
   
def jogar_jogo_do_tigrinho(): #função para começar o jogo
    print("Bem-vindo à máquina caça-níquel do Jogo do Tigrinho. Aqui o seu dinheiro pode voltar até X vezes ;)") # nenhuma pessoa foi financeiramente lesada nesse projeto
    while True: #loop infinito
        input("Aperte enter para começar")
        resultado_roleta = girar_roleta() #a variável local resultado_roleta recebe a invocação da função que gira a roleta e pode ser passada como parâmetro pra todas as funções
        printar_resultado_roleta(resultado_roleta) #chamando a função que mostra o resultado na tela
       
        if checar_vitoria(resultado_roleta): #o resultado da roleta é passado como parâmetro pra função checar_vitoria para ver se você ganhou o jogo
            print("Parabéns! Você venceu!") #se a checagem der true, você verá uma mensagem te parabenizando por ter vencido o jogo
        else:
            print("Tente novamente!") #se a checagem der false, você verá que não venceu o jogo e receberá a chance de tentar de novo

        jogar_novamente = input('Você quer jogar de novo? Digite "sim" para continuar investindo | ').strip().lower()
        if jogar_novamente != 'sim':
            print("Obrigado por ter jogado! Até mais!")
            break #sair do loop while

jogar_jogo_do_tigrinho() 