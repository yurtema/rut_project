from django.shortcuts import render

def index(request):
    return render(request, 'main/index2.html')

def about(request):
    return render(request, 'main/about.html')

def child(request):
    return render(request, 'main/child.html')

def cinema(request):
    return render(request, 'main/cinema.html')

def theatre(request):
    return render(request, 'main/theatre.html')

def exhibition(request):
    return render(request, 'main/exhibition.html')

def concert(request):
    return render(request, 'main/concert.html')

def other(request):
    return render(request, 'main/other.html')

def calendary(request):
    return render(request, 'main/calendary.html')
    
def one(request):
    return render(request, 'main/1.html')