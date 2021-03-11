from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
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
    search = forms.CharField(label='Produit recherché', max_length=100)
