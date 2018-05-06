#!/usr/bin/env python
import cv2
import numpy as np
from matplotlib import pyplot as plt


def media(img, mascara):
    img_filtrada = img.copy()

    # obter tamanho da image
    linhas, colunas = img.shape

    # obter tamanho da mascara
    mask_linhas, mask_colunas = mascara.shape

    # validar mascara
    if (mask_linhas != mask_colunas):
        raise Exception("Problemas no tamanho da mascara, verifique!")

    # obtem raio da mascara, utilizado para se orientar dentro da matriz com a mascara aplicada
    raio = (mask_linhas) / 2
    print("Raio = {}".format(raio))

    # percorrendo imagem ignorando as bordas
    for x in range(raio, linhas - raio):

        for y in range(raio, colunas - raio):
            media_i = 0
            tamanho = 0

            # percorre mascara
            for xx in range(-raio, +raio+1):

                for yy in range(-raio, +raio+1):
                    media_i += img.item(x - xx, y - yy)
                    tamanho = tamanho + 1

            print("Tamanho = {} Media = {},{}({}) = {}".format(tamanho, x, y, img.item(x, y), media_i / tamanho))
            img_filtrada.itemset((x, y), media_i / tamanho)

    return img_filtrada


if __name__ == '__main__':
    img = cv2.imread('../imagens/img03-b.jpg', cv2.IMREAD_GRAYSCALE)

    # exibir imagem
    cv2.imshow('Imagem Original', img)

    # define mascara
    mascara = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

    # realiza filtro espacial na imagem
    img_filtrada = media(img, mascara)

    # realiza filtro pelo algoritmo do opencv para comparacao
    img_filtrada_opencv = cv2.blur(img, (3, 3))

    # exibe imagem filtrada
    cv2.imshow('Imagem Filtrada pelo meu algoritmo', img_filtrada)
    cv2.imshow('Imagem Filtrada pelo algoritmo opencv', img_filtrada_opencv)

    # salvar imagens
    cv2.imwrite('resultados/ex5_original.png', img)
    cv2.imwrite('resultados/ex5_resultado_felipe.png', img_filtrada)
    cv2.imwrite('resultados/ex5_resultado_opencv.png', img_filtrada_opencv)

    # aguardar botao para continuar
    tecla = cv2.waitKey(0)