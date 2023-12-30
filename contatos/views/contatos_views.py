from django.shortcuts import render, get_object_or_404, redirect 
from contatos.models import Contato
from django.db.models import Q
from django.core.paginator import Paginator


def index(request):
    contatos = Contato.objects.filter(mostrar=True).order_by('-id')

    paginator = Paginator(contatos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'page_obj':page_obj,
        'site_title':'Contatos -'
    }
    return render(request,
    'contatos/index.html',
    context=context  
     )


def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contato:index')
    contatos = Contato.objects.filter(mostrar=True).filter(Q(nome__icontains=search_value) | \
    Q  (sobrenome__icontains=search_value) | Q\
            (email__icontains=search_value) |Q  (telefone__icontains=search_value)                                                     ).order_by('-id')
    
    paginator = Paginator(contatos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj':page_obj,
        'site_title':'Contatos -',
        'search_value':search_value
    }
    return render(request,
    'contatos/index.html',
    context=context  
     )


def contact(request, contact_id):
    single_contact = get_object_or_404(Contato.objects, pk=contact_id, mostrar=True)
    context = {
        'contacts':single_contact,
        'site_title':single_contact
    }
    return render(request,
    'contatos/ver_contato.html',
    context=context  
     )