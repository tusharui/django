from django.http import HttpResponse


def home(request):
    return HttpResponse(' <h1>hello world</h1> ')