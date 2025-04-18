from .models import Publication
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import ( 
                                        LoginRequiredMixin,
                                        UserPassesTestMixin
                                        )

# Create your views here.

class PublicationListView(ListView):
    model = Publication
    template_name = 'publication-list.html'
    
class PublicationDetailView(LoginRequiredMixin, DetailView):
    model = Publication
    template_name = 'publication-detail.html'
    
class PublicationCreateView(LoginRequiredMixin, CreateView):
    model = Publication
    template_name = 'publication-create.html'
    fields = ['title', 'body', 'author']
    
class PublicationUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Publication
    template_name = 'publication-update.html'
    fields = ['title', 'body']
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class PublicationDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Publication
    template_name = 'publication-delete.html'
    success_url = reverse_lazy('publication-list')
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user