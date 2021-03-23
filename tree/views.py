from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import File
from .forms import FileForm

def index_view(request):
    files = File.objects.all()
    if request.method == 'POST':
            form = FileForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                new_file = File.objects.create(
                    name=data['name'],
                    parent=data['parent'],
                )
                return HttpResponseRedirect(reverse('homepage'))

    form = FileForm()
    return render(request, 'index.html', {
        'heading': 'Files & Folders',
        'files': files,
        'form': form,
    })

# def add_file(request):
#     if request.method == 'POST':
#         form = FileForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             new_file = File.objects.create(
#                 name=data['name'],
#                 parent=data['parent'],
#             )
#             return HttpResponseRedirect(reverse('homepage'))

#     form = FileForm()
#     return render(request, 'index.html', {
#         'form': form,
#     })
