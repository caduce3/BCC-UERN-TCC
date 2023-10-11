import random
import serial
import pygame
import time
import os

pygame.init()

# Configurando a porta serial
ser = serial.Serial('COM5', 19200)

# Opções de áudio
audio_options = [
    'roboldo01.mp3',
    'roboldo02.mp3',
    'roboldo03.mp3',
    'roboldo04.mp3'
]

# Caminho absoluto para o diretório dos arquivos de áudio
audio_directory = r'C:\Users\caduc\Documents\BCC-UERN-TCC\python-speaks'

# Loop principal
while True:
    # Lendo a porta serial
    if ser.in_waiting > 0:
        serial_input = ser.readline().decode('utf-8').rstrip()
        if serial_input == "play_audio":
            # Carregando o arquivo de áudio de entrada
            audio_file = "roboldoEntradaW.mp3"
            audio_path = os.path.join(audio_directory, audio_file)
            print("MEU ARQUIVO >>>>> " + audio_path)
            if os.path.exists(audio_path):
                pygame.mixer.music.load(audio_path)
                pygame.mixer.music.set_volume(1)
            else:
                print('O arquivo ' + audio_file + ' não está no diretório de áudio')

            pygame.mixer.music.play()
            # time.sleep(30)  # espera 30 segundos antes de continuar com a execução do programa
        elif serial_input == "play_audio_fim":
            # Carregando o arquivo de áudio de saída
            audio_file = "roboldoSaidaW.mp3"
            audio_path = os.path.join(audio_directory, audio_file)
            print("MEU ARQUIVO >>>>> " + audio_path)
            if os.path.exists(audio_path):
                pygame.mixer.music.load(audio_path)
                pygame.mixer.music.set_volume(1)
            else:
                print('O arquivo ' + audio_file + ' não está no diretório de áudio')

            pygame.mixer.music.play()
            # time.sleep(30)  # espera 30 segundos antes de continuar com a execução do programa
        elif serial_input == "aprsEmocao":
            # Selecionando o arquivo de áudio a ser tocado
            audio_file = random.choice(audio_options)
            audio_path = os.path.join(audio_directory, audio_file)
            print("MEU ARQUIVO >>>>> " + audio_path)
            if os.path.exists(audio_path):
                pygame.mixer.music.load(audio_path)
                volume_atual = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(volume_atual * 1.5)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pass
            else:
                print('O arquivo ' + audio_file + ' não está no diretório de áudio')
