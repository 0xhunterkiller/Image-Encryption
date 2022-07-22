from dnaimage import imgenc,imgdec
import time
op = int(input("Do you want to encrypt or decrypt?\n1)Encrypt\n2)Decrypt\nOption: "))
if op == 1:
    print("---Encryption---")
    pt = input("Enter your image name : ")
    tic = time.time()
    keys = imgenc(pt)
    print("Keys: "," ".join(map(str,keys)))
    toc = time.time()
    print(f"Finished in {toc-tic} seconds!")
    print("---Done!---")
elif op == 2:
    print("---Decryption---")
    imfile = input("Enter Encrypted Image: ")
    keys = list(map(int,input("Enter Keys with ' ' in between : ").split(" ")))
    output = input("Enter Output filename: ")
    tic = time.time()
    imgdec(keys,imfile,output)
    toc = time.time()
    print(f"Finished in {toc-tic} seconds!")
    print("---Done!---")
else:
    print("Invalid Input")