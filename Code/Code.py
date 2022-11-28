from nltk.tokenize import word_tokenize
from gensim.parsing.preprocessing import remove_stopwords
from github import Github
from nltk.stem import WordNetLemmatizer
import re
import nltk

nltk.download('omw-1.4')
nltk.download('wordnet')


class IR:
    lemmatizer = WordNetLemmatizer()
    def BSBI(apiKey, userName, repoName, fileName, type):
        try:
            g = Github(apiKey)
        except:
            return "An exception occurred in authorising API"
        
        try:
            repository = g.get_repo(userName+"/"+repoName)

            files = repository.get_contents("")
        except:
            return "Check the details which you entered."

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
                            wordsUnique.add(IR.lemmatizer.lemmatize(word.lower()))
                            
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
                        if IR.lemmatizer.lemmatize(word.lower()) in wordsUnique:
                            if IR.lemmatizer.lemmatize(word.lower()) not in dictStore:
                                dictStore[IR.lemmatizer.lemmatize(word.lower())] = set()
                            if type=='FileName':
                                dictStore[IR.lemmatizer.lemmatize(word.lower())].add(file.name.replace(".txt", ""))
                            else:
                                dictStore[IR.lemmatizer.lemmatize(word.lower())].add(index+1)



        contentIs = ""
        dictStore = dict(sorted(dictStore.items(), key = lambda x : x[0]))
        for keyVal in dictStore:
            contentIs += keyVal
            contentIs += "   "
            dictStore[keyVal] = sorted(dictStore[keyVal])
            for element in dictStore[keyVal]:
                if type=='Index':
                    contentIs += str(element) + " "
                else:
                    contentIs += f"'{str(element)}'"+ " "
            contentIs += "\n"

        contentIs = contentIs.encode('utf-8')
        try:
            repository.create_file(f"{fileName}.txt", "Generated Inverted Index File by Inverted Index Generator", contentIs)
            
        except:
            return "File with specified name already exists in the repository!"
        
        return "Success"


                    
