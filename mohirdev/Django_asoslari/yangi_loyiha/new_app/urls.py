from django.urls import path
from .views import new_list, new_detail

urlpatterns = [
    path('all/', new_list, name='all_new_list'),
    path('<int:id>/', new_detail, name='new_detail_page'),
]