from django.shortcuts import render
from django.core.paginator import Paginator

from .models import User


def index(request):
    users = User.objects.all()
    page = request.GET.get('page')
    if request.method == 'POST':
        pages = request.POST['paginat']
    if pages is None:
        paginator = Paginator(users, 4)
    else:
        paginator = Paginator(users, pages)
    users = paginator.get_page(page)
    return render(request, 'index.html', {'users': users})
