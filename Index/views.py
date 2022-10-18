from django.http import JsonResponse
from Code import Code

def HomeRoute(request):
    message = Code.IR.BSBI("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", "HerokuNivas/InvertedIndex", "nivas")
    successCode = False
    if message != "Success":
        successCode = False
    else:
        successCode = True
    dictIs = {'successCode': successCode, 'text': message}
    return JsonResponse(dictIs)