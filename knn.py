import pylab as pl
import math
from operator import itemgetter

def printImg(img):
    for i in range(0,28):
        col = ""
        for j in range(0,28):
            if img[i*28 + j] == 0:
                col = col + " "
            else:
                col = col + "0 "
        print(col)

def img_distance(img1, img2):
    result = 0
    for i in range(0,len(img1)):
        result += math.fabs(img1[i]-img2[i])
    return result

def readMnistData(filename, lab_filename):
    imgs = open(filename, mode='rb')
    labels = open(lab_filename, mode='rb')

    imgs.read(4)
    labels.read(4)
    labels.read(4)

    img_num = int.from_bytes(imgs.read(4), byteorder="big")
    cols = int.from_bytes(imgs.read(4), byteorder="big")
    rows = int.from_bytes(imgs.read(4), byteorder="big")

    lists = [[],[]]

    img_num = 100

    for i in range(0,img_num):
        pixel_list = []
        for j in range(0, rows):
            for k in range(0, cols):
                pixel_list.append(int.from_bytes(imgs.read(1), byteorder="big"))

        label = int.from_bytes(labels.read(1), byteorder="big")
        lists[0].append(pixel_list)
        lists[1].append(label);

    return lists;

def predict(test_img,training_set_lists,knn):
    distance_list = []

    for img, label in zip(training_set_lists[0], training_set_lists[1]):
        distance_list.append([img_distance(test_img, img), label]);

    distance_list.sort(key=itemgetter(0))

    labels = [0,0,0,0,0,0,0,0,0,0]

    for i in range(0,knn):
        labels[distance_list[i][1]] += 1

    result = labels.index(max(labels))

    return result


training_set_lists = readMnistData("train-images.idx3-ubyte","train-labels.idx1-ubyte")
test_set_lists = readMnistData("t10k-images.idx3-ubyte","t10k-labels.idx1-ubyte")

knn = 3

right = 0
wrong = 0

for img,label in zip(test_set_lists[0], test_set_lists[1]):
    result = predict(img, training_set_lists, knn)
    if result == label:
        right += 1
    else:
        wrong += 1

print("Right: " + str(right) + " Wrong: " + str(wrong))
