#!/usr/bin/env python
import cv2
import numpy as np
from matplotlib import pyplot as plt


def negativo(img):

    # copiar imagem para nao trabalhar na original
    img_copy = img.copy()

    # obter tamanho da image
    linhas, colunas = img_copy.shape

    # percorrer imagem
    for i in range(0, int(linhas)):
        for j in range(0, colunas):
            negativo = 255 - img.item(i, j)
            img_copy.itemset((i, j), negativo)

    return img_copy

if __name__ == '__main__':
    img = cv2.imread('../imagens/img03-d.jpg', cv2.IMREAD_GRAYSCALE)

    # exibir imagem
    cv2.imshow('Imagem Original', img)

    # negativar imagem
    img_destino = negativo(img)

    # mostrar negativo da imagem
    cv2.imshow('Imagem NEGATIVA', img_destino)

    # aguardar botao para continuar
    tecla = cv2.waitKey(0)