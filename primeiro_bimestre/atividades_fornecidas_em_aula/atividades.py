#!/usr/bin/env python

#Importando bibliotecas
import cv2
import numpy as np

# definicoes
# define usado para o exercicio 3
nome_arquivo_ex3_png = 'exercicio_3.png'
nome_arquivo_ex3_jpg = 'exercicio_3.jpg'

# INREAD = LER IMAGEM EM DISCO
img = cv2.imread('a.jpg', cv2.IMREAD_GRAYSCALE)
img_negativa = cv2.imread('a.jpg', cv2.IMREAD_GRAYSCALE)

# atividade 1
# convertendo a imagem para negativa
img_negativa = cv2.bitwise_not(img_negativa)

cv2.imshow('imagem_original', img)
cv2.imshow('exercicio_1', img_negativa)

# atividade 1 - salvar imagem negativa
cv2.imwrite('exercicio_1.jpg', img_negativa)

# atividade 2
# salvar numero de linas e colunas da imagem
linhas, colunas = img.shape

# loop para ler pixel a pixel
for i in range(0, linhas):
    for j in range(0, colunas):
        # caso o pixel seja menor que 100
        if (img.item(i,j) < 100):
            img.itemset((i, j), 0)
        #caso o pixel seja maior que 255
        if (img.item(i,j) > 200):
            img.itemset((i, j), 255)

# exibe mensagem convertida no exercicio 2
cv2.imshow('exercicio_2', img)
cv2.imwrite('exercicio_2.jpg', img)

# exercicio 3
# como ja abrimos a imagem no topo da tela, vamos apenas salva-la em png
cv2.imwrite(nome_arquivo_ex3_png, img)
cv2.imwrite(nome_arquivo_ex3_jpg, img)

# com a imagem ja salva, vamos abrir a nova imagem
img_ex3_png = cv2.imread(nome_arquivo_ex3_png, cv2.IMREAD_GRAYSCALE)
img_ex3_jpg = cv2.imread(nome_arquivo_ex3_jpg, cv2.IMREAD_GRAYSCALE)

# exercicio 4, diferenca de imagem
# criar uma imagem em branco
img_branco = np.zeros(img_ex3_jpg.shape, np.uint8)

# salvar numero de linas e colunas da imagem par ao exercicio 4
linhasA, colunasB = img_ex3_jpg.shape

for i in range(0, linhasA):
    for j in range(0, colunasB):
        dig = (img_ex3_png.item(i,j) - img_ex3_jpg.item(i,j))
        img_branco.itemset((i, j), dig)

cv2.imshow('exercicio_4', img_branco)
cv2.imwrite('exercicio_4.jpg', img_branco)

# exercicio 5, virar de ponta cabeca
img_rotacionada_aux = cv2.getRotationMatrix2D((colunas/2, linhas/2), 180, 1)
img_rotacionada = cv2.warpAffine(img, img_rotacionada_aux, (colunas, linhas))

cv2.imshow('exercicio_5', img_rotacionada)
cv2.imwrite('exercicio_5.jpg', img_rotacionada)

# para manter a imagem abaixo, deixamos o programa esperando uma tecla
tecla = cv2.waitKey(0)

print(img.shape)