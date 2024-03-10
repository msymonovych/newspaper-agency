from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.models import Redactor


class AdminTest(TestCase):
    def setUp(self):
        self.password = "testPass1"
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password=self.password
        )
        self.client.force_login(self.admin_user)
        self.redactor = Redactor.objects.create(
            username="redactor",
            password=self.password,
            first_name="Test",
            last_name="Redactor",
            years_of_experience=5
        )

    def test_redactor_list_display(self):
        response = self.client.get(
            reverse("admin:newspaper_redactor_changelist")
        )
        self.assertContains(response, self.redactor.years_of_experience)
        self.assertContains(response, self.redactor.first_name)
        self.assertContains(response, self.redactor.last_name)

    def test_redactor_detail_fieldsets(self):
        response = self.client.get(
            reverse(
                "admin:newspaper_redactor_change",
                args=[self.redactor.id])
        )
        self.assertContains(response, self.redactor.years_of_experience)
