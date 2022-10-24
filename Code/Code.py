from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from gensim.parsing.preprocessing import remove_stopwords
import os
from github import Github
import re


class IR:
    ps = PorterStemmer()
    def BSBI(apiKey, userName, repoName, fileName):
        try:
            g = Github(apiKey)
        except:
            return "An exception occurred in authorising API"
        
        try:
            repository = g.get_repo(userName+"/"+repoName)

            files = repository.get_contents("")
        except:
            return "Wrong repo name entered. Check your username and reponame."

        if fileName == None:
            fileName = "InvertedIndex"
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
                            dictStore[word.lower()].add(file.name)



        contentIs = ""

        for keyVal in dictStore:
            contentIs += keyVal
            contentIs += "   "
            for element in dictStore[keyVal]:
                contentIs += str(element) + " "
            contentIs += "\n"

        contentIs = contentIs.encode('utf-8')
        try:
            repository.create_file(f"{fileName}.txt", "Generated Inverted Index File", contentIs)
            
        except:
            return "File with specified name already exists!"
        
        return "Success"


                    
