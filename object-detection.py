#! -*- coding: utf-8 -*-

import sys
import dlib
import cv2

RectangleColor = (0, 0, 255)  # red
Thickness = 2  # 矩形の太さ（px）


def main():
    # 読みこむ画像
    img = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)
    out = img.copy()

    # 検出
    detector = dlib.simple_object_detector("train/detector.svm")
    detected_imgs = detector(img)

    # 四角形描写
    for detected_img in detected_imgs:
        top, left, right, bottom = get_four_corners(detected_img)
        cv2.rectangle(out, (left, top), (right, bottom), RectangleColor, Thickness)

    cv2.imwrite("result.png", out)


def get_four_corners(detected_img):
    top = detected_img.top()
    left = detected_img.left()
    right = detected_img.right()
    bottom = detected_img.bottom()
    return top, left, right, bottom


if __name__ == '__main__':
    main()
