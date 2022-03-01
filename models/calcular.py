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
    # / -> Posicional, só infomar o valor;
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
        #Código vai ignorar
        pass
    
    @property
    
    def _gerar_resultado(self: object) -> int:
        pass
    
    def checar_resultado(self: object, resposta: int) -> bool:
        pass
    
    def mostrar_operacao(self: object) -> None:
        pass

