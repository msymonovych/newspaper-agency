from django.test import TestCase

from newspaper.models import Topic, Redactor, News


class ModelsTest(TestCase):

    def setUp(self):
        self.topic = Topic.objects.create(name="testTopic")
        self.redactor = Redactor.objects.create(
            username="testRedactor",
            password="testPass1",
            first_name="testFirstName",
            last_name="testLastName",
            years_of_experience=9
        )
        self.newspaper = News.objects.create(
            title="testNewspaper",
            content="testContent",
        )

    def test_topic_str(self):
        self.assertEqual(str(self.topic), "testTopic")

    def test_redactor_str(self):
        self.assertEqual(str(self.redactor), "testRedactor")

    def test_newspaper_str(self):
        self.assertEqual(
            str(self.newspaper),
            f"{self.newspaper.title} {self.newspaper.publish_date}"
        )
