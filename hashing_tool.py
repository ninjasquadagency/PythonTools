import hashlib
import colorama
from hashlib import *
colorama.init(autoreset=True)
style = """\033[31m
  ____  _            _    _    _                  _______          _ 
 |  _ \| |          | |  | |  | |                |__   __|        | |
 | |_) | | __ _  ___| | _| |__| | ___  _ __ ___  ___| | ___   ___ | |
 |  _ <| |/ _` |/ __| |/ /  __  |/ _ \| '__/ __|/ _ \ |/ _ \ / _ \| |
 | |_) | | (_| | (__|   <| |  | | (_) | |  \__ \  __/ | (_) | (_) | |
 |____/|_|\__,_|\___|_|\_\_|  |_|\___/|_|  |___/\___|_|\___/ \___/|_|
   v1.1                                         Hashing Tool \033[35mBy:@ Marouan Anouar                     
"""
print(style)
print("\033[35m################################################")
print("\033[33m1]- Hash Chacker\n2]- Hash length\n3]- hash type")
print("\033[33m4]- MD5 Encrypt\n5]- MD5 Decrypt")
print("\033[35m################################################")

choose = input("Enter Choose Option : ")
if choose == '1':
    print("\033[31m=================================================")
    print("\033[32mThis Option is { Hashing Chacker }")
    print("\033[31m=================================================")  
    hash1 = input("Enter First Hash : ")
    hash2 = input("Enter Second Hash : ")
    if hash1 == hash2:
        print("This Hash Number is Good")
    else:
        print("This Hash is Not Clean Bro")
if choose == '2':
    print("\033[31m=================================================")
    print("\033[32mThis Option is { Hashing Length }")
    print("\033[31m=================================================")    
    length = input("Enter Your Hash Number : ")
    print("Length Hash is : ", len(length))
if choose == '3':
    print("\033[31m=================================================")
    print("\033[32mThis Option is { Hashing type }")
    print("\033[31m=================================================")  
    hash = input("Enter The Hash : ")
    length = len(hash)
    if length == 32 : 
        print("The Hash is [MD5]")
    if length == 40 : 
        print("The Hash is [SHA1]")
    if length == 64 : 
        print("The Hash is [SHA256]")
    if length == 56 : 
        print("The Hash is [SHA224]")
    else:
        print("Error")
if choose == '4':
    print("\033[31m=================================================")
    print("\033[32mThis Option is { MD5 Encrypt }")
    print("\033[31m=================================================") 
    word = input("Enter Your Texe Bro : ")
    md5  = hashlib.md5(word.encode())
    print(md5.hexdigest())
if choose == '5':
    print("\033[31m=================================================")
    print("\033[32mThis Option is { MD5 Decrypt }")
    print("\033[31m=================================================") 
    hash = input("Enter Your Hash : ")
    file = input("Write File Name : ")
    with open (file, mode='r') as f :
        for line in f :
            line = line.strip()
            if md5(line.encode()).hexdigest() == hash:
                print("[+] Target Found :" +line)
            else:
                print("[-] Target Not Found ")
    
    
    
    
    
    
    
    
    
    
    
    
