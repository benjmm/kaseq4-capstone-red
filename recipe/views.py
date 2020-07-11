from django.shortcuts import render
from recipe.models import Recipe

# Create your views here.
def recpie(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_all.html', {'recipes': recipes})