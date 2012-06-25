#!/usr/bin/python3
#Written by Chris Rogers, 2012
#Take it and run!
#Requires BeautifulSoup to be installed


import os, codecs, re

from bs4 import BeautifulSoup

def main():
    pattern = re.compile("file_.*") #THIS IS YOUR ID PATTERN
    listing = os.listdir() #WORKS FOR ANY .HTML FILES IN ROOT DIR
    for item in listing:
        ext = os.path.splitext(item)[1]
        if ext == ('.html'): #CHANGE TO .XHTML AS NECESSARY
            desired_tags = []
            new_soup = load_file(item)
            result = new_soup.findAll('p')
            for tag in result:
                str_tag=str(tag)
                searcher = re.search(pattern, str_tag)
                if searcher:
                    desired_tags.append(tag) #SAVES DESIRED ELEMENTS TO A LIST
                    
                    #### Insert processing here. You could save to another file?  #####
                    
            print(desired_tags,"\n")
            
            
def load_file(file_loc):
    a_content_file = codecs.open(file_loc, mode='r', encoding = 'UTF-8')
    text = a_content_file.read()
    a_content_file.close()
    output = BeautifulSoup(''.join(text))
    return output

if __name__ == "__main__": main()