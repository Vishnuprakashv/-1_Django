from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from .models import Book_store
from django.db.models import Q

# Create your views here.
def home(request):
    books = Book_store.objects.all()
    return render(request,'home/home.html',{'books':books})
def manage_store(request):
    if request.method == "POST":
        book_name = request.POST.get("book_name")
        book_author = request.POST.get("book_author")
        book_category = request.POST.get("book_category")
    
        book_pieces_str = request.POST.get("book_pieces", "")
        book_price_str = request.POST.get("book_price", "")
        if book_pieces_str and book_price_str:
            book_pieces = int(book_pieces_str)
            book_price = int(book_price_str)

            existing_book = Book_store.objects.filter(name=book_name).first()
            if existing_book:
                existing_book.update_book(book_pieces, book_price)
            else:
            # Create a new book
                Book_store.objects.create(
                    name=book_name,
                    author=book_author,
                    category=book_category,
                    pieces=book_pieces,
                    price=book_price,
                    total=book_pieces * book_price
                )
        return redirect('/main/manage_store/')
    return render(request, "home/manage_store.html")
# Function for Display
def display(request):
    books = Book_store.objects.all()
    return render(request,'home/display.html',{'books':books})
# Function for id through Delete data particular
def delete_book(request,id):
    book = get_object_or_404(Book_store, pk=id)
    book.delete()
    return redirect("/main/display/")
#This function update the data
def update_book(request,id):
    book = Book_store.objects.get(pk=id)
    return render(request, "home/update.html" ,{'book':book})
def do_update_book(request, id):
    if request.method == "POST":
        try:
            # Data Fetch
            book_name = request.POST.get("book_name")
            book_author = request.POST.get("book_author")
            book_category = request.POST.get("book_category")
            book_pieces = request.POST.get("book_pieces")
            book_price = request.POST.get("book_price")
            book_total = request.POST.get("book_total")
            # get the book object
            book = get_object_or_404(Book_store, pk=id)
            # update the book object with the new data
            book.name = book_name
            book.author = book_author
            book.category = book_category
            book.pieces = book_pieces
            book.price = book_price
            book.total = book_total
            book.save() #Save Data
            # Redirect to the display page
            return redirect('/main/display/')
        except Exception as e:
            return HttpResponseServerError(f"An error occurred: {e}")
    return HttpResponseServerError("Invalid request method")

# Function for Search
def search(request):
    query = request.GET.get('search', '')
    books = []
    if query:
        books = Book_store.objects.filter(
            Q(name__icontains=query) | Q(author__icontains=query) | Q(id__icontains=query)
        )
    return render(request, 'home/search.html', {'books': books, 'query': query})
