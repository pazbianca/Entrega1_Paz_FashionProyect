from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio),
    path('fashionIcons', views.fashionIconsList, name = 'fashionIcons'),
    path('fashionBrands', views.fashionBrandsList, name = 'fashionBrands'),
    path('fashionShows', views.fashionShowsList, name = 'fashionShows'),
    path('form_fashionIcons', views.form_fashionIcons),
    path('form_fashionBrands', views.form_fashionBrands, name = 'formFashionBrands'),
    path('form_fashionShows', views.form_fashionShows),
    path('form_fashionShows', views.form_fashionShows),
    path('search_fashionIcons', views.search_fashionIcons,  name = 'searchFashionIcons'),
    path('searchResults_fashionIcons', views.searchResults_fashionIcons),

   


]
