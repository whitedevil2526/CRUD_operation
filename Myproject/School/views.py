from django.shortcuts import render, HttpResponseRedirect,get_object_or_404
from .models import Shoes
from .forms import ShoeForm

def home(request):
    shoes = Shoes.objects.all()  # Fetch all shoes at the beginning
    print(shoes)  # Debugging: Check if data is being retrieved

    if request.method == "POST":
        form = ShoeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")  # Redirect to prevent duplicate form submission
    else:
        form = ShoeForm()  # Initialize an empty form for GET request

    return render(request, 'school/home.html', {'form': form, 'shoes': shoes})  # Ensure 'shoes' matches template

def update_shoe(request, shoe_id):
    shoe = Shoes.objects.get(pk=shoe_id)
    if request.method == "POST":
        form = ShoeForm(request.POST, request.FILES, instance=shoe)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")  # Redirect to shoe list or shoe details page
    else:
        form = ShoesForm(instance=shoe)

    return render(request, 'update_shoe.html', {'form': form})

def delete_shoe(request, shoe_id):
    shoe = get_object_or_404(Shoes, id=shoe_id)
    if request.method == "POST":
        shoe.delete()
        return HttpResponseRedirect("/")  # Redirect to shoe list after deletion

    return render(request, 'confirm_delete.html', {'shoe': shoe})