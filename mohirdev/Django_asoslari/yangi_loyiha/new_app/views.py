from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView,ListView
from matplotlib.style.core import context

from .models import News, Category
from .forms  import ContactForm

def new_list(request):
    new_list = News.published.all()
    context = {
        'new_list': new_list
    }
    return render(request, 'news/new_list.html', context)

def new_detail(request, id):
    news = get_object_or_404(News, pk=id, status=News.Status.PUBLISHED)
    context = {
        'news': news
    }
    return render(request, 'news/new_detail_page.html', context)


def homePageViev(request):
    categories = Category.objects.all()
    news_list = News.published.all().order_by('-publish_time')[:10]
    local_one = News.published.filter(category__name='Mahalliy').order_by('-publish_time')[:1]
    local_list = News.published.all().filter(category__name='Mahalliy').order_by('-publish_time')[1:6]

    context = {
        'news_list': news_list,
        'categories': categories,
        'local_one': local_one,
        'local_list': local_list
    }
    return render(request, 'news/home.html', context)

class HomePageView(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news'

    def get_context_data(self, ** kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')[:10]
        context['local_one'] = News.published.filter(category__name='Mahalliy').order_by('-publish_time')[:1]
        context['local_list'] = News.published.all().filter(category__name='Mahalliy').order_by('-publish_time')[1:6]
        return context


# def contactPageView(request):
#     form = ContactForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return HttpResponse("<h1> Biz bilan bog'langaningiz uchun raxmat</h1>")
#     context = {
#         'form': form
#     }
#     return  render(request, 'news/contact.html', context)


def XatolikPageView(request):
    context = {}
    return  render(request, 'news/404.html', context)


# Class yordamida qilish

class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self,request, *args, **kwargs): # Malumot yuborish
        form = ContactForm()
        context = {
            'form': form
        }

        return render(request, 'news/contact.html', context)
    def post(self, request, *args, **kwargs): # Malumot olish
        form = ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            return HttpResponse("<h1> Biz bilan bog'langaningiz uchun raxmat</h1>")
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)