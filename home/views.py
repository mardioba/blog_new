from django.shortcuts import render, HttpResponse

def index(request):
  # return HttpResponse("Olá amigos ):")
  return render(request, 'index.html')
