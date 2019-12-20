from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Snake, Scientist
from .forms import SnakeForm, LoginForm, RegisterForm 

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def snakes(request):
    snakes = Snake.objects.all()
    if request.session.get('authenticated'):
        return render(request, 'snakes.html', {
            'snakes': snakes,
            'scientists': scientists,
            'first_name': request.session.get('first_name'),   
            'last_name': request.session.get('last_name')  
        })
    else:
        return redirect('home')
    
def add(request):
    if request.session.get('authenticated'):
        if request.method == 'POST':
                form = SnakeForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Snake has been successfully added!')
                else:
                     messages.error(request, 'Snake has not been added')
                return redirect('snakes')           
        else:
            form = SnakeForm()
            return render(request, 'add.html', {
                'form': form,
                'scientists': scientists,
                'first_name': request.session.get('first_name'),   
                'last_name': request.session.get('last_name')  
            })     
    else:
        return redirect('home')

def show(request, id):
    return render(request, 'show.html', {})

def edit(request, id):
    if request.session.get('authenticated'):
            snake = get_object_or_404(Snake, pk=id)
            if request.method == 'POST':
                form = SnakeForm(request.POST, instance=snake)
                form.save()
                messages.success(request, 'Snake has been successfully modified!')
                return redirect('snakes')
            else:
                form = SnakeForm(instance=snake)
                return render(request, 'edit.html', {
                    'form': form,
                    'snake': snake,
                    'scientists': scientists,
                    'first_name': request.session.get('first_name'),   
                    'last_name': request.session.get('last_name')  
                })
    else:
        return redirect('home')

def delete(request, id):
    if request.method == 'POST':
        snake = get_object_or_404(Snake, pk=id)
        snake.delete() 
    return redirect('snakes')

def home(request):
    if request.method == 'POST':
        if Scientist.objects.filter(email=request.POST.get('email')).exists():
            if Scientist.objects.filter(email=request.POST.get('email')).first().password == request.POST.get('password'):
                request.session['authenticated'] = True
                request.session['user_email'] = request.POST.get('email')     
                request.session['first_name'] = Scientist.objects.filter(email=request.POST.get('email')).first().first_name
                request.session['last_name'] = Scientist.objects.filter(email=request.POST.get('email')).first().last_name
                return redirect('dashboard')
            else:
                return redirect('home')
        else:
            return redirect('home') 
    else:
        login_form = LoginForm()
        return render(request, 'home.html', {
            'login_form': login_form
        })

def appRegister(request):
    if request.method == 'POST':
        submitted_register_form = RegisterForm(request.POST)
        if submitted_register_form.is_valid():
            submitted_register_form.save()
            request.session['authenticated'] = True
            request.session['user_email'] = request.POST.get('email') 
            request.session['first_name'] = Scientist.objects.filter(email=request.POST.get('email')).first().first_name
            request.session['last_name'] = Scientist.objects.filter(email=request.POST.get('email')).first().last_name
            return redirect('dashboard')
    else: 
        register_form = RegisterForm()
        return render(request, 'register.html', {
            'register_form': register_form
        })

def dashboard(request):
    scientists = Scientist.objects.all()
    if request.session.get('authenticated'):
        return render(request, 'dashboard.html', {
            'scientists': scientists,
            'first_name': request.session.get('first_name'),   
            'last_name': request.session.get('last_name')             
    })
    else:
        return redirect('home')  
    
def logout(request): 
    if request.method == 'POST':
        request.session['authenticated'] = False
        request.session['user_email'] = ''
        return redirect('home')
    else:
        return redirect('dashboard')

def scientists(request):
    scientists = Scientist.objects.all()
    if request.session.get('authenticated'):
        return render(request, 'scientists.html', {
            'scientists': scientists,
            'email': request.session.get('user_email'),
            'first_name': request.session.get('first_name'),   
            'last_name': request.session.get('last_name')             
    })
    else:
        return redirect('home')  
    
def delete_scientist(request, id):
    if request.method == 'POST':
        scientist = get_object_or_404(Scientist, pk=id)
        scientist.delete()
    return redirect('scientists')
