#!/usr/bin/env python
import cv2
import numpy as np
from matplotlib import pyplot as plt


def limiarizacao(img, limiar):
    val, nova_imagem = cv2.threshold(img, limiar, 255, cv2.THRESH_BINARY)
    return nova_imagem

if __name__ == '__main__':
    img = cv2.imread('../imagens/img02-a.jpg', cv2.IMREAD_GRAYSCALE)

    # exibir imagem
    cv2.imshow('Imagem Original', img)

    # limiarizar imagem
    img_limiarizada = limiarizacao(img, 127)

    # mostrar imagem limirizada
    cv2.imshow('Imagem Limiarizada', img_limiarizada)

    # aguardar botao para continuar
    tecla = cv2.waitKey(0)