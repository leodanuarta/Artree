from django.shortcuts import render
from .models import aboutus, sliders

# Create your views here.

def index(request):
    about = aboutus.objects.all()[0]
    slider = sliders.objects.all()
    context = {
    # 'nama' : 'hello world from halaman_awal';
        'about' : about,
        'slider' : slider
    }

    return render(request, 'index.html', context)