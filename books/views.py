from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Book
from .forms import BookForm
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# List View
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


# Create View
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book created successfully!")
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

# Update View
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully!")
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})

# Delete View
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, "Book deleted successfully!")
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})

from django.shortcuts import render, redirect
from .forms import BookForm

def book_form(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect('success_url')  # Redirect to a success page after saving
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})
