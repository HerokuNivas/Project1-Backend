from github import Github

class Check:
    def Check(apiKey, userName, repoName):
        g = Github(apiKey)
        listIs = []
        try:
            repository = g.get_repo(userName+"/"+repoName)
            files = repository.get_contents("")
        except:
            return [listIs]

        
        for file in files:
            if "-InvertedIndex" in file.name:
                listIs.append(file.name)
            
        return [listIs]    
        