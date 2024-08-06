from django.http import HttpResponse


def card(request):
    return HttpResponse("<h1> Визитка 1</h1>")

def work(request, name, time):
    return HttpResponse(f"""
    <h1>Место работы</h1>
    <p>Название: {name}</p>
    <p>Стаж: {time}</p>
""")