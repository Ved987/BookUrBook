from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from home.utils import get_db_handle,get_collection_handle

# Create your views here.

def home_view(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())  

db_handle, client = get_db_handle()
collection_handle = get_collection_handle(db_handle, 'Inventory')

def browse_view(request):
    template = loader.get_template('Browse.html')
    document_to_find = {"Category": "Fantasy"}
    Fantasy = collection_handle.find(document_to_find)
    document_to_find = {"Category" : "Sci-Fi"}
    Sci_fi = collection_handle.find(document_to_find)
    document_to_find = {"Category" : "Mystery"}
    Mystery = collection_handle.find(document_to_find)
    document_to_find = {"Category" : "Thriller"}
    Thriller = collection_handle.find(document_to_find)
    document_to_find = {"Category" : "Romance"}
    Romance = collection_handle.find(document_to_find)
    context = {'Fantasy' : Fantasy,
               'SciFi' : Sci_fi,
               'Mystery' : Mystery,
               'Thriller' : Thriller,
               'Romance' : Romance}
    return HttpResponse(template.render(context, request))


