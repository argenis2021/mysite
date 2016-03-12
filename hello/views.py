from django.http import HttpResponse
def hello(request):
 return HttpResponse("Hello, world.")
def current_datetime(request):
 now=datetime.datetime.now()
 html="it is now %s." %now
 return HttpResponse(html)
