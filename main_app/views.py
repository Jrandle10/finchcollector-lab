from django.shortcuts import render
from django.http import HttpResponse

# Class and List below
class Finch:
  def __init__(self, name, species, description, age):
    self.name = name
    self.species = species
    self.description = description
    self.age = age


finches = [
  Finch('Max', 'Evening Grosbeak', 'Pecks everything.', 3),
  Finch('Kev', 'Pine Grosbeak', 'Beautiful colors', 0),
  Finch('Cay', 'Gray-crowned Rosy-Finch', 'Kind of cool', 4),
  Finch('Ja', 'Black Rosy-Finch', 'Dark colors', 6)
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', { 'finches': finches})




