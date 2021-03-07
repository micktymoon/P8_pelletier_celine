from django.test import TestCase

from website.forms import SignUpForm, SearchForm


class SignUpFormTest(TestCase):
    def test_signup_form_first_name_field_label(self):
        form = SignUpForm()
        self.assertTrue(form.fields['first_name'].label is None
                        or form.fields['first_name'].label == 'first name')

    def test_signup_form_last_name_field_label(self):
        form = SignUpForm()
        self.assertTrue(form.fields['last_name'].label is None
                        or form.fields['last_name'].label == 'last name')

    def test_signup_form_email_field_label(self):
        form = SignUpForm()
        self.assertTrue(form.fields['email'].label is None
                        or form.fields['email'].label == 'email')

    def test_signup_form_first_name_field_help_text(self):
        form = SignUpForm()
        self.assertEqual(form.fields['first_name'].help_text,
                         'Entrez votre prénom.')

    def test_signup_form_last_name_field_help_text(self):
        form = SignUpForm()
        self.assertEqual(form.fields['last_name'].help_text,
                         'Entrez votre nom.')

    def test_signup_form_email_field_help_text(self):
        form = SignUpForm()
        self.assertEqual(form.fields['email'].help_text,
                         'Entrez une adresse email valide.')

    def test_signup_form_first_name_field_max_length(self):
        form = SignUpForm()
        self.assertEqual(form.fields['first_name'].max_length, 30)

    def test_signup_form_last_name_field_max_length(self):
        form = SignUpForm()
        self.assertEqual(form.fields['last_name'].max_length, 30)

    def test_signup_form_email_field_max_length(self):
        form = SignUpForm()
        self.assertEqual(form.fields['email'].max_length, 254)
