from django.contrib import admin
from django.urls import path
from Movieapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-movie/', views.add_movie)
]
