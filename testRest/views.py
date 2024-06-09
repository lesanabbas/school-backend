from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def login(request):
    return JsonResponse({"status": True})

def index(request):
    return render(request,'testRest/index.html')
