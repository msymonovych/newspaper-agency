from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic

from newspaper.forms import NewsForm, RedactorCreationForm
from newspaper.models import News


class NewsListView(generic.ListView):
    model = News
    paginate_by = 10


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
    model = get_user_model()
    paginate_by = 10


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
