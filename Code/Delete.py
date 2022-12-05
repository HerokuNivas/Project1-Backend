from github import Github

class Delete:
    def Delete(apiKey, userName, repoName):
        g = Github(apiKey)
        try:
            repository = g.get_repo(userName+"/"+repoName)
            files = repository.get_contents("")
        except:
            return "Failure"

        
        for file in files:
            if "-InvertedIndex" in file.name:
                contents = repository.get_contents(file.name)
                repository.delete_file(contents.path, "Removed already generated index file", contents.sha)
            
        return "Success"  
        