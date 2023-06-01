from django.urls import path
from . import views

urlpatterns = [
    path('', views.PersonView.as_view(), name='persons'),
    path('person_detail/<int:id>/', views.PersonDetailView.as_view(), name='person_detail'),
    path('person_detail/<int:id>/delete/', views.DeletePersonView.as_view(), name='person_delete'),
    path('person_detail/<int:id>/update/', views.UpdatePersonView.as_view(), name='person_update'),
    path('add-person/', views.CreatePersonView.as_view(), name='create_person'),
    path('search/', views.Search.as_view(), name='search'),
]