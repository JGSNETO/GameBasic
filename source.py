# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 10:09:14 2022

@author: Jose Gomes
"""

from models.calcular import Calcular

def main () -> None:
    
    pontos: int = 0
    jogar(pontos)
 
    
def jogar (pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade desejado[1,2,3 ou 4]: '))
    
    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    
    calc.mostrar_operacao()

    resultado: int = int(input())
    
    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} pontos')
        
    continuar: int = int(input('Deseja continuar no jogo ? [1-sim; 0-Não]'))
    if continuar:
        jogar(pontos)
    else:
        print('Você finalizou com {pontos} pontos')
        
        
if __name__ == '__main__' :
    main()