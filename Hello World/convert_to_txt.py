'''
Created on 10 dec. 2014.

@author: Ann
'''
if __name__ == '__main__':
    import os
    import json
    import ast
    import unicodedata
    directory = 'C:/Python27/json'
    files = os.listdir(directory)
    json_files = filter(lambda x: x.endswith('.json'), files)
    for i in json_files:
        file = open('C:/Python27/json/'+i, 'r')
        a = file.read()
        file.close()
        d = json.loads(a)
        text = d['data']
        text = text['text']
        print type(text)
        file = open('C:/Python27/json/'+i+'.txt', 'w')
        file.write(text.encode('utf-8'))
        file.close()
        
