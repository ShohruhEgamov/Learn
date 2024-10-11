from lib2to3.fixes.fix_input import context
# from msilib.schema import ListView
from django.views.generic import ListView

from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from .models import Blog

# def bloglistview(request):
#     blogs = Blog.objects.all()
#     users = User.objects.all()
#
#     context = {
#         "blogs":blogs,
#         "users":users
#     }
#
#     return render(request, "home.html", context=context)
#
#
# def blogdetailview(request, id):
#     # Bu yerda eski versiyasida
#     # try:
#     #     blog = Blog.objects.get(id=id)
#     #     context = {
#     #         'blog':blog
#     #     }
#     # except Blog.DoesNotExist:
#     #     raise Http404('No blog found')
#
#     # Bu yerda yangi versiyasi
#     blog = get_object_or_404(Blog,id=id)
#     context = {
#         "blog" : blog
#     }
#     return render(request, "blog_detail.html",context=context)


# Bu yerda esa CLASS lardan foydalanib yozamiz

class BlogListView(ListView):
    model = Blog
    template_name = 'home.html'
    context_object_name = "blogs"


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog_detail.html"