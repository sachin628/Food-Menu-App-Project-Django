from pdb import post_mortem
from django.shortcuts import render, redirect
from .models import Item
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.template import loader
from .forms import ItemForm

def index(request):
    item_list =  Item.objects.all()
    template = loader.get_template('food/index.html')

    context = {
        'item_list': item_list,
         
    }
    #this is another way to render the template page'html page'
    #return HttpResponse(template.render(context, request))
    return render(request,'food/index.html', context)



def item(request):
    return HttpResponse('This is an item view')


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    template = loader.get_template('food/detail.html')
    context ={
        'item': item,
    }

    return render(request, 'food/detail.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item-form.html',{'form':form})

# this is a class based view for create itemm

class CreateItem(CreateView):
    model = Item
    fields = ['item_name','item_desc','item_price','item_image']
    template_name='food/item-form.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)
    

def update_item(request, id, self):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item-form.html',{'form':form,'item':item})

def delete_item(request, id):
    item =item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request,'food/item-delete.html', {'item': item})    







