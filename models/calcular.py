# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 09:18:58 2022

@author: Jose Gomes
"""

#Gerar valor inteiro randomico. 
from random import randint 

class Calcular:
    
    #Construtor
    #Retorno é None
    # / -> Posicional, só informar o valor;
    def __init__(self: object, dificuldade: int, /) -> None:
        
        self.__dificuldade: int = dificuldade
        #Propriedade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 3) # 1 Somar; 2 Diminuir; 3 Multiplicar
        self.__resultado: int = self._gerar_resultado

    @property
    
    def dificuldade (self: object) -> int:
        return self.__dificuldade
    
    @property
    
    def valor1(self:object) -> int:
        return self.__valor1
    
    @property
    
    def valor2(self:object) -> int:
        return self.__valor2
    
    @property
    
    def operacao(self:object) ->int:
        return self.__operacao
    
    @property
    
    def resultado(self:object) -> int:
        return self.__resultado
    
    #Print no objeto instanciado
    def __str___ (self:object) -> str:
        op : str = ''
        if self.__operacao == 1:
            op = 'Somar'
        elif self.__operacao == 2:
            op = 'Diminuir'
        elif self.__operacao == 3:
            op = 'Multiplicar'
        else:
            op = 'Operação desconhecida'
        
        return f'Valor 1: {self.valor1} \nValor 2: {self.valor2} \nDificuldade: {self.dificuldade} \nOperação: {op}'

    @property
    
    def _gerar_valor(self: object) -> int:
        if self.dificuldade ==1:
            return randint(0, 10)
        elif self.dificuldade ==2:
            return randint(0, 100)
        elif self.dificuldade ==3:
            return randint(0,1000)
        elif self.dificuldade==4:
            return randint(0, 10000)
        else:
            return randint(0, 1000000)
        
    @property
    
    def _gerar_resultado(self: object) -> int:
        if self.operacao== 1: #Somar
            return self.valor1 + self.valor2
        
        elif self.operacao == 2:
            return self.valor1 - self.valor2
        
        else:
            return self.valor1 * self.valor2
        
    @property
    
    def _op_simbolo(self: object) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        else:
            return '*'
        
    def checar_resultado(self: object, resposta: int) -> bool:
        certo: bool = False
        
        if self.resultado == resposta:
            print('Resposta correta')
            certo = True
        else:
            print('Resposta errada')
        
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        return certo
    
    def mostrar_operacao(self: object) -> None:
        print(f'{self.valor1} {self._op_simbolo} {self.valor2}')
        
            
            
