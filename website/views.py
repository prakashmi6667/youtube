from django.shortcuts import render

# Create your views here.
def index(request):
    try:
        return render(request, 'youtube.html')
    except Exception as error:
        return render(request, 'error.html')
    
    
def playVideo(request):
    try:
        return render(request, 'video.html')
    except Exception as error:
        return render(request, 'error.html')