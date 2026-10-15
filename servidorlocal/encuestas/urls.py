from django.urls import path
from.import views


urlpatterns = [
    path('', views.index, name='index'),

    path("musico/", views.musico, name="musico"),

    path('profesor/', views.profesor_view, name='profesor')

]
