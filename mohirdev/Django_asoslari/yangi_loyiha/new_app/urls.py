from django.urls import path
from .views import new_list, new_detail,homePageViev,ContactPageView,XatolikPageView
urlpatterns = [
    path("", homePageViev, name="home_page"),
    path('news/', new_list, name='all_new_list'),
    path('news/<int:id>/', new_detail, name='new_detail_page'),
    path('contact/', ContactPageView.as_view(), name='contact-page'),
    path('xatolik/', XatolikPageView, name='xatolik_view'),
]