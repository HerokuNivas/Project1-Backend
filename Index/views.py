from django.http import JsonResponse
from Code import Code

def HomeRoute(request):
    apiKey = request.GET.get('apikey')
    print("apiKey ", apiKey)
    repoLocation = request.GET.get('location')
    name = request.GET.get('name')
    message = Code.IR.BSBI(apiKey, repoLocation, name)
    successCode = False
    if message != "Success":
        successCode = False
    else:
        successCode = True
    dictIs = {'successCode': successCode, 'text': message}
    return JsonResponse(dictIs)