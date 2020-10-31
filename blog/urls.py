from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.get_post),
    path('<int:year>/<int:month>/<int:day>/<slug:slug_post>/', views.get_post_detail, name='detail'),
    path('<slug:slug_post>/share/', views.emailForm, name='email'),
]