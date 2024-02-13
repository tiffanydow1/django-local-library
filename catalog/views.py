from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

def index(request):
  """View function for home page of site."""

  # Generate counts of some of the main objects
  num_books = Book.objects.all().count()
  num_instances = BookInstance.objects.all().count()

  # Available books (status = 'a')
  num_instances_available = BookInstance.objects.filter(status__exact='a').count()

  # Number of books that fall into the magical realism genre
  magic_genre_count = Book.objects.filter(genre__name__icontains='magic').distinct().count()

  # The 'all()' is implied by default
  num_authors = Author.objects.count()

  context = {
    'num_books': num_books,
    'num_instances': num_instances,
    'num_instances_available': num_instances_available,
    'magic_genre_count': magic_genre_count,
    'num_authors': num_authors,
  }

  # Render the HTML template index.html with the data in the context variable
  return render(request, 'index.html', context=context)
