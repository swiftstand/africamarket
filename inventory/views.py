from django.shortcuts import render,get_object_or_404,get_list_or_404,redirect
from django.views.generic import ListView,DetailView,CreateView
from .models import ItemShelfOne,ItemShelfTwo,ItemShelfThree,ItemShelfFour,ItemShelfFive,ShelfOne,ShelfTwo,ShelfThree,ShelfFour,ShelfFive
from users.models import SellerProfile
from django.contrib import messages

def sizes(modele):
    i=float(modele.shelf_size)
    m=int(i)
    return m

class FilterOne(ListView):
    model = ItemShelfOne
    template_name = 'inventory/filterone.html'
    context_object_name = 'filterone'
    paginate_by= 8


    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        shelf_rep= get_object_or_404(ShelfOne,pk=self.kwargs.get('pk'))
        context['shelfones']=ShelfOne.objects.filter(pk=shelf_rep.pk).first()
        sizeone=sizes(self.request.user.sellerprofile.shelfone)
        sizeonediv=(sizeone//2)+(sizeone//10)
        context['items_one_number']=ItemShelfOne.objects.filter(shelf=self.request.user.sellerprofile.shelfone).count()
        context['sizeone']=sizeone
        context['shelfonediv']=sizeonediv
        return context

    def get_queryset(self):
        shelf_pk= get_object_or_404(ShelfOne,pk=self.kwargs.get('pk'))
        items= get_list_or_404(ItemShelfOne,status=self.kwargs.get('status'))
        return ItemShelfOne.objects.filter(shelf=shelf_pk,status=items[0].status).order_by('-date_posted')



class FilterTwo(ListView):
    model = ItemShelfTwo
    template_name = 'inventory/filtertwo.html'
    context_object_name = 'filtertwo'
    paginate_by= 8


    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        shelf_rep= get_object_or_404(ShelfTwo,pk=self.kwargs.get('pk'))
        context['shelftwos']=ShelfTwo.objects.filter(pk=shelf_rep.pk).first()
        sizetwo=sizes(self.request.user.sellerprofile.shelftwo)
        sizetwodiv=(sizetwo//2)+(sizetwo//10)
        context['items_two_number']=ItemShelfTwo.objects.filter(shelf=self.request.user.sellerprofile.shelftwo).count()
        context['sizetwo']=sizetwo
        context['shelftwodiv']=sizetwodiv
        return context

    def get_queryset(self):
        shelf_pk= get_object_or_404(ShelfTwo,pk=self.kwargs.get('pk'))
        items= get_list_or_404(ItemShelfTwo,status=self.kwargs.get('status'))
        return ItemShelfTwo.objects.filter(shelf=shelf_pk,status=items[0].status).order_by('-date_posted')


class FilterThree(ListView):
    model = ItemShelfThree
    template_name = 'inventory/filterthree.html'
    context_object_name = 'filterthree'
    paginate_by= 8


    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        shelf_rep= get_object_or_404(ShelfThree,pk=self.kwargs.get('pk'))
        context['shelfthrees']=ShelfThree.objects.filter(pk=shelf_rep.pk).first()
        sizethree=sizes(self.request.user.sellerprofile.shelfthree)
        context['items_three_number']=ItemShelfThree.objects.filter(shelf=self.request.user.sellerprofile.shelfthree).count()
        context['sizethree']=sizethree
        context['shelfthreediv']=sizethreediv
        return context

    def get_queryset(self):
        shelf_pk= get_object_or_404(ShelfThree,pk=self.kwargs.get('pk'))
        items= get_list_or_404(ItemShelfThree,status=self.kwargs.get('status'))
        return ItemShelfThree.objects.filter(shelf=shelf_pk,status=items[0].status).order_by('-date_posted')


class FilterFour(ListView):
    model = ItemShelfFour
    template_name = 'inventory/filterfour.html'
    context_object_name = 'filterfour'
    paginate_by= 8


    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        shelf_rep= get_object_or_404(ShelfFour,pk=self.kwargs.get('pk'))
        context['shelffours']=ShelfFour.objects.filter(pk=shelf_rep.pk).first()
        context['items_four_number']=ItemShelfFour.objects.filter(shelf=self.request.user.sellerprofile.shelffour).count()
        sizefour=sizes(self.request.user.sellerprofile.shelffour)
        sizefourdiv=(sizefour//2)+(sizefour//10)
        context['sizefour']=sizefour
        context['shelffourdiv']=sizefourdiv
        return context

    def get_queryset(self):
        shelf_pk= get_object_or_404(ShelfFour,pk=self.kwargs.get('pk'))
        items= get_list_or_404(ItemShelfFour,status=self.kwargs.get('status'))
        return ItemShelfFour.objects.filter(shelf=shelf_pk,status=items[0].status).order_by('-date_posted')


class FilterFive(ListView):
    model = ItemShelfFive
    template_name = 'inventory/filterfive.html'
    context_object_name = 'filterfive'
    paginate_by= 8


    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        shelf_rep= get_object_or_404(ShelfFive,pk=self.kwargs.get('pk'))
        context['shelffives']=ShelfFive.objects.filter(pk=shelf_rep.pk).first()
        return context

    def get_queryset(self):
        shelf_pk= get_object_or_404(ShelfFive,pk=self.kwargs.get('pk'))
        items= get_list_or_404(ItemShelfFive,status=self.kwargs.get('status'))
        return ItemShelfFive.objects.filter(shelf=shelf_pk,status=items[0].status).order_by('-date_posted')



class ItemsOneListView(ListView):
    model = ItemShelfOne
    context_object_name = 'shelfonefilter'
    paginate_by=8

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        shelf_rep= get_object_or_404(ShelfOne,pk=self.kwargs.get('pk'))
        context['shelfones']=ShelfOne.objects.filter(pk=shelf_rep.pk).first()
        sizeone=sizes(self.request.user.sellerprofile.shelfone)
        context['items_one_number']=ItemShelfOne.objects.filter(shelf=self.request.user.sellerprofile.shelfone).count()
        sizeonediv=(sizeone//2)+(sizeone//10)
        context['sizeone']=sizeone
        context['shelfonediv']=sizeonediv
        return context

    def get_queryset(self):
        shelf= get_object_or_404(ShelfOne,pk=self.kwargs.get('pk'))
        return ItemShelfOne.objects.filter(shelf=shelf).order_by('-date_posted')


class ItemsTwosListView(ListView):
    model = ItemShelfTwo
    context_object_name = 'shelftwofilter'
    paginate_by= 8


    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        shelf_rep= get_object_or_404(ShelfTwo,pk=self.kwargs.get('pk'))
        context['shelftwos']=ShelfTwo.objects.filter(pk=shelf_rep.pk).first()
        sizetwo=sizes(self.request.user.sellerprofile.shelftwo)
        sizetwodiv=(sizetwo//2)+(sizetwo//10)
        context['items_two_number']=ItemShelfTwo.objects.filter(shelf=self.request.user.sellerprofile.shelftwo).count()
        context['sizetwo']=sizetwo
        context['shelftwodiv']=sizetwodiv
        return context

    def get_queryset(self):
        shelf= get_object_or_404(ShelfTwo,pk=self.kwargs.get('pk'))
        return ItemShelfTwo.objects.filter(shelf=shelf).order_by('-date_posted')


class ItemsThreeListView(ListView):
    model = ItemShelfThree
    context_object_name = 'shelfthreefilter'
    paginate_by= 8


    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        shelf_rep= get_object_or_404(ShelfThree,pk=self.kwargs.get('pk'))
        context['shelfthrees']=ShelfThree.objects.filter(pk=shelf_rep.pk).first()
        sizethree=sizes(self.request.user.sellerprofile.shelfthree)
        context['items_three_number']=ItemShelfThree.objects.filter(shelf=self.request.user.sellerprofile.shelfthree).count()
        sizethreediv=(sizethree//2)+(sizethree//10)
        context['sizethree']=sizethree
        context['shelfthreediv']=sizethreediv
        return context

    def get_queryset(self):
        shelf= get_object_or_404(ShelfThree,pk=self.kwargs.get('pk'))
        return ItemShelfThree.objects.filter(shelf=shelf).order_by('-date_posted')


class ItemsFourListView(ListView):
    model = ItemShelfFour
    context_object_name = 'shelffourfilter'
    paginate_by= 8


    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        shelf_rep= get_object_or_404(ShelfFour,pk=self.kwargs.get('pk'))
        context['shelffours']=ShelfFour.objects.filter(pk=shelf_rep.pk).first()
        sizefour=sizes(self.request.user.sellerprofile.shelffour)
        context['items_four_number']=ItemShelfFour.objects.filter(shelf=self.request.user.sellerprofile.shelffour).count()
        sizefourdiv=(sizefour//2)+(sizefour//10)
        context['sizefour']=sizefour
        context['shelffourdiv']=sizefourdiv
        return context

    def get_queryset(self):
        shelf= get_object_or_404(ShelfFour,pk=self.kwargs.get('pk'))
        return ItemShelfFour.objects.filter(shelf=shelf).order_by('-date_posted')


class ItemsFiveListView(ListView):
    model = ItemShelfFive
    context_object_name = 'shelffivefilter'
    paginate_by= 8


    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        shelf_rep= get_object_or_404(ShelfFive,pk=self.kwargs.get('pk'))
        context['shelffives']=ShelfFive.objects.filter(pk=shelf_rep.pk).first()
        context['sizefive']=sizes(ShelfFive)
        return context

    def get_queryset(self):
        shelf= get_object_or_404(ShelfFive,pk=self.kwargs.get('pk'))
        return ItemShelfFive.objects.filter(shelf=shelf).order_by('-date_posted')



def shelfsize(modele):
    i=float(modele.shelf_size)
    m=int(i)
    return m

class ItemShelfOneCreate(CreateView):
    model = ItemShelfOne
    template_name = 'inventory/item_form.html'
    fields = ['name','image','price','discount_price','item_description','status']

    def form_valid(self, form):
        form.instance.shelf=self.request.user.sellerprofile.shelfone
        size=shelfsize(form.instance.shelf)
        if ItemShelfOne.objects.filter(shelf=form.instance.shelf).count()<size:
            name=form.cleaned_data.get('name')
            status=form.cleaned_data.get('status')
            messages.success(self.request, 'A Product Card For Item {}  With Status {} Has Been Successfully Created '.format(name,status))
            return super().form_valid(form)
            product_card = form.save(commit=False)
            product_card.save()
        else:
            size=ItemShelfOne.objects.filter(shelf=form.instance.shelf).count()
            messages.warning(self.request, 'Your Shelf Has Been Completely Filled Up With {} Items,  Product Card Was Not Added '.format(size))
            return redirect('itemsone',self.request.user.store_name,self.request.user.sellerprofile.shelfone.pk,self.request.user.sellerprofile.shelfone.slug)



class ItemShelfTwoCreate(CreateView):
    model = ItemShelfTwo
    template_name = 'inventory/item_form.html'
    fields = ['name','image','price','discount_price','item_description','status']

    def form_valid(self, form):
        form.instance.shelf=self.request.user.sellerprofile.shelftwo
        size=shelfsize(form.instance.shelf)
        if ItemShelfTwo.objects.filter(shelf=form.instance.shelf).count()<size:
            name=form.cleaned_data.get('name')
            status=form.cleaned_data.get('status')
            messages.success(self.request, 'A Product Card For Item {}  With Status {} Has Been Successfully Created '.format(name,status))
            return super().form_valid(form)
            product_card = form.save(commit=False)
            product_card.save()
        else:
            size=ItemShelfTwo.objects.filter(shelf=form.instance.shelf).count()
            messages.warning(self.request, 'Your Shelf Has Been Completely Filled Up With {} Items,   Product Card Was Not Added '.format(size))
            return redirect('itemsone',self.request.user.store_name,self.request.user.sellerprofile.shelftwo.pk,self.request.user.sellerprofile.shelftwo.slug)


class ItemShelfThreeCreate(CreateView):
    model = ItemShelfThree
    template_name = 'inventory/item_form.html'
    fields = ['name','image','price','discount_price','item_description','status']

    def form_valid(self, form):
        form.instance.shelf=self.request.user.sellerprofile.shelfthree
        size=shelfsize(form.instance.shelf)
        if ItemShelfThree.objects.filter(shelf=form.instance.shelf).count()<size:
            name=form.cleaned_data.get('name')
            status=form.cleaned_data.get('status')
            messages.success(self.request, 'A Product Card For Item {}  With Status {} Has Been Successfully Created '.format(name,status))
            return super().form_valid(form)
            product_card = form.save(commit=False)
            product_card.save()
        else:
            size=ItemShelfThree.objects.filter(shelf=form.instance.shelf).count()
            messages.warning(self.request, 'Your Shelf Has Been Completely Filled Up With {} Items,   Product Card Was Not Added '.format(size))
            return redirect('itemsone',self.request.user.store_name,self.request.user.sellerprofile.shelfthree.pk,self.request.user.sellerprofile.shelfthree.slug)


class ItemShelfFourCreate(CreateView):
    model = ItemShelfFour
    template_name = 'inventory/item_form.html'
    fields = ['name','image','price','discount_price','item_description','status']

    def form_valid(self, form):
        form.instance.shelf=self.request.user.sellerprofile.shelffour
        size=shelfsize(form.instance.shelf)
        if ItemShelfFour.objects.filter(shelf=form.instance.shelf).count()<size:
            name=form.cleaned_data.get('name')
            status=form.cleaned_data.get('status')
            messages.success(self.request, 'A Product Card For Item {}  With Status {} Has Been Successfully Created '.format(name,status))
            return super().form_valid(form)
            product_card = form.save(commit=False)
            product_card.save()
        else:
            size=ItemShelfFour.objects.filter(shelf=form.instance.shelf).count()
            messages.warning(self.request, 'Your Shelf Has Been Completely Filled Up With {} Items,   Product Card Was Not Added '.format(size))
            return redirect('itemsone',self.request.user.store_name,self.request.user.sellerprofile.shelffour.pk,self.request.user.sellerprofile.shelffour.slug)


class ItemShelfFiveCreate(CreateView):
    model = ItemShelfFive
    template_name = 'inventory/item_form.html'
    fields = ['name','image','price','discount_price','item_description','status']

    def form_valid(self, form):
        form.instance.shelf=self.request.user.sellerprofile.shelffive
        size=shelfsize(form.instance.shelf)
        if ItemShelfFive.objects.filter(shelf=form.instance.shelf).count()<size:
            name=form.cleaned_data.get('name')
            status=form.cleaned_data.get('status')
            messages.success(self.request, 'A Product Card For Item {}  With Status {} Has Been Successfully Created '.format(name,status))
            return super().form_valid(form)
            product_card = form.save(commit=False)
            product_card.save()
        else:
            size=ItemShelfFive.objects.filter(shelf=form.instance.shelf).count()
            messages.warning(self.request, 'Your Shelf Has Been Completely Filled Up With {} Items,   Product Card Was Not Added '.format(size))
            return redirect('itemsone',self.request.user.store_name,self.request.user.sellerprofile.shelffive.pk,self.request.user.sellerprofile.shelffive.slug)
