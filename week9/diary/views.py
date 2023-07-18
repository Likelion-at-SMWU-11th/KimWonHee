from django.shortcuts import render
from django.views.generic import ListView
from .models import Diary

# Create your views here.

def fbv_view(request):
    return render(request, 'introduce.html')

class cbv_view(ListView):
    model = Diary
    template_name = "diary.html"