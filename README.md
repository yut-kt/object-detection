# object-detection

HOG特徴をSVMで学習する方法で物体検出を行う

## 訓練データの作成
Dlibによって訓練データを作成する

### Install

DlibをビルドするためにCMakeをインストール
```
$ brew install cmake
```

GUIによって訓練データを作成するために[X11（XQuartz）](https://www.xquartz.org/)をインストール後、シンボリックリンクを貼る
```
$ export CPPFLAGS=-I/opt/X11/include
$ ln -s /opt/X11/include/X11 /usr/local/include/X11
```

Dlibをインストール
```
$ git clone https://github.com/davisking/dlib.git
```

画像中の座標を指定したXMLファイルを作成する必要があるため、それを行うdlib中のimglabをビルドする
```
$ cd dlib/tools/imglab/
$ mkdir build
$ cd build
$ cmake ..
$ cmake --build . --config Release
```

### 矩形選択

画像ファイルのXMLリストを作成
```
$ cd ../../../../
$ ./dlib/tools/imglab/build/imglab -c train/all.xml train
```

GUIにより矩形選択する
```
$ ./dlib/tools/imglab/build/imglab train/all.xml
```

矩形選択し終えたらSaveAsよりtrain/train.xmlとして保存

## 分類器の作成
作成した訓練データからSVMの分類器を作成

### Install

pythonからdlibを使用するモジュールをインストール
```
$ pip install dlib==19.12.0
```

### 学習
```
$ python train.py
```

## SVMによる物体検出
作成した分類器によってメーターの矩形を検出

### Install
検出した物体を枠付けるためにopencvを使用する
```
$ pip install opencv-python==3.4.1.15
```

### 物体検出
```
$ python object-detection.py 画像パス
```

物体検出した場所を枠で囲んだresult.pngが生成されている