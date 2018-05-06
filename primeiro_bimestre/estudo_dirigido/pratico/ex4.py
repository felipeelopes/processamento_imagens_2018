#!/usr/bin/env python
import cv2
import numpy as np
from matplotlib import pyplot as plt


def fatiamento(img, lim_inf, lim_ext):

    # copiar imagem para nao trabalhar na original
    img_copy = img.copy()

    # obter tamanho da image
    linhas, colunas = img_copy.shape

    # percorrer imagem
    for i in range(0, int(linhas)):

        for j in range(0, colunas):

            # verifica se pixel esta no limite passado
            # caso nao esteja, preenchemos o pixel com 0
            # conforme orientacao do professor
            if(img.item(i, j) >= lim_inf and img.item(i, j) <= lim_ext):
                img_copy.itemset((i, j), img.item(i, j))
            else:
                img_copy.itemset((i, j), 0)

    return img_copy

if __name__ == '__main__':
    img = cv2.imread('../imagens/img03-d.jpg', cv2.IMREAD_GRAYSCALE)

    # exibir imagem
    cv2.imshow('Imagem Original', img)

    # negativar imagem
    img_destino = fatiamento(img, 200, 255)

    # mostrar negativo da imagem
    cv2.imshow('Imagem FATIADA', img_destino)

    # salvar imagens
    cv2.imwrite('resultados/ex4_original.png', img)
    cv2.imwrite('resultados/ex4_resultado.png', img_destino)

    # aguardar botao para continuar
    tecla = cv2.waitKey(0)