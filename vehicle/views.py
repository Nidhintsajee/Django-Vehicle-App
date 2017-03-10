from django.shortcuts import render
from django.utils import timezone
from .models import PostsSubmit
from .forms import PostsSubmitForm

# Create your views here.


def add_vehicle(request):
    form = PostsSubmitForm()
    context = {'form': form}
    return render(request, 'vehicle/add_vehicle.html', context)


def save_vehicle(request):
    if request.method == "POST":
        form = PostsSubmitForm(request.POST, request.FILES)
        # print("outside if saveproduct")
        print(form.errors)
        if form.is_valid():
            # print('save_productviewsample')
            form.save()
            context = {'form': form}
            print(form.errors)
            return render(request, 'vehicle/save_vehicle.html', context)
    else:
        form = PostsSubmitForm()
        print(form.errors)
        return render(request, 'vehicle/add_vehicle.html', {'form': form})


def vehicle_display(request):
    List = PostsSubmit.objects.all()
    context = {'List': List}
    return render(request, 'vehicle/vehicle_display.html', context)


def click_vehicle(request, vehicle_id):
    # print List
    # print product_id
    obj = PostsSubmit.objects.get(id=vehicle_id)
    # print key
    # obj = PostsSubmit.objects.get(id = key)
    print(obj)
    return render(request, 'click_vehicle.html', {'obj': obj})

def edit_vehicle(request,vehicle_id):
    obj = PostsSubmit.objects.get(id=vehicle_id)
    form = PostsSubmitForm(instance=obj)
    context = {'form': form}
    return render(request, 'vehicle/add_vehicle.html', context)

