from django.urls import path
from . import views
app_name = 'pages'
urlpatterns = [
    path('',views.index, name='index'),
    path('about', views.about, name='about')
]
# '' empty string so name = index, if 'about', name = 'about'(end point)
# index and about are end point