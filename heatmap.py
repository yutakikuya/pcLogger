import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from numpy import *

from gaussian_filter import gaussian_kernel, convolve, tile_and_reflect
#const
MAX_X = 1920
MAX_Y = 1080

#関数群
#2次元のデータを、pythonのmatplotlibを用いて一瞬で図に起こす
#http://qiita.com/AnchorBlues/items/0dd1499196670fdf1c46
def draw(data,name):  #cb_min,cb_max:カラーバーの下端と上端の値
    plt.figure(figsize=(10,4))  #図の縦横比を指定する
    plt.contourf(data,100)
    plt.colorbar()
    plt.savefig("wakam"+name+".png")
    plt.jet()
    plt.savefig("jet"+name+".png")
    plt.show()

#2次元情報ログを2次元ビンにボートする
def log2Mat(data,max_x,max_y):
    #ビンの作成
    scale = 10
    H_img = np.zeros((int(max_y/scale), int(max_x/scale)))
    #マウスの位置が同じ立った場合はじくための道具
    tmp_x = 0
    tmp_x = 0

    #ログデータをMAX_X x MAX_Yの数のビンのどれかにボートする
    for log in data:
        if (tmp_x != log[0:1][0] or tmp_y != log[1:2][0]) and (log[0:1][0] < max_x and log[1:2][0] < max_y):
            #前の要素情報を保持
            tmp_x = log[0:1][0]
            tmp_y = log[1:2][0]
            #特定のビン[x,y]にボートする
            H_img[int(log[1:2][0]/scale),int(log[0:1][0]/scale)] += 1
    return H_img
#2次元のmatrixにボートしたdataをheatmapに変換する
def drawHeatMap(logs,max_x,max_y):
    bins = log2Mat(logs,max_x,max_y)
    bin255 = 255/bins.max()*bins;
    print(bin255.max())
    gaussian_fitered_bins = convolve(bin255, gaussian_kernel(4, truncate=2.0))
    pil_img = Image.fromarray(np.uint8(255/gaussian_fitered_bins.max()*gaussian_fitered_bins))
    pil_img.save('lena_RGBs.jpg')
    print("bin m",bins.max())

    draw(bin255,"")
    draw(255/gaussian_fitered_bins.max()*gaussian_fitered_bins,"_gaussian")


#main処理
if __name__=="__main__":
    #ログデータ data format [x, y],....
    logs = np.loadtxt("text1497149675.1216633.csv",delimiter=",", usecols=(1,2))
    drawHeatMap(logs,MAX_X,MAX_Y)


    im  = array(Image.open('graph.png').convert('L'))
    print(im.shape, im.dtype)
    print(im)


# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.set_title('1st graph')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# fig.colorbar(H_img,ax=ax)
# plt.show()
