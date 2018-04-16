#!/usr/bin/env python
import cv2
import numpy as np
from matplotlib import pyplot as plt


def gamma(img, gamma):

    # copiar imagem para nao trabalhar na original
    img_copy = img.copy()

    # declaracao da constante solicitada pela expressao mateimatica T(r) = cr ^ y
    const_c = 1

    # obter tamanho da image
    linhas, colunas = img_copy.shape

    # percorrer imagem
    for i in range(0, int(linhas)):
        for j in range(0, colunas):
            correcao_gama = const_c * (img_copy.item(i, j) ** gamma)
            img_copy.itemset((i, j), correcao_gama)

    return img_copy

if __name__ == '__main__':
    img = cv2.imread('../imagens/img03-d.jpg', cv2.IMREAD_GRAYSCALE)

    # exibir imagem
    cv2.imshow('Imagem Original', img)

    # corrigir gama da imagem
    img_destino = gamma(img, 0.8)

    # mostrar imagem limirizada
    cv2.imshow('Imagem com correcao de GAMMA', img_destino)

    # aguardar botao para continuar
    tecla = cv2.waitKey(0)