from django.http import JsonResponse
from Code import Code

def HomeRoute(request):
    apiKey = request.GET.get('apikey')
    userName = request.GET.get('userName')
    repoName = request.GET.get('repoName')
    fileName = request.GET.get('fileName')
    message = Code.IR.BSBI(apiKey,userName,repoName, fileName)
    successCode = False
    if message != "Success":
        successCode = False
    else:
        successCode = True
    dictIs = {'successCode': successCode, 'text': message}
    return JsonResponse(dictIs, safe=False)