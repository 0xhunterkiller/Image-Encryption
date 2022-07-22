from dna import strenc,strdec

while True:
    pt = input("Enter your String : ")
    ct, DCR, ini = strenc(pt)
    
    print(f"DCR: {DCR}")
    print(f"ini: {ini[0]} {ini[1]} {ini[2]} {ini[3]}")
    print(f"Cipher Text: {ct}\n")
    print("-"*50)
    print("---Decryption---")
    ct = input("Enter Cipher Text: ")
    DCR = int(input("DCR: "))
    ini = list(map(float,input("Enter y1 y2 y3 y4:").split(" ")))
    print("-"*50)
    print(strdec(ct,DCR,ini))
    print("-"*50)
