import nltk
nltk.download('omw-1.4')

from github import Github
from nltk.stem import WordNetLemmatizer

class Search:
    
    def Search(link, word):
        successCode = "Success"
        if("https://github.com/" not in link or "/blob/main" not in link or len(link.split("/"))!=8):
            return [{}, "Failure", "", ""]
        link = link.replace("https://github.com/","")
        link = link.replace("/blob/main","")
        userName, repoName, fileName = link.split("/")
        dictIs = {}
        try:
            ListFiles = []
            lemmatizer = WordNetLemmatizer()
            g = Github()
            repo = g.get_repo(f"{userName}/{repoName}")
            files = repo.get_contents("")
            print(files)
            for file in files:
                if(file.name != fileName):
                    ListFiles.append(file.name)    
            file = repo.get_contents(f"{fileName}")
            content = file.decoded_content.decode()
            line = content.split("\n")
            for singleline in line:
                words = singleline.split(" ")
                if lemmatizer.lemmatize(word) in lemmatizer.lemmatize(words[0].lower()) and words[0]!='':
                    dictIs[words[0]] = []
                    for i in range(3,len(words)-1):
                        if(words[i].isnumeric()):
                            dictIs[words[0]].append(ListFiles[int(words[i])-1])
                        else:
                            dictIs[words[0]].append(words[i])      
        except Exception as e:
            print(e)
            successCode = "Failure"  
        print(dictIs)                              
        return [dictIs, successCode, userName, repoName]