# Import Required Modules
import time
import random

# Tables Involved
CODES={
    0:{"00":"T","01":"A","10":"G","11":"C"},
    1:{"00":"A","01":"T","10":"C","11":"G"},
    2:{"00":"A","01":"C","10":"T","11":"G"},
    3:{"00":"C","01":"A","10":"G","11":"T"},
    4:{"00":"T","01":"G","10":"A","11":"C"},
    5:{"00":"G","01":"C","10":"T","11":"A"},
    6:{"00":"G","01":"T","10":"C","11":"A"},
    7:{"00":"C","01":"G","10":"A","11":"T"}
}
DECODES = {
    0:{'T':'00','A':'01','G':'10','C':'11'}, 
    1:{'A':'00','T':'01','C':'10','G':'11'}, 
    2:{'A':'00','C':'01','T':'10','G':'11'}, 
    3:{'C':'00','A':'01','G':'10','T':'11'}, 
    4:{'T':'00','G':'01','A':'10','C':'11'}, 
    5:{'G':'00','C':'01','T':'10','A':'11'}, 
    6:{'G':'00','T':'01','C':'10','A':'11'}, 
    7:{'C':'00','G':'01','A':'10','T':'11'}
}
dna_xor = {
    "G":{"G":"A","A":"G","C":"T","T":"C"},
    "A":{"G":"G","A":"A","C":"C","T":"T"},
    "C":{"G":"T","A":"C","C":"A","T":"G"},
    "T":{"G":"C","A":"T","C":"G","T":"A"}
}
dna_add = {
    "G":{"G":"C","A":"G","C":"T","T":"A"},
    "A":{"G":"G","A":"A","C":"C","T":"T"},
    "C":{"G":"T","A":"C","C":"A","T":"G"},
    "T":{"G":"A","A":"T","C":"G","T":"C"}
}
dna_sub = {
    "G":{"G":"A","A":"G","C":"T","T":"C"},
    "A":{"G":"T","A":"A","C":"C","T":"G"},
    "C":{"G":"G","A":"C","C":"A","T":"T"},
    "T":{"G":"C","A":"T","C":"G","T":"A"}
}
COMPLEMENT = {"A":"G","G":"A","T":"C","C":"T"}

# Get Binary String from ASCII values
def binstr(x): # Enter ASCII LIST
    binx = ""
    for i in x:
        binx += bin(i)[2:].zfill(8)
    return binx # Returns a string of binary numbers

# Get ASCII from binary string
def ascii(binstr): # Enter a string of binary numbers
    return [int(binstr[i:i+8],2) for i in range(0,len(binstr),8)] # Returns a list of ASCII values

# Get DNA Code
def code(DCR,binstr): # Enter a string of 0's and 1's
    val = DCR%8
    return "".join([CODES[val][binstr[i:i+2]] for i in range(0,len(binstr),2)]) # Returns DNA Sequence

# Decode DNA Sequence
def decode(DCR,dnastr): # Enter DNA Sequence
    val = DCR%8
    return "".join([DECODES[val][i] for i in dnastr]) # returns a string of binary numbers

# Moore Machine
def moore(DCR,dna): # Enter a DNA Sequence
    rnd = DCR%4
    stateInOut = {rnd : "A",(rnd+1)%4 : "T",(rnd+2)%4 : "C",(rnd+3)%4 : "G"}
    ttable = {
        "G":{0:(rnd+1)%4,1:rnd,2:(rnd+2)%4,3:(rnd+3)%4},
        "A":{0:(rnd+2)%4,1:(rnd+1)%4,2:(rnd+3)%4,3:rnd},
        "C":{0:rnd,1:(rnd+3)%4,2:(rnd+1)%4,3:(rnd+2)%4},
        "T":{0:(rnd+3)%4,1:(rnd+2)%4,2:rnd,3:(rnd+1)%4}
    }
    state = rnd
    for i in range(len(dna)):
        state = ttable[dna[i]][state]
        dna[i] = stateInOut[state]
    return dna # Returns a different DNA Sequence

# Reverse Moore Machine
def revMoore(DCR,dna): # Enter a DNA Sequence
    rnd = DCR%4
    stateOutIn = {"A":rnd,"T":(rnd+1)%4,"C":(rnd+2)%4,"G":(rnd+3)%4}
    rttable = {
        0:{(rnd+1)%4:"G",(rnd+2)%4:"A",rnd:"C",(rnd+3)%4:"T"},
        1:{rnd:"G",(rnd+1)%4:"A",(rnd+3)%4:"C",(rnd+2)%4:"T"},
        2:{(rnd+2)%4:"G",(rnd+3)%4:"A",(rnd+1)%4:"C",rnd:"T"},
        3:{(rnd+3)%4:"G",rnd:"A",(rnd+2)%4:"C",(rnd+1)%4:"T"}
    }
    state = rnd
    ndna = ""
    for i in range(len(dna)):
        fstate = stateOutIn[dna[i]]
        ndna += rttable[state][fstate]
        state = fstate
    return ndna # Returns a different DNA Sequence

# Key Generation Algorithm & Hyperchaotic System
def keygen(pt): # Enter the ASCII values in plain text
    DCR = round(time.time())
    y1 = random.getrandbits(10)
    y2 = random.getrandbits(10)
    y3 = random.getrandbits(10)
    y4 = random.getrandbits(10)    
    a = 36
    b = 36
    c = 28
    d = -16
    k = 0.5
    X1 = []
    X2 = [] 
    X3 = []
    X4 = []
    SUM = sum(pt)
    LEN = len(pt)
    y1 = abs(y1 - (float(SUM%100)/1000))
    y2 = abs(y2 - (float(SUM%100)/1000))
    y3 = abs(y3 - (float(SUM%100)/1000))
    y4 = abs(y4 - (float(SUM%100)/1000))
    ini = (y1,y2,y3,y4)

    for _ in range(LEN):
        y1 = a*(y2-y1)
        y2 = -1*(y1*y3) + (d*y1) + (c*y2) - y4
        y3 = (y1*y2)-(b*y3)
        y4 = y1+k
        y1 = abs(y1 - round(y1))
        y2 = abs(y2 - round(y2))
        y3 = abs(y3 - round(y3))
        y4 = abs(y4 - round(y4))
        X1.append(y1)
        X2.append(y2)
        X3.append(y3)
        X4.append(y4)
    keys = []
    for key in [X1,X2,X3,X4]:
        tmp = sorted(key)
        nkey = []
        for e in key:
            nkey.append(tmp.index(e))
        keys.append(nkey)
    for e in range(1,len(keys)):
        keys[e] = code(DCR,binstr(keys[e]))
    return DCR,keys,ini # Return DCR, keys -> [X1,dnaX2,dnaX3,dnaX4] and ini -> [y1,y2,y3,y4]

# Key Retreival Algorithm
def keyretr(ct,DCR,ini): # Enter Cipher Text, DCR,and ini - > [y1,y2,y3,y4] (Obtained from the Key Generation Process)
    y1,y2,y3,y4 = ini[0],ini[1],ini[2],ini[3]
    a = 36
    b = 36
    c = 28
    d = -16
    k = 0.5
    X1 = []
    X2 = [] 
    X3 = []
    X4 = []
    for _ in range(len(ct)//4):
        y1 = a*(y2-y1)
        y2 = -1*(y1*y3) + (d*y1) + (c*y2) - y4
        y3 = (y1*y2)-(b*y3)
        y4 = y1+k
        y1 = abs(y1 - round(y1))
        y2 = abs(y2 - round(y2))
        y3 = abs(y3 - round(y3))
        y4 = abs(y4 - round(y4))
        X1.append(y1)
        X2.append(y2)
        X3.append(y3)
        X4.append(y4)
    keys = []
    for key in [X1,X2,X3,X4]:
        tmp = sorted(key)
        nkey = []
        for e in key:
            nkey.append(tmp.index(e))
        keys.append(nkey)
    for e in range(1,len(keys)):
        keys[e] = code(DCR,binstr(keys[e]))
    return keys # Return keys -> [X1,dnaX2,dnaX3,dnaX4]

def encrypt(pt,DCR,keys): # Enter ASCII Values, DCR, keys -> [X1,dnaX2,dnaX3,dnaX4] 
    # Scramble Plain Text with index values of X1
    scrpt = []
    for i in keys[0]:
        scrpt.append(pt[i])
    # Convert X1 and Scrambled Plaintext into binary strings
    binx1 = binstr(keys[0])
    binpt = binstr(scrpt)
    binpt = list(binpt)
    # XOR binx1 and binpt
    for i in range(len(binpt)):
        binpt[i] = "0" if binpt[i] == binx1[i] else "1"
    binpt = "".join(binpt)
    # DNA Coding on binpt
    dna = code(DCR,binpt)
    # ADD dna , dnaX2
    dna1 = [dna_add[i][j] for i,j in zip(dna,keys[1])]
    # SUBTRACT dna1 , dnaX3
    dna2 = [dna_sub[i][j] for i,j in zip(dna1,keys[2])]
    # XOR dna2 , dnaX4
    dna3 = [dna_xor[i][j] for i,j in zip(dna2,keys[3])]
    # Pass dna3 as input to randomly generated moore machine
    dna4 = moore(DCR,dna3)

    # If DCR < 3 complement even indexes, else complement odd indexes
    if DCR%8 < 3:
        for i in range(len(dna4)):
            if i%2 == 0:
                dna4[i] = COMPLEMENT[dna4[i]]
    else:
        for i in range(len(dna4)):
            if i%2 != 0:
                dna4[i] = COMPLEMENT[dna4[i]]
    return "".join(dna4)

# Decryption Algorithm
def decrypt(ct,DCR,keys): # Enter Cipher Text, DCR, keys -> [X1,dnaX2,dnaX3,dnaX4]
    dna4 = list(ct)

    # Reverse Complement
    if DCR%8 < 3:
        for i in range(len(dna4)):
            if i%2 == 0:
                dna4[i] = COMPLEMENT[dna4[i]]
    else:
        for i in range(len(dna4)):
            if i%2 != 0:
                dna4[i] = COMPLEMENT[dna4[i]]

    # Reverse Moore Machine
    dna3 = revMoore(DCR,dna4)

    # Reverse DNA Operations
    dna2 = [dna_xor[i][j] for i,j in zip(dna3,keys[3])]
    dna1 = [dna_add[i][j] for i,j in zip(dna2,keys[2])]
    dna = [dna_sub[i][j] for i,j in zip(dna1,keys[1])]
    binx1 = binstr(keys[0])
    dnabin = list(decode(DCR,dna))
    # Reverse XOR between binx1 and binpt
    for i in range(len(dnabin)):
        dnabin[i] = "0" if dnabin[i] == binx1[i] else "1"
    binpt = "".join(dnabin)
    # Scrambled List of ASCII Values
    scrpt = ascii(binpt)
    # Unscramble using X1 indexes
    pt = []
    for i in range(len(scrpt)):
        pt.append(scrpt[keys[0].index(i)])
    return pt # Return ASCII in list of Plain Text Characters

# String Encryption Algorithm
def strenc(pt:str):
    inp = [ord(i) for i in pt]
    DCR,keys,ini = keygen(inp)
    ct = encrypt(inp,DCR,keys)
    return ct, DCR, ini

# String Decryption Algorithm
def strdec(ct:str,DCR,ini):
    keys = keyretr(ct,DCR,ini)
    pt = decrypt(ct,DCR,keys)
    pt = "".join([chr(i) for i in pt])
    return pt

# File Encryption Algorithm
def fileenc(fname:str):
    inp = open(fname,"rb").read()
    DCR,keys,ini = keygen(inp)
    out = open(f"{fname}.enc","w")
    ct = encrypt(inp,DCR,keys)
    out.write(ct)
    out.close()
    return DCR, ini

# File Decryption Algorithm
def filedec(cf:str,DCR,ini):
    ct = open(cf,"r").readlines()[0]
    fname = cf.split(".")[0] + ".dec"
    keys = keyretr(ct,DCR,ini)
    pt = decrypt(ct,DCR,keys)
    pt = bytearray(pt)
    pt = bytes(pt)
    f = open(fname,"wb")
    f.write(pt)
    f.close()