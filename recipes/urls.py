from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path
from .views import recipe_list, recipe_create

urlpatterns += [
    path('web/', recipe_list, name='recipe_list'),
    path('web/add/', recipe_create, name='recipe_create'),
]
