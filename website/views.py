from django.shortcuts import render
from .models import Videos,Comments
# Create your views here.
def index(request):
    try:
        __context = {}
        __context['videos'] = Videos.objects.filter(is_active=True).order_by("-id")
        return render(request, 'youtube.html',__context)
    except Exception as error:
        return render(request, 'error.html',{"error":error})
    
    
def playVideo(request,id):
    try:
        __context = {}
        
        videos = Videos.objects.filter(is_active=True)
        __context['videos'] = videos.exclude(id=id)

        video = videos.get(id=id)
        __context['video'] = video
        if request.method == "POST":
            Comments.objects.create(video_id=id,
                                    comments=request.POST['comments'])

        __context['comments'] = Comments.objects.filter(video__id=id)
        return render(request, 'video.html',__context)
    except Exception as error:
        print(error)
        return render(request, 'error.html',{"error":error})