from django.shortcuts import render, HttpResponseRedirect
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
