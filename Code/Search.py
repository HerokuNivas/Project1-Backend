import nltk
nltk.download('omw-1.4')

from github import Github
from nltk.stem import WordNetLemmatizer

class Search:
    
    def Search(link, word):
        successCode = "Success"
        ListFiles = []
        dictIs = {}
        lemmatizer = WordNetLemmatizer()
        link = link.replace("https://github.com/","")
        link = link.replace("/blob/main","")
        g = Github()
        userName, repoName, fileName = link.split("/")
        try:
            repo = g.get_repo(f"{userName}/{repoName}")
            files = repo.get_contents("")
            for file in files:
                ListFiles.append(file.name) 
            file = repo.get_contents(f"{fileName}")
            content = file.decoded_content.decode()
            line = content.split("\n")
            for singleline in line:
                words = singleline.split(" ")
                if lemmatizer.lemmatize(word) in lemmatizer.lemmatize(words[0].lower()):
                    dictIs[words[0]] = []
                    for i in range(1,len(words)):
                        if(words[i].isnumeric()):
                            if(ListFiles[int(words[i])-1] != fileName):
                                dictIs[words[0]].append(ListFiles[int(words[i])-1])
                        else:
                            if(words[i] != fileName):
                                dictIs[words[0]].append(words[i])      
        except:
            successCode = "Failure"                            
        return [dictIs, successCode, userName, repoName]