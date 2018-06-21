#!/usr/local/bin/python3

import cv2
import numpy as np

if __name__ == '__main__':
    capture = cv2.VideoCapture('video/01.mp4')
    mascara_morfologia_a = np.ones((10, 10), np.uint8)
    mascara_morfologia_b = np.ones((8, 8), np.uint8)

    B = 0
    G = 1
    R = 2

    while(capture.isOpened()):
        ret, frame = capture.read()
        frame = cv2.pyrDown(frame)

        # criar copia do frame
        img_copia = frame
        linhas, colunas, z = img_copia.shape

        # criar uma imgem vazia
        mascara = np.ones((linhas, colunas), np.uint8)

        for i in range(1, linhas-1):
            for j in range(1, colunas-1):
                if img_copia.item(i, j, R) > 95 \
                    and img_copia.item(i, j, G) > 40 \
                    and img_copia.item(i, j, B) > 20 \
                    and (img_copia.item(i, j, R) - img_copia.item(i, j, G)) > 15 \
                    and img_copia.item(i, j, R) > img_copia.item(i, j, G) \
                    and img_copia.item(i, j, R) > img_copia.item(i, j, B):
                        mascara.itemset((i , j), 255)
                else:
                    mascara.itemset((i, j), 0)

        mascara = cv2.erode(mascara, mascara_morfologia_a, iterations=1)
        mascara = cv2.dilate(mascara, mascara_morfologia_b, iterations=8)
        mascara = cv2.erode(mascara, mascara_morfologia_a, iterations=1)

        cv2.imshow('frame', mascara)
        #print(f'X:{linhas} Y:{colunas}')
        cv2.waitKey(30)

    capture.release()
    cv2.destroyAllWindows()

