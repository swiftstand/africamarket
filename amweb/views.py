from django.shortcuts import render,get_object_or_404
from .models import AdminPost
from users.models import SellerProfile
from inventory.models import ShelfOne
from django.views.generic import ListView, DetailView, CreateView
from django.utils import timezone
from datetime import timedelta
from users.views import postpick,postsize
# Create your views here.

def home(request):
    context={
        'latestposts':postpick(),
        'postsize':postsize(),
        'shelf': ShelfOne.objects.all()
        }
    return render(request, 'amweb/index.html',context)

class AdminPostListView(ListView):
    model = AdminPost
    template_name = 'amweb/adminpost.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class AdminPostDetailView(DetailView):
    model = AdminPost
    query_pk_and_slug = False


def accounts(request):
    return render(request, 'amweb/my-accounts.html')

def about(request):
    return render(request, 'amweb/about.html')

def service(request):
    return render (request, 'amweb/service.html')

def cart(request):
    return render(request, 'amweb/cart.html')

def checkout(request):
    return render(request, 'amweb/checkout.html')

def wishlist(request):
    return render(request, 'amweb/wishlist.html')

def contactus(request):
    return render(request, 'amweb/contact-us.html')
