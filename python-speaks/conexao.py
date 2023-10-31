import socket
import serial
import pygame
import os
import random
import time
import serial
from tkinter import *

pygame.init()


# Configurando a porta serial
ser = serial.Serial('COM5', 19200)

def send_command(cod):
    aux = str(cod)
    ser.write(aux.encode())

# Caminho absoluto para o diretório dos arquivos de áudio C1
audio_directory = r'C:\Users\caduc\Documents\BCC-UERN-TCC\python-speaks\aud-c1'

# Caminho absoluto para o diretório dos arquivos de áudio C2
# audio_directory = r'C:\Users\caduc\Documents\BCC-UERN-TCC\python-speaks\aud-c2'

#AUDIOS CONDIÇÃO 1 -  Roboldo erra e coloca a culpa no jogador 
audio_options_c1 = [
    'c1-1.mp3',
    'c1-2.mp3',
    'c1-3.mp3',
    'c1-4.mp3',
    'c1-5.mp3',
]

#AUDIOS CONDIÇÃO 2 - Roboldo erra e coloca a culpa nele mesmo ou no programador
# audio_options_c2 = [
#     'c2-1.mp3',
    # 'c2-2.mp3',
    # 'c2-3.mp3',
    # 'c2-4.mp3',
    # 'c2-5.mp3',
# ]


audio_directory_acerto = r'C:\Users\caduc\Documents\BCC-UERN-TCC\python-speaks\acerto'
#AUDIOS ACERTO DO USUÁRIO
audio_options_acerto = [
    'acerto1.mp3',
    'acerto2.mp3',
    'acerto3.mp3',
    'acerto4.mp3',
    'acerto5.mp3',
]


audio_directory_acerto_roboldo = r'C:\Users\caduc\Documents\BCC-UERN-TCC\python-speaks\acerto-roboldo'
#AUDIOS ACERTO DO ROBOLDO
audio_options_acerto_roboldo = [
    'acerto1.mp3',
    'acerto2.mp3',
    'acerto3.mp3'
]

HOST = 'localhost'
PORT = 3005

def processar_mensagem(message):
    if message == "1":
        # print("O usuário acertou")
        #time.sleep(3)
        audio_file = os.path.join(audio_directory_acerto, random.choice(audio_options_acerto))
    elif message == "0":
        # print("O roboldo errou")
        #time.sleep(3)
        send_command('0')  # Envie '0' como uma string codificada em UTF-8
        resposta_arduino = ser.read()
        print(resposta_arduino)
        audio_file = os.path.join(audio_directory, random.choice(audio_options_c1))
    elif message == "2":
        # print("O roboldo acertou")
        #time.sleep(3)
        send_command('2')  # Envie '2' como uma string codificada em UTF-8
        resposta_arduino = ser.read()
        print(resposta_arduino)
        audio_file = os.path.join(audio_directory_acerto_roboldo, random.choice(audio_options_acerto_roboldo))
    elif message == "3":
        # print("O jogador venceu")
        audio_file = os.path.join(audio_directory, 'saida.mp3')
    elif message == "4":
         # print("O Roboldo venceu")
        audio_file = os.path.join(audio_directory, 'saida.mp3')
    elif message == "5":
         # print("EMPATE")
        audio_file = os.path.join(audio_directory, 'saida.mp3')
    elif message == 'inicio':
        audio_file = os.path.join(audio_directory, 'entrada.mp3')
    else:
        print("Mensagem não reconhecida")

    if message in ["0", "1", "2", "3", "4", "5", "inicio"]:
        sound = pygame.mixer.Sound(audio_file)
        sound.play()
        pygame.time.wait(int(sound.get_length() * 1000))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print('Aguardando conexões...')

    while True:
        conn, addr = server_socket.accept()
        print('Conectado por', addr)
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                message = data.decode('utf-8')
                print('Recebido:', message)
                processar_mensagem(message)
