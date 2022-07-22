import time
from dnaimage import imgdec
from PIL import Image
import numpy as np
from sewar.full_ref import mse
import warnings
warnings.filterwarnings("ignore")

tshape = (200,200,3)
imfile = "lena.enc.png"
original = np.array(Image.open("lena.jpg"),dtype=np.uint8)
if original.shape[-1] != 4:
        original = np.dstack((original, np.ones(original.shape[:-1])*255)).astype(np.uint8)


def changeb(x:int,pos):
    c={"1":"0","0":"1"}
    b=list(bin(x)[2:].zfill(32))
    b[pos] = c[b[pos]]
    b = int("".join(b),2)
    return b

k1,k2,k3,k4 = list(map(int,input("Enter keys with ' ' seperating them: ").split(" ")))

testcases = {
    "proper-decryption": [k1,k2,k3,k4],
    "1-missing": [0,k2,k3,k4],
    "2-missing": [k1,0,k3,k4],
    "3-missing": [k1,k2,0,k4],
    "4-missing": [k1,k2,k3,0],
    "1-2-missing": [0,0,k3,k4],
    "1-3-missing": [0,k2,0,k4],
    "1-4-missing": [0,k2,k3,0],
    "2-3-missing": [k1,0,0,k4],
    "2-4-missing": [k1,0,k3,0],
    "3-4-missing": [k1,k2,0,0],
    "1-msb":[changeb(k1,0),k2,k3,k4],
    "2-msb":[k1,changeb(k2,0),k3,k4],
    "3-msb":[k1,k2,changeb(k3,0),k4],
    "4-msb":[k1,k2,k3,changeb(k4,0)],
    "1-lsb":[changeb(k1,-1),k2,k3,k4],
    "2-lsb":[k1,changeb(k2,-1),k3,k4],
    "3-lsb":[k1,k2,changeb(k3,-1),k4],
    "4-lsb":[k1,k2,k3,changeb(k4,-1)]
}

for k,v in testcases.items():
    tic = time.time()
    print(f"Testing --{k}--")
    decrypted = imgdec(v,imfile,k+".png")
    toc = time.time()
    print(f"Difference from original MSE = {mse(original,decrypted)}")
    print(f"Time Taken {toc - tic}")
    print("")
