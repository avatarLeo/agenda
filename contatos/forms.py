from typing import Any
from django.core.exceptions import ValidationError
from django import forms
from .models import Contato
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

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
        ),
        required=False
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
    

class RegisterUpdateForm(forms.ModelForm):
        
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.'
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)

        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self) -> dict[str, Any]:
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não batem.')
                )
        return super().clean()


    def clean_email(self):

        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email!= email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Este  email já esite', code='invalid')
                )
        
        return email
    

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )


        return password1

