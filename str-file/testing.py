from dna import strenc,strdec
import random
import string
import time

letters = string.printable

tests = []
for i in range(200):
    tmp = {}
    length = random.randint(100,500)
    text = random.choices(letters,k=length)
    random.shuffle(text)
    tmp["len"] = length
    tmp["text"] = text
    tic = time.time()
    ct,DCR,ini = strenc(text)
    toc = time.time()
    retr = strdec(ct,DCR,ini)
    tictoc = time.time()
    passed = "False"
    if retr == text:
        passed = "True"
    enctime = toc-tic
    tmp["enctime"] = enctime
    tmp["dectime"] = tictoc-toc
    tmp["throughput"] = length/enctime
    tmp["passed"] = passed