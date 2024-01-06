from django.core.exceptions import ValidationError
from django import forms
from .models import Contato
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )

    last_name = forms.CharField(
        required=True,
        min_length=3,
    )

    email = forms.CharField()
    
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1', 'password2'
        )

    def clean_email(self):

        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Este  email já esite', code='invalid')
            )
        
        return email
    


class ContactForms(forms.ModelForm):

    foto = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )

    class Meta:
        model = Contato
        fields = (
            'nome', 'sobrenome', 'telefone', 'descricao', 'email', 'categoria', 'foto',
        )

    
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Escreva aqui'
            }
        ),
        help_text='Texto de ajuda'
    )

    def clean(self):
        nome = self.cleaned_data.get('nome')
        sobrenome = self.cleaned_data.get('sobrenome')
        if nome == sobrenome:
            msg = ValidationError(
                'O nome não pode ser igual ao sobrenome',
                code='invalid'
            )

            self.add_error('nome', error=msg)
            self.add_error('sobrenome', error=msg)


        # self.add_error(
        #     'nome',
        #     ValidationError(
        #         'Mensagen de erro',
        #         code='invalid'
        #     )
        # )
        # self.add_error(
        #     'sobrenome',
        #     ValidationError(
        #     'Mensagen de erro',
        #     code='invalid',
        # )
        # )
        return super().clean()
    
    
    def clean_nome(self):
        nome = self.cleaned_data.get('nome')

        if nome == 'aaa':
            'nome',
            ValidationError(
                'Mensagen de erro 2',
                code='invalid'
            )
    
        return nome