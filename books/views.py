from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from django.shortcuts import redirect

# Create your views here.
def main(request):
    books = Book.objects.all()
    context={'books':books}
    return render(request,'main.html',context)

def newBook(request):
    if request.method=='POST':
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        new_book = Book(nombre=nombre, descripcion=descripcion)
        new_book.save()

    return redirect(request.META['HTTP_REFERER'])
