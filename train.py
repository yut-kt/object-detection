import dlib

TrainingXml = 'train/train.xml'
SvmFile = 'train/detector.svm'


def main():
    dlib.train_simple_object_detector(TrainingXml, SvmFile, get_options())


def get_options():
    options = dlib.simple_object_detector_training_options()

    # True -> 左右対象画像とみなし、左右反転させた画像を学習データとして増やす
    options.add_left_right_image_flips = True

    # True -> 学習中に情報を表示する
    options.be_verbose = True

    # 学習強度 大きくしすぎると過学習になるため注意
    options.C = 5

    # 並列実行数（CPUの数に設定すると最速）
    options.num_threads = 4

    return options


if __name__ == '__main__':
    main()
