from django.urls import path
from .views import *

urlpatterns = [
    path('', landing_view, name="landing"),
    # path('home/', home_view, name='home'),

    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('pets/', pets_view, name='pets'),
    path('pets/add-pet', add_pet_view, name='add-pet'),
    path('pets/edit-pet/<int:pet_id>/', edit_pet_view, name='edit-pet'),
    path('pets/delete-pet/<int:pet_id>/', delete_pet_view, name='delete_pet'),
    path('vet-visits/', vet_visits_view, name='vet-visits'),
    path('vet-visits/add-visit', vet_visit_add_view, name='add-visit'),

    # path('search/', search_view, name='search'),
]