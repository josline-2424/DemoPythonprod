from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import Bookform


# Create your views here.
def index(request):
    book = Book.objects.all()
    context = {'booklist': book}
    return render(request, 'index.html', context)


def detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, "detail.html", {'book': book})


def add(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        book = Book(name=name, desc=desc, year=year, img=img)
        book.save()

    return render(request, 'add.html')


def update(request, id):
    book = Book.objects.get(id=id)
    form = Bookform(request.POST or None, request.FILES, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'book': book})


def delete(request, id):
    book = id
    if request.method == "POST":
        book = Book.objects.get(id=id)
        book.delete()
        return redirect('/')
    return render(request, 'delete.html', {'book': book})
