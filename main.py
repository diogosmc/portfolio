from colorama import Fore, init
from blocon import *
from conect import *
from tempon import ver_tempo
import sys


init(convert=True, autoreset=True)
print(Fore.YELLOW+ 'Olá Bem Vindo ao BOT para Ativos ( Somente Paridades Digitais ) !!!')
print('-Feito por : Diogo\n')


conectar(email,senha,rp)
par = verificar_par(par)
entrada = ver_entradas(entrada)
direcao = ver_direcao(direcao)
timeframe = ver_timeframe(timef)

print(Fore.CYAN+ 'Sempre lembre de verificar os valores para não dar error!')

ver_tempo(tempo)
ver_gale(par,entrada,direcao,gale,timeframe)

