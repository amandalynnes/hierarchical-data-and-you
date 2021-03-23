from django.shortcuts import render
from .models import File

def index_view(request):
    files = File.objects.all()
    return render(request, 'index.html', {
        'heading': 'Files',
        'files': files
    })