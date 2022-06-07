from django.shortcuts import render
from.models import Video
#from django.http import HttpResponse

# Create your views here.
def index(request):
    #return render(request,'index.html')
    video=Video.objects.all()
    return render(request,"index.html",{"video":video})
    