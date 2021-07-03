from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    """A form to register new user accounts"""

    first_name = forms.CharField(max_length=30,
                                 required=False,
                                 help_text='Entrez votre prénom.')
    last_name = forms.CharField(max_length=30,
                                required=False,
                                help_text='Entrez votre nom.')
    email = forms.EmailField(max_length=254,
                             help_text='Entrez une adresse email valide.')

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email',
                  'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class SearchForm(forms.Form):
    """A form to search for a product in the database"""
    search = forms.CharField(label='Produit recherché', max_length=100)


class ContactForm(forms.Form):
    """A form that sends a message to the contact of the website"""
    name = forms.CharField(label='Nom, Prénom', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    message = forms.CharField(label='Message')
