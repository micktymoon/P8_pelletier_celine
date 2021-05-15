from django.test import TestCase

from website.forms import SignUpForm, SearchForm


class SignUpFormTest(TestCase):
    def setUp(self):
        self.form = SignUpForm()
        self.form.fields['username'] = 'testusername'
        self.form.fields['first_name'] = 'testfirstname'
        self.form.fields['last_name'] = 'testlastname'
        self.form.fields['email'] = 'testemail'
        self.form.fields['password1'] = 'testpassword'
        self.form.fields['password2'] = 'testpassword'
        self.form.__init__()

    def test_signup_form_first_name_field_label(self):
        self.assertTrue(self.form.fields['first_name'].label is None
                        or
                        self.form.fields['first_name'].label == 'first name')

    def test_signup_form_last_name_field_label(self):
        self.assertTrue(self.form.fields['last_name'].label is None
                        or self.form.fields['last_name'].label == 'last name')

    def test_signup_form_email_field_label(self):
        self.assertTrue(self.form.fields['email'].label is None
                        or self.form.fields['email'].label == 'email')

    def test_signup_form_first_name_field_help_text(self):
        self.assertEqual(self.form.fields['first_name'].help_text,
                         'Entrez votre prénom.')

    def test_signup_form_last_name_field_help_text(self):
        self.assertEqual(self.form.fields['last_name'].help_text,
                         'Entrez votre nom.')

    def test_signup_form_email_field_help_text(self):
        self.assertEqual(self.form.fields['email'].help_text,
                         'Entrez une adresse email valide.')

    def test_signup_form_first_name_field_max_length(self):
        self.assertEqual(self.form.fields['first_name'].max_length, 30)

    def test_signup_form_last_name_field_max_length(self):
        self.assertEqual(self.form.fields['last_name'].max_length, 30)

    def test_signup_form_email_field_max_length(self):
        self.assertEqual(self.form.fields['email'].max_length, 254)

    def test_signup_form_field_class_is_form_control(self):
        for visible in self.form.visible_fields():
            self.assertEqual(visible.field.widget.attrs['class'],
                             'form-control')


class SearchFormTest(TestCase):
    def test_search_form_search_field_label(self):
        form = SearchForm()
        self.assertTrue(form.fields['search'].label is None
                        or form.fields['search'].label == 'Produit recherché')

    def test_search_form_search_field_max_length(self):
        form = SearchForm()
        self.assertEqual(form.fields['search'].max_length, 100)
