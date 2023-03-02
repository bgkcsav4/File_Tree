#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def open_next_file(filename: str):

    with open(filename, 'r', encoding='utf8') as f:
        data = f.read().split()
       
    return data[1:], data[0]
    pass          
     

def get_max(a): return (a[1], -ord(a[0]))
def most_frequent_chars(filename: str) -> str:

    list, newfilename = (open_next_file(filename))
    
    while filename != newfilename:
        newlist, newfilename = (open_next_file(newfilename))
        list += newlist
        
    max_len = len(max(list, key=len))    
    string =''
    list = [(x, len(x)) for x in list]

    for each in range(max_len):
        ldict = {}
        for word in list:
          if each < word[1]:
             try: ldict[word[0][each]] += 1
             except: ldict[word[0][each]] = 1
    
        string += max(ldict.items(), key = get_max)[0]

    return ldict

print(most_frequent_chars("test01/A.txt"))


