from rest_framework import viewsets
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm
from .serializers import RecipeSerializer

# ✅ 1. API ViewSet (for /api/recipes/)
'''class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('-id') # ⛔ This shows latest first
    serializer_class = RecipeSerializer
'''
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('id')  # ✅ Shows recipes starting from ID 1
    serializer_class = RecipeSerializer
'''
# ✅ 2. Frontend View with Pagination (for /api/web/)
def recipe_list(request):
    recipe_list = Recipe.objects.all().order_by('-id')  # ⛔ Latest first
    paginator = Paginator(recipe_list, 10)  # Show 10 recipes per page
'''
def recipe_list(request):
    recipe_list = Recipe.objects.all().order_by('id')  # ✅ Show from ID 1
    paginator = Paginator(recipe_list, 10)
    page_number = request.GET.get('page')
    recipes = paginator.get_page(page_number)
    return render(request, 'recipe_list.html', {'recipes': recipes})

# ✅ 3. Frontend View to Add a New Recipe (for /api/web/add/)
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipe_form.html', {'form': form})
