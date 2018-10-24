from django.shortcuts import render,redirect
from .forms import NewBookForm,NewRideForm
from .models import Book,Ride

# def home(request):
#     form = NewRideForm()
#     price = Ride.objects.all()
#     return render(request, 'home.html',{"form": form,"price":price})


def price(request):
    form = NewRideForm()
    if request.method == 'POST':
        form = NewRideForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save()
            new_post.save()
        return redirect('home')
    else:
        form = NewRideForm()
    return render(request, 'price.html',{"form": form})


def search_location(request):
    title = 'booky'
                                                                  
    if 'search' in request.GET and request.GET['search']:
        search_item = request.GET.get('search')
        searched_location = Ride.objects.filter(location=search_item)
        message = f"{searched_location}"
        return render(request, 'home.html',{"message":message,"location": searched_location })
    else:
        message = "You haven't searched for any location"
        return render(request, 'home.html',{"message":message})


