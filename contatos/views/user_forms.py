from django.shortcuts import render, redirect
from contatos.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

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
            messages.success(request, 'Logado com sucesso')
            return redirect('contato:index')
        messages.error(request, 'Login inválido!')
            

    return render(request, 'contatos/login.html', context)

@login_required(login_url='contato:index')
def logout_view(request):
    auth.logout(request)
    return redirect('contato:login')

@login_required(login_url='contato:login')
def user_update(request):
    form = RegisterUpdateForm(
        instance=request.user
    )

    if request.method != 'POST':
        return render(
            request,
            'contatos/register.html',
            {
                'form': form
            }
        )
    
    form = RegisterUpdateForm(
        data=request.POST,
        instance=request.user
    )

    if not form.is_valid():
        messages.error(request, 'Invalid')
        return render(
            request,
            'contatos/register.html',
            {
                'form': form
            }
        )
    
    form.save()
    return redirect('contato:user_update')