# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 11:37:39 2019

@author: Mikef
"""
import hashlib


# My code
def fileStorage(fileName):
    file = open(fileName, 'r')
    lines = file.readlines()
    users = []
    for line in lines:
        users.append(line.strip())
    return users

def generatePasswords(str, low, high, list):
    if high < low:
        temp = high
        high = low
        low = temp
    if len(str) > high:
        return
    if len(str) >= low:
        checkPasswords(str, list)
    generatePasswords(str + '0', low, high, list)
    generatePasswords(str + '1', low, high, list)
    generatePasswords(str + '2', low, high, list)
    generatePasswords(str + '3', low, high, list)
    generatePasswords(str + '4', low, high, list)
    generatePasswords(str + '5', low, high, list)
    generatePasswords(str + '6', low, high, list)
    generatePasswords(str + '7', low, high, list)
    generatePasswords(str + '8', low, high, list)
    generatePasswords(str + '9', low, high, list)


def checkPasswords(password, list):

    for line in list:
        pieces = line.split(',')

        if str(pieces[2]) == str(hash_with_sha256(password + pieces[1])):
            print(pieces[0] + ': ' + password)
            list.remove(line)


# code provided

def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def main():
    # hex_dig = hash_with_sha256('This is how you hash a string with sha256')
    # print(hex_dig)
    # generatePasswords('', int(input('What is the shortest a password can be?(Number of characters)\n')), int(input('What is the longest a password can be?(Number of characters)\n')))
    generatePasswords('', 7, 3, fileStorage("password_file.txt"))


# fileName = input('What is the file\'s name? (include ".txt" at the end)\n')

main()
