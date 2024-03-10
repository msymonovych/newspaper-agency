from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.models import Topic, Redactor, News


urls = {
    "NEWS_LIST_PUB_URL": reverse("newspaper:news-list"),
    "NEWS_DETAIL_PUB_URL": reverse("newspaper:news-detail", kwargs={"pk": 1}),
    "NEWS_UPDATE_URL": reverse("newspaper:news-update", kwargs={"pk": 1}),
    "NEWS_DELETE_URL": reverse("newspaper:news-delete", kwargs={"pk": 1}),
    "NEWS_CREATE_URL": reverse("newspaper:news-create"),
    "REDACTOR_LIST_PUB_URL": reverse("newspaper:redactor-list"),
    "REDACTOR_DETAIL_PUB_URL": reverse(
        "newspaper:redactor-detail", kwargs={"pk": 1}
    ),
    "REDACTOR_UPDATE_URL": reverse(
        "newspaper:redactor-update", kwargs={"pk": 1}
    ),
    "REDACTOR_DELETE_URL": reverse(
        "newspaper:redactor-delete", kwargs={"pk": 1}
    ),
    "REDACTOR_CREATE_PUB_URL": reverse("newspaper:redactor-create")
}


class PublicViewTests(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(
            name="Test Topic"
        )
        self.redactor = Redactor.objects.create_user(
            username="admin.test",
            password="testPass1",
            years_of_experience=10
        )
        self.news = News.objects.create(
            title="Test",
            content="Test content",
        )
        self.news.topics.add(self.topic)

    def test_login_required(self):
        for key in urls:
            if key.endswith("PUB_URL"):
                self.assertEqual(
                    self.client.get(urls[key]).status_code, 200
                )
            else:
                self.assertEqual(
                    self.client.get(urls[key]).status_code, 302
                )

    def test_retrieve_news(self):
        response = self.client.get(urls["NEWS_LIST_PUB_URL"])
        news = News.objects.all()
        self.assertEqual(
            list(response.context["news_list"]),
            list(news)
        )
        self.assertTemplateUsed(response, "newspaper/news_list.html")

    def test_retrieve_redactor(self):
        response = self.client.get(urls["REDACTOR_LIST_PUB_URL"])
        redactors = get_user_model().objects.all()
        self.assertEqual(
            list(response.context["redactor_list"]),
            list(redactors)
        )
        self.assertTemplateUsed(response, "newspaper/redactor_list.html")

    def test_search_news_by_title(self):
        target_title = "Target Title"
        News.objects.create(
            title=target_title,
            content="Content",
        )
        response = self.client.get(
            urls["NEWS_LIST_PUB_URL"] + f"?title={target_title}"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(response.context["news_list"]),
            1
        )
        self.assertContains(
            response,
            target_title
        )

    def test_search_news_by_topic(self):
        target_topic = Topic.objects.create(
            name="Target Topic"
        )
        test_news = News.objects.create(
            title="Test 2",
            content="Content",
        )
        test_news.topics.add(target_topic)
        response = self.client.get(
            urls["NEWS_LIST_PUB_URL"] + f"?topic={target_topic.name}"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(response.context["news_list"]),
            1
        )
        self.assertContains(
            response,
            target_topic.name
        )

    def test_search_news_by_title_and_topic(self):
        target_title = "Test"
        test_news = News.objects.create(
            title="Test 2",
            content="Content"
        )
        test_news.topics.add(self.topic)
        response = self.client.get(
            urls["NEWS_LIST_PUB_URL"]
            + f"?title={target_title}&topic={self.topic.name}"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(response.context["news_list"]),
            2
        )

    def test_detail_news(self):
        response = self.client.get(urls["NEWS_DETAIL_PUB_URL"])
        news = News.objects.get(pk=1)
        self.assertEqual(
            response.context["news"],
            news
        )
        self.assertTemplateUsed(response, "newspaper/news_detail.html")

    def test_detail_redactor(self):
        response = self.client.get(urls["REDACTOR_DETAIL_PUB_URL"])
        redactor = get_user_model().objects.get(pk=1)
        self.assertEqual(
            response.context["redactor"],
            redactor
        )
        self.assertTemplateUsed(response, "newspaper/redactor_detail.html")

    def test_create_redactor(self):
        test_username = "user.test"
        response = self.client.post(
            urls["REDACTOR_CREATE_PUB_URL"],
            {
                "username": test_username,
                "password1": "testPass1",
                "password2": "testPass1",
                "years_of_experience": "10",
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            get_user_model().objects.filter(username=test_username).exists()
        )


class PrivateViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="testPass1",
            years_of_experience=10,
        )
        self.client.force_login(self.user)
        self.topic = Topic.objects.create(
            name="test"
        )
        self.news = News.objects.create(
            title="Test news",
            content="Test content",
        )
        self.news.topics.add(self.topic)
        self.news.publishers.add(self.user)

    def test_create_news(self):
        test_title = "Test title"
        response = self.client.post(
            urls["NEWS_CREATE_URL"],
            {
                "title": test_title,
                "content": "Test Content",
                "topics": [self.topic.id],
                "publishers": [self.user.id]
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            News.objects.filter(title=test_title).exists()
        )

    def test_update_news(self):
        test_title = "Test title edited"
        response = self.client.post(
            urls["NEWS_UPDATE_URL"],
            {
                "title": test_title,
                "content": self.news.title,
                "topics": [self.topic.id],
                "publishers": [self.user.id]
            }
        )
        News.objects.get(pk=1).refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            News.objects.get(pk=1).title,
            test_title
        )

    def test_update_redactor(self):
        test_username = "Edited"
        response = self.client.post(
            urls["REDACTOR_UPDATE_URL"],
            {
                "username": test_username,
                "years_of_experience": 10
            }
        )
        get_user_model().objects.get(pk=1).refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            get_user_model().objects.get(pk=1).username,
            test_username
        )

    def test_delete_news(self):
        response = self.client.post(
            urls["NEWS_DELETE_URL"]
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(News.objects.filter(id=1).exists())

    def test_delete_redactor(self):
        response = self.client.post(
            urls["REDACTOR_DELETE_URL"]
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(get_user_model().objects.filter(id=1).exists())
