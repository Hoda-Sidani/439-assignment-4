from django.urls import path
from .views import create_contact, contact_list, update_contact, delete_contact, recommend_doctors  # Add recommend_doctors here

urlpatterns = [
    path('', contact_list, name='contact_list'),  # List contacts (READ)
    path('create/', create_contact, name='create_contact'),  # Create contact
    path('update/<int:id>/', update_contact, name='update_contact'),  # Update contact
    path('delete/<int:id>/', delete_contact, name='delete_contact'),  # Delete contact
    path('recommend_doctors/', recommend_doctors, name='recommend_doctors')  # Recommendation system
]
