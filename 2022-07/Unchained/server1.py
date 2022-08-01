from django.shortcuts import render
from django.http import HttpResponse, FileResponse

from requests import get

# at /
def index(request):
    return HttpResponse(open(__file__, 'r').read(), content_type='text/plain')

# at /flag
def flag(request):
    user = request.GET.get('user', '')
    if user == 'admin':
        return HttpResponse("Hey, no impersonating admin!")
    url = request.build_absolute_uri().replace(request.build_absolute_uri('/'), '')
    r = get('http://0.0.0.0:1337/'+url)
    return HttpResponse(r.content)

# definitely not at /nothing_important_dont_look_here
def nothing_important_dont_look_here(request):
    return HttpResponse(get('http://0.0.0.0:1337').content, content_type='text/plain')

