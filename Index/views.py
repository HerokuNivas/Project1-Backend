from django.http import JsonResponse
from Code import Code
from Code import Search
from Code import Database

def HomeRoute(request):
    apiKey = request.GET.get('apikey')
    userName = request.GET.get('userName')
    repoName = request.GET.get('repoName')
    fileName = request.GET.get('fileName')
    type = request.GET.get('type')
    message = Code.IR.BSBI(apiKey,userName,repoName, fileName, type)
    successCode = False
    if message != "Success":
        successCode = False
    else:
        successCode = True
    dictIs = {'successCode': successCode, 'text': message}
    return JsonResponse(dictIs, safe=False)


def SearchRoute(request):
    link = request.GET.get('link')
    word = request.GET.get('word')
    apiKey = request.GET.get('apiKey')
    word = word.lower()
    result = Search.Search.Search(link, word, apiKey)
    return JsonResponse({"Files": result[0], "Success" : result[1], "User": result[2], "Repo": result[3]}, safe=False)

def DataRoute(request):
    email = request.GET.get('email')
    update = request.GET.get('update')
    result = Database.Database.Database(email, update)
    return JsonResponse({"Success": result[0]})