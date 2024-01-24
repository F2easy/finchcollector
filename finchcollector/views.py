from django.shortcuts import render

from .models import Finch



def home(request):

    # unlike with ejs, we need our .html file extension
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# index view - shows all the finces at '/finches'
def finches_index(request):
  # collect our objects from the database
  finches = Finch.objects.all()
  # just like in ejs, we can pass some data to our views

  ## for finch in finches:
   ## print(finch)
  return render(request, 'finches/index.html', { 'finches': finches })

# detail view - shows one finch at ' /finches/:id'

def finches_detail(request):
  finches = Finch.objects.get(id=finch_id)

  return render(request, 'finchess/detail.html', { 'finches': finches })