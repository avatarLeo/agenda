from django.shortcuts import render, redirect
from contatos.forms import RegisterForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    form = RegisterForm()

   
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado com sucesso')
            return redirect('contato:index')

    return render(request, 'contatos/register.html',
    {
        'form': form
    }              
                  )

def login_view(request):

    form = AuthenticationForm(request)

    context = {
            'form': form
        }

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        context = {
            'form': form
        }

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            

    return render(request, 'contatos/login.html', context)