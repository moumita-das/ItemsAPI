from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import auth
from .forms import ItemForm
from .models import ItemList


def loginView(request):
    if request.user.is_authenticated:
        return render(request, 'index.html', {'form': ItemForm()})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return render(request, 'index.html', {'form': ItemForm()})

        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def CreateView(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
        else:
            return render(request, 'index.html', {'form': form})
    return render(request, 'index.html', {'form': form})


def retrieveView(request):
    model = ItemList.objects.all()
    item = model[::-1][0]
    data = {"results": {
        "first name": item.fname,
        "last name": item.lname,
        "DOB": item.dob,
        "img": item.img.path
    }}
    return JsonResponse(data)
