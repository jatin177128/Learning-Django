from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("hello , this is home ")
    return render(request,'website/index.html')
def about(request):
    return HttpResponse("hello , this is about ")
def contact(request):
    return HttpResponse("hello , this is contact ")
