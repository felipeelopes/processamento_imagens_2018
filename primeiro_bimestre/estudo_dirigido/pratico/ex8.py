#!/usr/bin/env python
import cv2
import numpy as np
import bisect

from matplotlib import pyplot as plt


def max(img, mascara):
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
            mediana = []

            # percorre mascara
            for xx in range(-raio, +raio+1):
                tamanho = 0

                for yy in range(-raio, +raio+1):
                    # inserir itens na lista de mediana ja ordenada
                    bisect.insort_left(mediana, img.item(x - xx, y - yy))

            # imprime lista de mediana
            print(mediana)

            # seta o pixel da nova imagem com o valor do meio da lista
            img_filtrada.itemset((x, y), mediana[0])

    return img_filtrada


if __name__ == '__main__':
    img = cv2.imread('../imagens/img03-b.jpg', cv2.IMREAD_GRAYSCALE)

    # exibir imagem
    cv2.imshow('Imagem Original', img)

    # define mascara
    mascara = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

    # realiza filtro espacial na imagem
    img_filtrada = max(img, mascara)

    # exibe imagem filtrada
    cv2.imshow('Imagem Filtrada pelo meu algoritmo', img_filtrada)

    # salvar imagens
    cv2.imwrite('resultados/ex8_original.png', img)
    cv2.imwrite('resultados/ex8_resultado.png', img_filtrada)

    # aguardar botao para continuar
    tecla = cv2.waitKey(0)