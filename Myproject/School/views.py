from django.shortcuts import render, get_object_or_404, redirect,HttpResponseRedirect
from .models import Shoes
from .forms import ShoeForm

def home(request):
    shoes = Shoes.objects.all()
    return render(request, 'home.html', {'shoes': shoes})

def update_shoe(request, id):
    shoe = get_object_or_404(Shoes, id=id)
    if request.method == 'POST':
        form = ShoeForm(request.POST, request.FILES, instance=shoe)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        pi = Shoes.objects.get(pk=id)
        form = ShoeForm(instance=shoe)
    return render(request, 'shoes/home.html', {'form': form})

def delete_shoe(request, id):
    shoe = get_object_or_404(Shoes, id=id)
    if request.method == 'POST':
        shoe.delete()
        return redirect('home')
    return HttpResponseRedirect("/")
