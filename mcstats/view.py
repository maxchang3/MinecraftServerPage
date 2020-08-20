from django.http import HttpResponse
import mygetter

def hello(request):
    ip  = request.GET.get("ip")
    title = request.GET.get("title")
    motd = request.GET.get("motd")
    image = mygetter.status_get(ip,title,motd)
    return HttpResponse(image,content_type='image/png')