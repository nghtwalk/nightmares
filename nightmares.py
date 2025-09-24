import random
import time
import pygame
from colorama import init, Fore, Back, Style

init(autoreset=True)  # Inicializa colorama

pygame.mixer.init()

# Frases de pesadelo
frases = [
    "Você sente algo se mexendo atrás de você...",
    "O chão está cheio de mãos tentando te agarrar!",
    "Uma voz sussurra seu nome, mas ninguém está aí...",
    "Algo passa por você tão rápido que não consegue ver...",
    "O espelho mostra seu rosto, mas ele sorri sozinho...",
    "Uma sombra cresce e cresce até engolir a sala inteira...",
    "Olhos aparecem na escuridão, te observando...",
    "O tempo para, mas você continua se movendo sozinho..."
]

# ASCII Art de pesadelo
ascii_art = [
    r"""
      .-.
     (o o)
     | O \
      \   \
       `~~~'
    """,
    r"""
      (\_._/) 
      ( o o ) 
      /     \
     (       )
      `-._.-'
    """,
    r"""
      .-.
     /   \
     \_v_/
     (   )
      `~'
    """,
    r"""
     .----.
    / .-"-.\
   / /_   _\
   | |O| |O|
   | |__|__|
   \ \____/
    `------`
    """
]

def tocar_som():
    sons = ["scream.wav"]
    som = random.choice(sons)
    try:
        sound = pygame.mixer.Sound(som)
        sound.play()  # toca e segue sem travar
    except Exception as e:
        print(f"Erro ao tocar som: {e}")



def gerar_pesadelo(nome):
    print(Fore.RED + f"\n {nome}, seu pesadelo começa agora...\n")
    time.sleep(1)
    
    for _ in range(random.randint(3,6)):
        frase = random.choice(frases)
        arte = random.choice(ascii_art)
        
        # cores aleatórias
        cor = random.choice([Fore.RED, Fore.MAGENTA, Fore.YELLOW, Fore.CYAN])
        
        # piscada rápida
        for _ in range(2):
            print(cor + arte)
            time.sleep(0.3)
            print("\033c", end="")  # limpa o terminal
            time.sleep(0.3)
        
        print(cor + arte)
        print(Style.BRIGHT + frase) 
        print("\n...")
        time.sleep(2)
    
    print(Fore.GREEN + "\n O pesadelo acabou... por enquanto.\n")

# Programa principal
print(Fore.MAGENTA + " Bem-vindo ao Gerador de Pesadelos 2.0 ")
nome = input(Fore.CYAN + "Digite seu nome para começar: ")
gerar_pesadelo(nome)
