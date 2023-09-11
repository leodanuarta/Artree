from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
    'nama' : 'hello world from halaman_awal'
    }
    return render(request, 'index.html', context)