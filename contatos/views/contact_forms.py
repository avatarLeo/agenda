from django.shortcuts import render, redirect, get_object_or_404
from contatos.forms import ContactForms
from django.urls import reverse
from contatos.models import Contato


def create(request):
    form_action = reverse('contato:create')
    if request.method == 'POST':
        form = ContactForms(request.POST, request.FILES)
        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contato:update', contact_id=contact.pk)


        return render(request,
        'contatos/create.html', context
        )

    context = {
        'form': ContactForms(),
        'form_action': form_action,
    }

    return render(request,
    'contatos/create.html', context
    )

def update(request, contact_id):
    contact = get_object_or_404(Contato, pk=contact_id, mostrar=True)

    form_action = reverse('contato:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForms(request.POST, request.FILES, instance=contact)
        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contato:update', contact_id=contact.id)


        return render(request,
        'contatos/create.html', context
        )

    context = {
        'form': ContactForms(instance=contact),
        'form_action': form_action,
    }

    return render(request,
    'contatos/create.html', context
    )

def delete(request, contact_id):
    contact =  get_object_or_404(
        Contato, pk=contact_id, mostrar=True
        )
    contact.delete()
    return redirect('contato:index'
     )