from django.shortcuts import render, redirect, get_object_or_404

from myapp.forms import BookForm
from myapp.models import Book


# CREATE and LIST
def book_list(request):
    books = Book.objects.all()
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    return render(request, 'myapp/book_list.html', {'books': books, 'form': form})

def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'myapp/book_form.html', {'form': form})

# UPDATE
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'myapp/book_form.html', {'form': form})

# DELETE
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'myapp/book_confirm_delete.html', {'book': book})