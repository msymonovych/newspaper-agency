from django.test import TestCase

from newspaper.forms import RedactorCreationForm


class FormsTest(TestCase):

    def test_redactor_creation_form(self):
        test_password = "testPass1"
        form_data = {
            "username": "test_user",
            "password1": test_password,
            "password2": test_password,
            "first_name": "User",
            "last_name": "Test",
            "years_of_experience": 10
        }
        form = RedactorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
