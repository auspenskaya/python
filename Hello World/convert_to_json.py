'''
Created on 10 dec. 2014.

@author: Ann ......
'''
if __name__ == '__main__':
    import os
    import json
    import ast
    import unicodedata
    import chardet
    directory = 'C:/Python27/text_documents'
    files = os.listdir(directory)
    json_files = filter(lambda x: x.endswith('.txt'), files)
    for i in json_files:
        with open('C:/Python27/text_documents/'+i) as file:
            a = file.readline()
            file.close()
            file = open('C:/Python27/text_documents/'+i+'.json', 'w')        
            enc = chardet.detect(a)
            if enc['encoding']== 'MacCyrillic':
                a = unicode(a.decode('Windows-1251'))           
                file.write('{"data":{"text":"'.encode('utf-8')+a.encode('utf-8')+'",}}'.encode('utf-8'))
            else:
                file.write('{"data":{"text":"'.encode('utf-8')+a+'",}}'.encode('utf-8'))
        
        
