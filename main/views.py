from django.shortcuts import render
from django.core.paginator import Paginator

from .models import User, Page


def index(request):
    users = User.objects.all()
    page_num = request.GET.get('page')
    if request.method == 'POST':
        pages = request.POST['paginat']
        page = Page.objects.create(page=pages)
        paginator = Paginator(users, page.page)
        users = paginator.get_page(page_num)
        return render(request, 'index.html', {'users': users})
    try:
        page = Page.objects.last()
        paginator = Paginator(users, page.page)
    except:
        paginator = Paginator(users, 4)
    users = paginator.get_page(page_num)
    return render(request, 'index.html', {'users': users})
