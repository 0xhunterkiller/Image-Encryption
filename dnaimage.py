# Import Required Modules
from PIL import Image
import random
import numpy as np

# Making the CODES List
cdna = []
cbin = []
count = 0
for i in "ATGC":
    for j in "ATGC":
        for k in "ATGC":
            for l in "ATGC":
                cdna.append(i+j+k+l)
for i in range(256):
    cbin.append(bin(i)[2:].zfill(8))
DECODES = {}
for i in range(256):
    DECODES[i] = {}
    cdnal = cdna[i:] + cdna[:i]
    for j in range(256):
        DECODES[i][cdnal[j]] = cbin[j]

# Making the DECODES List
CODES = {}
for i in range(256):
    CODES[i] = {v:k for k,v in DECODES[i].items()} 

Sbox = [
0x63,0x7c,0x77,0x7b,0xf2,0x6b,0x6f,0xc5,0x30,0x01,0x67,0x2b,0xfe,0xd7,0xab,0x76,
0xca,0x82,0xc9,0x7d,0xfa,0x59,0x47,0xf0,0xad,0xd4,0xa2,0xaf,0x9c,0xa4,0x72,0xc0,
0xb7,0xfd,0x93,0x26,0x36,0x3f,0xf7,0xcc,0x34,0xa5,0xe5,0xf1,0x71,0xd8,0x31,0x15,
0x04,0xc7,0x23,0xc3,0x18,0x96,0x05,0x9a,0x07,0x12,0x80,0xe2,0xeb,0x27,0xb2,0x75,
0x09,0x83,0x2c,0x1a,0x1b,0x6e,0x5a,0xa0,0x52,0x3b,0xd6,0xb3,0x29,0xe3,0x2f,0x84,
0x53,0xd1,0x00,0xed,0x20,0xfc,0xb1,0x5b,0x6a,0xcb,0xbe,0x39,0x4a,0x4c,0x58,0xcf,
0xd0,0xef,0xaa,0xfb,0x43,0x4d,0x33,0x85,0x45,0xf9,0x02,0x7f,0x50,0x3c,0x9f,0xa8,
0x51,0xa3,0x40,0x8f,0x92,0x9d,0x38,0xf5,0xbc,0xb6,0xda,0x21,0x10,0xff,0xf3,0xd2,
0xcd,0x0c,0x13,0xec,0x5f,0x97,0x44,0x17,0xc4,0xa7,0x7e,0x3d,0x64,0x5d,0x19,0x73,
0x60,0x81,0x4f,0xdc,0x22,0x2a,0x90,0x88,0x46,0xee,0xb8,0x14,0xde,0x5e,0x0b,0xdb,
0xe0,0x32,0x3a,0x0a,0x49,0x06,0x24,0x5c,0xc2,0xd3,0xac,0x62,0x91,0x95,0xe4,0x79,
0xe7,0xc8,0x37,0x6d,0x8d,0xd5,0x4e,0xa9,0x6c,0x56,0xf4,0xea,0x65,0x7a,0xae,0x08,
0xba,0x78,0x25,0x2e,0x1c,0xa6,0xb4,0xc6,0xe8,0xdd,0x74,0x1f,0x4b,0xbd,0x8b,0x8a,
0x70,0x3e,0xb5,0x66,0x48,0x03,0xf6,0x0e,0x61,0x35,0x57,0xb9,0x86,0xc1,0x1d,0x9e,
0xe1,0xf8,0x98,0x11,0x69,0xd9,0x8e,0x94,0x9b,0x1e,0x87,0xe9,0xce,0x55,0x28,0xdf,
0x8c,0xa1,0x89,0x0d,0xbf,0xe6,0x42,0x68,0x41,0x99,0x2d,0x0f,0xb0,0x54,0xbb,0x16 ]

InvSbox = [
0x52,0x09,0x6a,0xd5,0x30,0x36,0xa5,0x38,0xbf,0x40,0xa3,0x9e,0x81,0xf3,0xd7,0xfb,
0x7c,0xe3,0x39,0x82,0x9b,0x2f,0xff,0x87,0x34,0x8e,0x43,0x44,0xc4,0xde,0xe9,0xcb,
0x54,0x7b,0x94,0x32,0xa6,0xc2,0x23,0x3d,0xee,0x4c,0x95,0x0b,0x42,0xfa,0xc3,0x4e,
0x08,0x2e,0xa1,0x66,0x28,0xd9,0x24,0xb2,0x76,0x5b,0xa2,0x49,0x6d,0x8b,0xd1,0x25,
0x72,0xf8,0xf6,0x64,0x86,0x68,0x98,0x16,0xd4,0xa4,0x5c,0xcc,0x5d,0x65,0xb6,0x92,
0x6c,0x70,0x48,0x50,0xfd,0xed,0xb9,0xda,0x5e,0x15,0x46,0x57,0xa7,0x8d,0x9d,0x84,
0x90,0xd8,0xab,0x00,0x8c,0xbc,0xd3,0x0a,0xf7,0xe4,0x58,0x05,0xb8,0xb3,0x45,0x06,
0xd0,0x2c,0x1e,0x8f,0xca,0x3f,0x0f,0x02,0xc1,0xaf,0xbd,0x03,0x01,0x13,0x8a,0x6b,
0x3a,0x91,0x11,0x41,0x4f,0x67,0xdc,0xea,0x97,0xf2,0xcf,0xce,0xf0,0xb4,0xe6,0x73,
0x96,0xac,0x74,0x22,0xe7,0xad,0x35,0x85,0xe2,0xf9,0x37,0xe8,0x1c,0x75,0xdf,0x6e,
0x47,0xf1,0x1a,0x71,0x1d,0x29,0xc5,0x89,0x6f,0xb7,0x62,0x0e,0xaa,0x18,0xbe,0x1b,
0xfc,0x56,0x3e,0x4b,0xc6,0xd2,0x79,0x20,0x9a,0xdb,0xc0,0xfe,0x78,0xcd,0x5a,0xf4,
0x1f,0xdd,0xa8,0x33,0x88,0x07,0xc7,0x31,0xb1,0x12,0x10,0x59,0x27,0x80,0xec,0x5f,
0x60,0x51,0x7f,0xa9,0x19,0xb5,0x4a,0x0d,0x2d,0xe5,0x7a,0x9f,0x93,0xc9,0x9c,0xef,
0xa0,0xe0,0x3b,0x4d,0xae,0x2a,0xf5,0xb0,0xc8,0xeb,0xbb,0x3c,0x83,0x53,0x99,0x61,
0x17,0x2b,0x04,0x7e,0xba,0x77,0xd6,0x26,0xe1,0x69,0x14,0x63,0x55,0x21,0x0c,0x7d ]

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
    val = DCR%256
    return "".join([CODES[val][binstr[i:i+8]] for i in range(0,len(binstr),8)]) # Returns DNA Sequence


# Decode DNA Sequence
def decode(DCR,dnastr): # Enter DNA Sequence
    val = DCR%256
    return "".join([DECODES[val][dnastr[i:i+4]] for i in range(0,len(dnastr),4)]) # returns a string of binary numbers

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

def unscramble(k,b): # Key -> binary string, b -> list of integers
    l = len(b)
    ptr1 = 0
    ptr0 = l//32*(k.count('1'))
    n = []
    for i in range(l):
        if k[i%32] == '1':
            n.append(b[ptr1])
            ptr1+=1
        else:
            n.append(b[ptr0])
            ptr0+=1
    return n # -> list of integers

def scramble(k,b):  # Key -> binary string, b -> list of integers
    zero = []
    one = []
    for i in range(len(b)):
        if k[i%32] == '0':
            zero.append(b[i])
        else:
            one.append(b[i])
    return one + zero # -> list of values

def keygen():
    SR = random.getrandbits(32) 
    y1 = random.getrandbits(32) 
    y2 = random.getrandbits(32) 
    y3 = random.getrandbits(32) 
    t1 = "".join(scramble(bin(SR)[2:].zfill(32),bin(y1^y2^y3)[2:].zfill(32))) # IV and for Coding Rule
    t2 = "".join(scramble(bin(y1)[2:].zfill(32),bin(y2^y3^SR)[2:].zfill(32))) # Scramble
    t3 = "".join(scramble(bin(y2)[2:].zfill(32),bin(y1^y3^SR)[2:].zfill(32))) # Key
    t4 = "".join(scramble(bin(y3)[2:].zfill(32),bin(y1^y2^SR)[2:].zfill(32))) # Key
    return [SR,y1,y2,y3],[t1,t2,t3,t4]

def keyretr(ini):
    SR = ini[0]
    y1 = ini[1]
    y2 = ini[2]
    y3 = ini[3]
    t1 = "".join(scramble(bin(SR)[2:].zfill(32),bin(y1^y2^y3)[2:].zfill(32))) # IV and for Coding Rule
    t2 = "".join(scramble(bin(y1)[2:].zfill(32),bin(y2^y3^SR)[2:].zfill(32))) # Scramble
    t3 = "".join(scramble(bin(y2)[2:].zfill(32),bin(y1^y3^SR)[2:].zfill(32))) # Key
    t4 = "".join(scramble(bin(y3)[2:].zfill(32),bin(y1^y2^SR)[2:].zfill(32))) # Key
    return [t1,t2,t3,t4]

def sbox(key,pt):
    words = [pt[i:i+8] for i in range(0,32,8)]
    words = "".join([bin(int(Sbox[int(i,2)]))[2:].zfill(8) for i in words])
    cblock = "".join(['0' if x == y else '1' for x,y in zip(key,words)])
    return cblock

def isbox(key,ct):
    words = "".join(['0' if x == y else '1' for x,y in zip(key,ct)])
    words = [words[i:i+8] for i in range(0,32,8)]
    cblock = "".join([bin(int(InvSbox[int(i,2)]))[2:].zfill(8) for i in words])
    return cblock

def decipherBlock(IV,keys,cblock):
    DCR = int(IV,2)
    k1 = int(keys[0],2)
    k2 = int(keys[1],2)
    k3 = int(keys[2],2)
    # Code with k1
    dna4 = list(code(k1,cblock))

    # Reverse Complement with k3
    if k3%8 < 3:
        for i in range(len(dna4)):
            if i%2 == 0:
                dna4[i] = COMPLEMENT[dna4[i]]
    else:
        for i in range(len(dna4)):
            if i%2 != 0:
                dna4[i] = COMPLEMENT[dna4[i]]

    # Reverse Moore
    dna3 = revMoore(k2,dna4)
    # Reverse DNA Operations
    dnak1 = code(DCR,keys[0])
    dnak2 = code(DCR,keys[1])
    dnak3 = code(DCR,keys[2])
    dna2 = [dna_xor[i][j] for i,j in zip(dna3,dnak3)]
    dna1 = [dna_add[i][j] for i,j in zip(dna2,dnak2)]
    bdna = [dna_sub[i][j] for i,j in zip(dna1,dnak1)]
    bdna = "".join(bdna)
    cblock = decode(DCR,bdna)

    # Using k2 pass it through inverse SBox
    cblock = isbox(keys[1],cblock)
    # Using k3 unscramble the cblock
    cblock = "".join(unscramble(keys[2],cblock))
    # IV xor cblock = block
    block = "".join(['0' if x == y else '1' for x,y in zip(IV,cblock)])
    return block

def encipherBlock(IV,keys,block): # 32 bits
    # IV xor Block
    cblock = "".join(['0' if x == y else '1' for x,y in zip(IV,block)])
    # Using k3 scramble each cblock
    cblock = "".join(scramble(keys[2],cblock))
    # Using k2 pass it through  SBox
    cblock = sbox(keys[1],cblock)

    # DNA Operations Begin
    DCR = int(IV,2)
    k1 = int(keys[0],2)
    k2 = int(keys[1],2)
    k3 = int(keys[2],2)
    cblock = code(DCR,cblock)
    dnak1 = code(DCR,keys[0])
    dnak2 = code(DCR,keys[1])
    dnak3 = code(DCR,keys[2])
    # ADD dna , dnaX2
    dna1 = [dna_add[i][j] for i,j in zip(cblock,dnak1)]
    # SUBTRACT dna1 , dnaX3
    dna2 = [dna_sub[i][j] for i,j in zip(dna1,dnak2)]
    # XOR dna2 , dnaX4
    dna3 = [dna_xor[i][j] for i,j in zip(dna2,dnak3)]
    # Moore Machine using k2
    dna4 = moore(k2,dna3)

    # If k3%8 < 3 complement even indexes, else complement odd indexes
    if k3%8 < 3:
        for i in range(len(dna4)):
            if i%2 == 0:
                dna4[i] = COMPLEMENT[dna4[i]]
    else:
        for i in range(len(dna4)):
            if i%2 != 0:
                dna4[i] = COMPLEMENT[dna4[i]]

    # Decode the cblock with k1 and return it.
    cblock = decode(k1,"".join(dna4))
    return cblock

def makeimg(img,tshape,out="imgsave.png"): # List of Integers
    pixels = [int(img[i:i+8],2) for i in range(0,len(img),8)]
    img = np.array(pixels)
    img = np.reshape(img,tshape)
    image = Image.fromarray(img.astype(np.uint8))
    image.save(out,bitmap_format='png')
    return img

def encrypt(keys,image,out=None):
    # Get the Keys
    IV = keys[0]
    k1 = keys[1]
    k2 = keys[2]
    k3 = keys[3]
    img = np.array(Image.open(image))
    if img.shape[-1] != 4:
        img = np.dstack((img, np.ones(img.shape[:-1])*255)).astype(np.uint8)
    tshape = img.shape
    img = img.flatten()

    # Make it a binary string and scramble it.
    img = binstr(img)
    img = "".join(scramble(k1,img))
    
    # Get the length of the binary string
    l = len(img)
    
    # Block Operation
    blocks = [img[i:i+32] for i in range(0,l,32)]
    print("No of blocks (Encryption): ", len(blocks))
    cblocks = []
    IV = keys[0]
    for block in blocks:
        cblock = encipherBlock(IV,[k1,k2,k3],block)
        IV = cblock
        cblocks.append(cblock)
    
    # Converge all blocks and get final binary to convert into image
    cimg = "".join(cblocks)
    cimg = "".join(scramble(k3,cimg))
    if out is None:
        out = f"{''.join(image.split('.')[:-1])}.enc.png"
    makeimg(cimg,tshape,out)

def decrypt(keys,image,out="retr.png"): # add paramns ,shape,csp
    # Get the keys
    IV = keys[0]
    k1 = keys[1]
    k2 = keys[2]
    k3 = keys[3]

    # Open Encrypted Image
    img = np.array(Image.open(image))
    tshape = img.shape
    img = img.flatten()
    img = binstr(img)
    l = len(img)
    
    # Unscramble using k1
    img = "".join(unscramble(k3,img))
    # Block Operations
    cblocks = [img[i:i+32] for i in range(0,l,32)]
    print("No of blocks (Decryption): ", len(cblocks))
    blocks = []
    for cblock in cblocks:
        blocks.append(decipherBlock(IV,[k1,k2,k3],cblock))
        IV = cblock
    
    # Convert it into binary string
    pimg = "".join(blocks)
    
    # Unscramble using k1
    pimg = "".join(unscramble(k1,pimg))
    
    # Retrieve final image
    return makeimg(pimg,tshape,out)

def imgenc(imfile,outfile=None):
    ini,keys = keygen()
    encrypt(keys,imfile,outfile)
    return ini

def imgdec(ini,imfile,out="retr.png"):
    keys = keyretr(ini)
    return decrypt(keys,imfile,out)