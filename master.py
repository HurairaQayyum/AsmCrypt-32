import os
from telnetlib import ENCRYPT
import subprocess
from click import argument
import docx
import re
import art

systemCalls = 0  
numOfNetworkCalls = 0

def find_string(file_name, word):
    
    global systemCalls
    global numOfNetworkCalls
    if word == "socket":
        with open(file_name, 'r') as a:
            for line in a:
                line = line.rstrip()
                if re.search(r"\b{}\b".format(word),line):
                    systemCalls += 1
                    numOfNetworkCalls += 1
    elif word == "write":
        with open(file_name, 'r') as a:
            for line in a:
                line = line.rstrip()
                if re.search(r"\b{}\b".format(word),line):
                    systemCalls += 1
                    

def encrypt():
    st = input("Enter text to print:")
    file = input("Enter file name:")
    cmd = "./encrypt"
    
    subprocess.call([cmd, st, file])
    

def decrypt():
    file = input("Enter file name:")
    cmd = "./decrypt"
    sp = " "
    #cm = cmd + sp + file
    subprocess.call([cmd, file])
    
     
def encryptexisiting():
    file = input("Enter file name to encrypt:")
    if(os.path.exists(file)):
        f = open(file, mode='r', encoding='utf-8')
        data = f.read()
        encryptedFile = input("Enter file name:")
        cmd = "./encrypt"
        subprocess.call([cmd, data, encryptedFile])
        print("File Encrypted Successfully")
    else:
        print("The given file does not exist")

def decryptExisting():
    
    file = input("Enter file name:")
    cmd = "./decrypt"
    sp = " "
    ts = " > "
    txt = ".txt"
    cm = cmd + sp + file
    Nfile = file + txt
    
    out = str(os.system(cm))
    
    #output = .read()
    # newfile = file + ".txt"
    # output = subprocess.run([cm , newfile], stdout=subprocess.DEVNULL,
    # stderr=subprocess.DEVNULL)
    print(out)

def malwareAnalysis():
    # file = input("Enter file name to disassemble for analysis :: ")
    # cmd = "objdump -d "
    # txt = " > file.txt"
    # id = cmd + file + txt 
    # os.system(id)
    
    global systemCalls
    global numOfNetworkCalls
    find_string('file.txt', 'socket')
    find_string('file.txt', 'write')
        
    print("Number of System calls :: {}",systemCalls)
    print("Number of Network calls :: {}",numOfNetworkCalls)     
        

def main():
    art.tprint("Assembly  Project",chr_ignore=True) 
    
    ch = 'y'
    while (ch == 'y'):
        print("1. Create and Encrypt new File\n2. Encrypt Existing File\n3. Derypt the File\n4. Generate Report for any executable file(Analyze the disassembled file)\n")
        choice = int(input("Enter your Choice :: "))
        if(choice == 1):
            encrypt()
        elif(choice == 2):
            encryptexisiting()
        elif(choice == 3):
            decrypt() 
        elif(choice == 4):
            malwareAnalysis()   
        else:
            print("Wrong Choice")      
        ch = input("Do you want to continue (y/n) :: ")        

if __name__ == "__main__":
    main()