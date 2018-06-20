#!/usr/local/bin/python3

import cv2
import numpy as np

def transforma_binario(imagem):
    ret, img_bin = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)
    return img_bin

def rotulo_vizinho(imagem, i, j):
    rotulo = 255
    for ii in range(i-1, i+2):
        for jj in range(j-1, j+2):
            if imagem.item(ii, jj) != 0 and imagem.item(ii, jj) < rotulo:
                rotulo = imagem.item(ii, jj)

    return rotulo

def rotular(imagem):
    alterou = True
    rotulo = 10
    linhas, colunas = imagem.shape
    lista_rotulos = []

    while(alterou == True):
        alterou = False

        # loop inicia em 1 para ignorar as bordas e nao dar erro
        for i in range(1, linhas-1):
            for j in range(1, colunas-1):

                if imagem.item(i, j) != 0:
                    rv = rotulo_vizinho(imagem, i, j)

                    if rv == 255:
                        imagem.itemset((i, j), rotulo)
                        rotulo += 1
                        alterou = True
                    elif rv != imagem.item(i, j):
                        imagem.itemset((i, j), rv)
                        alterou = True

    # pega os rotulos atuais da imagem
    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            # adiciona o rotulo na lista para fazer a contagem posteriormente
            rotulo = imagem.item(i, j)
            if rotulo not in lista_rotulos:
                lista_rotulos.append(rotulo)

    return imagem, lista_rotulos

if __name__ == '__main__':
    # foi carregado as duas imagens devido a particularidades de ambas, necessario ajustes morfologicos diferentes para as duas imagens
    img_a = cv2.imread('img01-a.png', 0)
    img_b = cv2.imread('img01-b.png', 0)

    # transforma as imagems em binaria
    img_binaria_a = transforma_binario(img_a)
    img_binaria_b = transforma_binario(img_b)

    # realizar ajustes de morfologia na imagem A
    # mascara testada com resultado melhor 3x3
    mascara = np.ones((3, 3), np.uint8)
    img_binaria_a = cv2.dilate(img_binaria_a, mascara, iterations=1)
    img_binaria_a = cv2.erode(img_binaria_a, mascara, iterations=2)
    img_binaria_a = cv2.morphologyEx(img_binaria_a, cv2.MORPH_OPEN, mascara)
    img_binaria_a = cv2.dilate(img_binaria_a, mascara, iterations=2)

    # realizar ajustes de morfologia na imagem B
    img_binaria_b = cv2.dilate(img_binaria_b, mascara, iterations=1)
    img_binaria_b = cv2.erode(img_binaria_b, mascara, iterations=2)
    img_binaria_b = cv2.morphologyEx(img_binaria_b, cv2.MORPH_OPEN, mascara)
    img_binaria_b = cv2.dilate(img_binaria_b, mascara, iterations=3)

    # rotula a imagem
    img_rotulada_a, lista_rotulos_a = rotular(img_binaria_a)
    img_rotulada_b, lista_rotulos_b = rotular(img_binaria_b)

    cv2.imshow("img_rotulada_a", img_rotulada_a)
    cv2.imshow("img_rotulada_b", img_rotulada_b)

    # foi subtraido 2 da contagem da lista para descontar a borda branca da imagem e o rotulo preto.
    print(f'Total de moedas na figura A: {len(lista_rotulos_a)-2}')
    print(f'Total de moedas na figura B: {len(lista_rotulos_b)-2}')

    cv2.waitKey(0)
    cv2.destroyAllWindows()
