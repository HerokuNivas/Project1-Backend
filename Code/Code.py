from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from gensim.parsing.preprocessing import remove_stopwords
import os
from github import Github
import re


class IR:
    ps = PorterStemmer()
    def BSBI(apiKey, repository, fileName):
        try:
            g = Github(apiKey)

            repository = g.get_repo(repository)

            files = repository.get_contents("")
        except:
            return "An exception occurred in authorising API"

        wordsUnique = set()


        for file in files:
            if file.content == None:
                continue

            else:
                listSeperate = file.decoded_content.decode()
                listSeperate = listSeperate.split('\n')
                for items in listSeperate:
                    items = remove_stopwords(items)
                    currItem = items.split(' ')
                    for word in currItem:
                        word = re.sub(r'[^\w\s]', '', word)
                        if len(word) > 0:
                            wordsUnique.add(word)
                            
        dictStore = {}

        for index, file in enumerate(files):
            if file.content == None:
                continue
            else:
                listSeperate = file.decoded_content.decode()
                listSeperate = listSeperate.split('\n')
                for items in listSeperate:
                    items = remove_stopwords(items)
                    currItem = items.split(' ')
                    for word in currItem:
                        word = re.sub(r'[^\w\s]', '', word)
                        if word.lower() in wordsUnique:
                            if word.lower() not in dictStore:
                                dictStore[word.lower()] = set()
                            dictStore[word.lower()].add(index+1)



        contentIs = ""

        for keyVal in dictStore:
            contentIs += keyVal
            contentIs += "   "
            for element in dictStore[keyVal]:
                contentIs += str(element) + " "
            contentIs += "\n"

        contentIs = contentIs.encode('utf-8')
        try:
            repository.create_file(f"{fileName}.txt", "Merged file", contentIs)
            
        except:
            return "File with specified name already exists!"
        
        return "Success"


                    
