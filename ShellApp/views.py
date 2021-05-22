from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def index(request):
    all_books = Book.objects.all()
    all_authors = Author.objects.all()
    context ={
        "all_books": all_books,
        "all_authors": all_authors
    }
    return render(request,'index.html',context)

def add_book(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        Book.objects.create(title=title, desc=desc)
    return redirect("/")

def add_author(request):
    if request.method =="POST":
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        Author.objects.create(first_name=f_name,last_name=l_name)
    return redirect("/")

def edit_book(request, book_id):
    edit_book= Book.objects.get(id=book_id)
    authors = Author.objects.exclude(books__id=book_id)
    authors_are = Author.objects.filter(books = edit_book)
    context = {
        "book": edit_book,
        "authors": authors,
        "authors_are": authors_are,
    }
    return render(request,'books.html',context)

def book_to_author(request,book_id):
    if request.method =="POST":
        # edit_book = request.POST['book_id']
        # author_id = ['author_id']
        book = Book.objects.get(id = request.POST['book_id'])
        author =Author.objects.get(id=request.POST['author_id'])
        book.authors.add(author)
    return redirect(f"/books/{book_id}")
        
def author_edit(request, author_id):
    edit_author = Author.objects.get(id=author_id)
    books = Book.objects.exclude(authors__id=author_id)
    books_are = Book.objects.filter(authors = edit_author)
    context = {
        "author" : edit_author,
        "books":books,
        "books_are": books_are,
    }
    return render(request,'authors.html',context)

def author_to_book(request,author_id):
    if request.method=="POST":
        ''' author_id= request.POST['author_id']
        book_id= request.POST['book_id'] '''
        book = Book.objects.get(id=request.POST['book_id'])
        author = Author.objects.get(id=request.POST['author_id'])
        author.books.add(book)
    return redirect(f"/authors/{author_id}")