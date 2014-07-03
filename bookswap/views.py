import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *

def home(request):
    return render_to_response('home.html', locals(),
            context_instance=RequestContext(request))

example_books = [
    {'title': 'Calculus',
     'author': 'James Stewart',
     'edition': 7},
    {'title': 'Multivariable Calculus',
     'author': 'C. Henry Edwards, David E. Penney',
     'edition': 6},
    {'title': 'University Physics with Modern Physics',
     'author': 'Hugh D. Young, et al',
     'edition': 12},
    {'title': 'Campbell Biology',
     'author': 'Jane B. Reece, et al',
     'edition': 9},
    {'title': 'Biology for Dummies',
     'author': 'Rene F. Kratz, et al',
     'edition': 2},
]

def book_search(request):
    query = request.GET.get('query').lower()
    print query
    book_results = filter(lambda book: query in book['title'].lower() or query in book['author'].lower(), example_books)
    return HttpResponse(json.dumps(book_results), content_type='application/json')

