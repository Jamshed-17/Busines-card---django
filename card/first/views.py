from django.http import HttpResponse


def card(request):
    return HttpResponse("<h1>Визитка 1")