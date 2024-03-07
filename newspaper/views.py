from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic

from newspaper.forms import (
    NewsForm,
    RedactorCreationForm,
    NewsSearchForm, RedactorSearchForm
)
from newspaper.models import News


class NewsListView(generic.ListView):
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title")
        context["search_form"] = NewsSearchForm(
            initial={"title": title}
        )
        return context

    def get_queryset(self):
        queryset = News.objects.all()
        form = NewsSearchForm(self.request.GET)
        if form.is_valid():
            queryset = queryset.filter(
                title__icontains=form.cleaned_data["title"]
            )
        return queryset


class NewsDetailView(generic.DetailView):
    model = News


class NewsCreateView(generic.CreateView):
    model = News
    form_class = NewsForm
    success_url = reverse_lazy("newspaper:news-list")


class NewsUpdateView(generic.UpdateView):
    model = News
    form_class = NewsForm
    success_url = reverse_lazy("newspaper:news-list")


class NewsDeleteView(generic.DeleteView):
    model = News
    success_url = reverse_lazy("newspaper:news-list")


class RedactorListView(generic.ListView):
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.GET.get("username")
        context["search_form"] = RedactorSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = get_user_model().objects.all()
        form = RedactorSearchForm(self.request.GET)
        if form.is_valid():
            queryset = queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class RedactorDetailView(generic.DetailView):
    model = get_user_model()


class RedactorCreateView(generic.CreateView):
    model = get_user_model()
    form_class = RedactorCreationForm
    success_url = reverse_lazy("newspaper:redactor-list")


class RedactorUpdateView(generic.UpdateView):
    model = get_user_model()
    form_class = RedactorCreationForm
    success_url = reverse_lazy("newspaper:redactor-list")


class RedactorDeleteView(generic.DeleteView):
    model = get_user_model()
    success_url = reverse_lazy("newspaper:news-list")
