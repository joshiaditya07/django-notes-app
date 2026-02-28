"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), #added a URL pattern for the home view to display the list of notes on the homepage')
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'), #added a URL pattern for the delete_note view to handle note deletion requests
    path('update/<int:note_id>/', views.update_note, name='update_note'), #added a URL pattern for the update_note view to handle note update requests
]
