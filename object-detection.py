#! -*- coding: utf-8 -*-

import sys
import dlib
import cv2


def main():
    # 読みこむ画像
    img = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)
    out = img.copy()

    # 検出
    detector = dlib.simple_object_detector("train/detector.svm")
    dets = detector(img)

    # 四角形描写
    print(str(len(dets)))
    for d in dets:
        cv2.rectangle(out, (d.left(), d.top()), (d.right(), d.bottom()), (0, 0, 255), 2)

    cv2.imwrite("result.png", out)


if __name__ == '__main__':
    main()
