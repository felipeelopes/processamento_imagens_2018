#!/usr/bin/env python
import cv2
import numpy as np
from matplotlib import pyplot as plt

'''TODO: Estudar esse metodo, nao ficou claro. Foi realizado a media dos pixels vizinhos'''

def media(img, mascara):
    img_filtrada = img.copy()

    # obter tamanho da image
    linhas, colunas = img.shape

    # criar a imagem filtrada
    for i in range(0, int(linhas)):

        for j in range(0, colunas):

            # primeira linha
            if(i == 0 and j == 0):
                media = ((img.item(i, j + 1) + img.item(i + 1, j) + img.item(i + 1, j + 1)) / 3)
                img_filtrada.itemset((i, j), media)
            if (i == 0 and j == colunas):
                media = ((img.item(i, j - 1) + img.item(i - 1, j - 1) + img.item(i + 1, j)) / 3)
                img_filtrada.itemset((i, j), media)
            if (i == 0 and j != 0 and j != colunas and j + 1 < colunas):
                media = ((img.item(i, j - 1) + img.item(i, j + 1) + img.item(i + 1, j - 1) +
                          img.item(i + 1, j) + img.item(i + 1, j + 1)) / 5)
                img_filtrada.itemset((i, j), media)

            # ultima linha
            if(i == linhas and j == 0):
                media = ((img.item(i - 1, j) + img.item(i - 1, j + 1) + img.item(i, j + 1)) / 3)
                img_filtrada.itemset((i, j), media)
            if(i == linhas and j == colunas):
                media = ((img.item(i - 1, j) + img.item(i - 1, j - 1) + img.item(i, j - 1)) / 3)
                img_filtrada.itemset((i, j), media)
            if(i == linhas and j!= 0 and j != colunas):
                media = ((img.item(i, j - 1) + img.item(i - 1, j - 1) + img.item(i - 1, j) +
                          img.item(i - 1, j + 1) + img.item(i, j + 1)) / 5)
                img_filtrada.itemset((i, j), media)

            # primeira coluna
            if(i != 0 and i != linhas and j == 0 and i + 1 < linhas):
                media = ((img.item(i - 1, j) + img.item(i - 1, j + 1) + img.item(i, j + 1) +
                          img.item(i + 1, j) + img.item(i + 1, j + 1)) / 5)
                img_filtrada.itemset((i, j), media)

            # ultima coluna
            if(i != 0 and i != linhas and j == colunas):
                media = ((img.item(i - 1, j) + img.item(i - 1, j - 1) + img.item(i, j - 1) +
                          img.item(i + 1, j - 1) + img.item(i + 1, j)) / 5)
                img_filtrada.itemset((i, j), media)

            # meio
            if(i != 0 and j != 0 and i != linhas and j != colunas and i + 1 < linhas and j + 1 < colunas):
                media = ((img.item(i - 1, j - 1) + img.item(i - 1, j) + img.item(i - 1, j + 1) +
                          img.item(i, j - 1) + img.item(i, j + 1) +
                          img.item(i + 1, j - 1) + img.item(i + 1, j) + img.item(i + 1, j + 1)) / 8)
                img_filtrada.itemset((i, j), media)

    # verificar se tamanho do filtro bate com o tamanho da imagem
    if(np.shape(img_filtrada) != np.shape(img)):
        raise Exception("Tamanho da imagem filtrada diferente da imagem original!")

    return img_filtrada


if __name__ == '__main__':
    img = cv2.imread('../imagens/img03-b.jpg', cv2.IMREAD_GRAYSCALE)

    # exibir imagem
    cv2.imshow('Imagem Original', img)

    img_filtrada = media(img, 100)

    cv2.imshow('Imagem Filtrada', img_filtrada)

    # aguardar botao para continuar
    tecla = cv2.waitKey(0)