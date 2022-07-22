from dna import fileenc,filedec

while True:
    pt = input("Enter your Filename : ")
    DCR, ini = fileenc(pt)
    
    print(f"DCR: {DCR}")
    print(f"ini: {ini[0]} {ini[1]} {ini[2]} {ini[3]}")
    print("-"*50)
    print("---Decryption---")
    ct = input("Enter Cipher File: ")
    DCR = int(input("DCR: "))
    ini = list(map(float,input("Enter y1 y2 y3 y4:").split(" ")))
    print("-"*50)
    filedec(ct,DCR,ini)
    print("Check local directory for decrypted file :)")
    print("-"*50)