from . import views
from django.urls import path


urlpatterns = [
    path('publishers/', views.publishers),
    path('locations/', views.locations),
]