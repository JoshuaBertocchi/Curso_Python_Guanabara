import pygame


pygame.mixer.init()


pygame.mixer.music.load(R"G:\0_Estudos_Python\Aula_04_SCRIPTS_INPUT_PRINT\Arquivo_Python_exercicio\Curso_em_video_python_exercicio\Exercício_aula_final\NAGALLI.mp3")


pygame.mixer.music.play()


while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)