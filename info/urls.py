from django.urls import path

from .views import list_hotels, get_registration, create_registration, edit_registration, list_nationalities

urlpatterns = [
    path('hotels/', list_hotels, name='hotels'),
    path('nationality/', list_nationalities, name='nationality'),
    path('get-registration/<int:request_id>/', get_registration, name='get-registration'),
    path('create-registration/', create_registration, name='create-registration'),
    path('edit-registration/<int:request_id>/', edit_registration, name='edit-registration'),
]
