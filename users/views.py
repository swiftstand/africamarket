from django.shortcuts import render, redirect
from .forms import BuyerRegisterForm, SellerRegisterForm, UserUpdateForm,SellerProfileUpdateForm,BuyerProfileUpdateForm
from .forms import ShelfFiveUpdateForm,ShelfFourUpdateForm, ShelfThreeUpdateForm, ShelfTwoUpdateForm, ShelfOneUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
from amweb.models import AdminPost
from django.utils import timezone
from inventory.models import (ItemShelfOne,ItemShelfTwo,ItemShelfThree,ItemShelfFour,ItemShelfFive,)
from inventory.views import shelfsize
# Create your views here.

def postpick():
    post_filtered=AdminPost.objects.all().order_by('date_posted')
    latestposts=[]
    i=0
    for post in post_filtered:
        if len(post_filtered)>=6:
            if i<6:
                latestposts.append(post)
                i+=1
        else:
            if i<3:
                latestposts.append(post)
                i+=1
    return latestposts

def postsize():
    post_filtered=AdminPost.objects.all()
    last_post=post_filtered.last()
    if last_post is not None:
        size=int(last_post.id)
        return size
    else:
        return 0



def register_a_buyer(request):
    if request.method=='POST':
        form = BuyerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request, 'A buyer account  was successfully created for {}!,  you can now Login '.format(username))
            return redirect('login_buyer')
    else:
        form = BuyerRegisterForm()
    return render(request, 'amweb/register-buyer.html', {'form':form})


def register_a_seller(request):
    if request.method=='POST':
        form = SellerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'A seller account was successfully created for {}!,  you can now Login, welcome to AfricaMarket'.format(username))
            return redirect('login_seller')
    else:
        form = SellerRegisterForm()
    return render(request, 'amweb/register-seller.html',{'form':form})

@login_required
def seller_profile(request):
    return render(request, 'amweb/seller-profile.html')


@login_required
def buyer_profile(request):
    context={
            'latestposts':postpick()
    }
    return render(request, 'amweb/buyer_profile.html',context)

@login_required
def seller_profile_update(request):
    if request.method== 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        s_form = SellerProfileUpdateForm(request.POST,instance=request.user.sellerprofile)
        if u_form.is_valid() and s_form.is_valid():
            u_form.save()
            s_form.save()
            messages.success(request, 'your account has been successfully updated')
            return redirect('seller-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        s_form = SellerProfileUpdateForm(instance=request.user.sellerprofile)

    context = {
        'u_form': u_form,
        's_form': s_form    }

    return render(request, 'amweb/seller-profile-update.html', context)


@login_required
def buyer_profile_update(request):
    if request.method== 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        b_form = BuyerProfileUpdateForm(request.POST, instance=request.user.buyerprofile)
        if u_form.is_valid and b_form.is_valid:
            u_form.save()
            b_form.save()
            messages.success(request, 'your account has been successfully updated!')
            return redirect('buyer-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        b_form = BuyerProfileUpdateForm(instance=request.user.buyerprofile)
    context = {
        'u_form': u_form,
        'b_form': b_form
}

    return render(request, 'amweb/buyer_profile_update.html', context)

def sizes(modele):
    i=float(modele.shelf_size)
    m=int(i)
    return m

@login_required
def seller_dashboard(request):
    sizeone=int(sizes(request.user.sellerprofile.shelfone))
    context={
            'sizeone':sizeone,
            'latestposts':postpick(),
            'postsize':postsize(),
            'items_one_number':ItemShelfOne.objects.filter(shelf=request.user.sellerprofile.shelfone.pk).count(),
            'shelfonediv':(sizeone//2)+(sizeone//10),
            }
    if request.user.sellerprofile.is_free==False:
        sizetwo=int(sizes(request.user.sellerprofile.shelftwo))
        sizethree=int(sizes(request.user.sellerprofile.shelfthree))
        context['items_two_number']=ItemShelfTwo.objects.filter(shelf=request.user.sellerprofile.shelftwo.pk).count()
        context['items_three_number'] =ItemShelfThree.objects.filter(shelf=request.user.sellerprofile.shelfthree.pk).count()
        context['shelftwodiv']=(sizetwo//2)+(sizetwo//10)
        context['shelfthreediv']=(sizethree//2)+(sizethree//10)
        context['sizetwo']=sizetwo
        context['sizethree']=sizethree
    if request.user.sellerprofile.is_free==False and request.user.sellerprofile.is_diamond==True:
        sizefour=int(sizes(request.user.sellerprofile.shelffour))
        sizefive=int(sizes(request.user.sellerprofile.shelffive))
        context['shelffourdiv']=(sizefour//2)+(sizefour//10)
        context['items_four_number']=ItemShelfFour.objects.filter(shelf=request.user.sellerprofile.shelffour.pk).count()
        context['items_five_number']=ItemShelfFive.objects.filter(shelf=request.user.sellerprofile.shelffive.pk).count()
        context['sizefour']=sizefour
        context['sizefive']=sizefive

    return render(request, 'amweb/seller_dashboard.html',context)

@login_required
def shelfone_update(request):
    if request.method== 'POST':
        s_form = ShelfOneUpdateForm(request.POST, request.FILES, instance=request.user.sellerprofile.shelfone)
        if s_form.is_valid:
            s_form.save()
            shelf_name=s_form.cleaned_data.get('shelf_name')
            messages.success(request, 'shelf {} has been successfully updated!'.format(shelf_name))
            return redirect('seller-dashboard')
    else:
        s_form = ShelfOneUpdateForm(instance=request.user.sellerprofile.shelfone)
    context = {
        's_form': s_form,
}

    return render(request, 'amweb/shelfone_update.html', context)


@login_required
def shelftwo_update(request):
    if request.method== 'POST':
        s_form = ShelfTwoUpdateForm(request.POST, request.FILES, instance=request.user.sellerprofile.shelftwo)
        if s_form.is_valid:
            s_form.save()
            shelf_name=s_form.cleaned_data.get('shelf_name')
            messages.success(request, 'shelf {} has been successfully updated!'.format(shelf_name))
            return redirect('seller-dashboard')
    else:
        s_form = ShelfTwoUpdateForm(instance=request.user.sellerprofile.shelftwo)
    context = {
        's_form': s_form,
}

    return render(request, 'amweb/shelftwo_update.html', context)


@login_required
def shelfthree_update(request):
    if request.method== 'POST':
        s_form = ShelfThreeUpdateForm(request.POST, request.FILES, instance=request.user.sellerprofile.shelfthree)
        if s_form.is_valid:
            s_form.save()
            shelf_name=s_form.cleaned_data.get('shelf_name')
            messages.success(request, 'shelf {} has been successfully updated!'.format(shelf_name))
            return redirect('seller-dashboard')
    else:
        s_form = ShelfThreeUpdateForm(instance=request.user.sellerprofile.shelfthree)
    context = {
        's_form': s_form,
}

    return render(request, 'amweb/shelfthree_update.html', context)


@login_required
def shelffour_update(request):
    if request.method== 'POST':
        s_form = ShelfFourUpdateForm(request.POST, request.FILES, instance=request.user.sellerprofile.shelffour)
        if s_form.is_valid:
            s_form.save()
            shelf_name=s_form.cleaned_data.get('shelf_name')
            messages.success(request, 'shelf {} has been successfully updated!'.format(shelf_name))
            return redirect('seller-dashboard')
    else:
        s_form = ShelfFourUpdateForm(instance=request.user.sellerprofile.shelffour)
    context = {
        's_form': s_form,
}

    return render(request, 'amweb/shelffour_update.html', context)



@login_required
def shelffive_update(request):
    if request.method== 'POST':
        s_form = ShelfFiveUpdateForm(request.POST, request.FILES, instance=request.user.sellerprofile.shelffive)
        if s_form.is_valid:
            s_form.save()
            shelf_name=s_form.cleaned_data.get('shelf_name')
            messages.success(request, 'shelf {} has been successfully updated!'.format(shelf_name))
            return redirect('seller-dashboard')
    else:
        s_form = ShelfFiveUpdateForm(instance=request.user.sellerprofile.shelffive)
    context = {
        's_form': s_form,
}

    return render(request, 'amweb/shelffive_update.html', context)


