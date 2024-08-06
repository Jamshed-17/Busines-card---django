from django.http import HttpResponse


def card(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path = request.path

    return HttpResponse(f"""
    <p>Host: {host}</p>
    <p>Path: {path}</p>
    <p>User-agent: {user_agent}</p>
""")

def work(request, name, time):
    return HttpResponse(f"""
    <h1>Место работы</h1>
    <p>Название: {name}</p>
    <p>Стаж: {time}</p>
""")

def HR(requst):
    return HttpResponse("Hello world", headers={"Date": "Sun, 06 Aug 2024 04:33:08"})

def Eror(request):
    return HttpResponse("Eror", status=435, reason="incorrect data")

def Type(request):
    return HttpResponse("<h1>Hi!<h1>", content_type="text/plain", charset="utf-8")

def user(request, name="Undefined", age=0):
    return HttpResponse(f"<h2>Имя: {name} Возраст: {age}<h2>")