from django.shortcuts import redirect, render
from .models import ToDo
from .forms import FormToDo
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
# my ToDo


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'user dont not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username OR password does not exist')

    return render(request, 'register/login.html')



def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        username = User.objects.all()
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # print(form)
        if username not in username:
            if  password1 == password2:
                if form.is_valid():
                    user = form.save(commit=False)
                    user.username = user.username.lower()
                    user.save()
                    return redirect('home')
            else:
                messages.error(request, 'Error password')
            
        else:
            messages.error(request, 'a user with the same name already exists')

    return render(request, 'register/register.html')



def home(request):
    todo = None
    if request.user.is_authenticated:
        todo = ToDo.objects.filter(user=request.user)
    context = {
        'Todo': todo
    }
    return render(request, 'body/todo.html', context)


@login_required(login_url='/login')
def create_Todo(request):

    if request.POST.get('title') not in "":
        title_get = request.POST.get('title') 
        if request.method == "POST":
            ToDo.objects.create(
                user=request.user,
                title=title_get
            )
            return redirect('home')
    else:
        return redirect('home')
    
    return render(request, 'body/todo.html')


def update_Todo(request, pk):
    todo = ToDo.objects.get(id=pk)
    form = FormToDo(instance=todo)
    if request.method == "POST":
        todo.title = request.POST.get('title')
        todo.description=request.POST.get('description')
        todo.save()
        return redirect('home')
    context = {
        'form':form
    }
    return render(request, 'body/update.html', context)


def delete_todo(request, pk):
    todo = ToDo.objects.get(id=pk)
    todo.delete()
    return redirect('home')






