from django.urls import path

from newspaper import views


urlpatterns = [
    path("", views.NewsListView.as_view(), name="news-list"),
    path("news/create/", views.NewsCreateView.as_view(), name="news-create"),
    path("news/<int:pk>/", views.NewsDetailView.as_view(), name="news-detail"),
    path(
        "news/<int:pk>/update/",
        views.NewsUpdateView.as_view(),
        name="news-update"
    ),
    path(
        "news/<int:pk>/delete/",
        views.NewsDeleteView.as_view(),
        name="news-delete"
    ),
    path(
        "redactors/",
        views.RedactorListView.as_view(),
        name="redactor-list"
    ),
    path(
        "redactors/create/",
        views.RedactorCreateView.as_view(),
        name="redactor-create"
    ),
    path(
        "redactors/<int:pk>/",
        views.RedactorDetailView.as_view(),
        name="redactor-detail"
    ),
    path(
        "redactors/<int:pk>/update/",
        views.RedactorUpdateView.as_view(),
        name="redactor-update"
    ),
    path(
        "redactors/<int:pk>/delete/",
        views.RedactorDeleteView.as_view(),
        name="redactor-delete"
    ),
]

app_name = "newspaper"
