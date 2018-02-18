

# Create your views here.
# def score_list(request):
    # scores = Score.objects.all().order_by('call_number')    
    # return render(request, 'performance_collection/score_list.html', {'scores': scores})
 
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import Score
from haystack.generic_views import SearchView
from haystack import forms
from haystack.forms import SearchForm

class ScoreSearchView(SearchView):
  template_name = 'search.html'
  def get_queryset(self):
    queryset = super(ScoreSearchView, self).get_queryset()
    return queryset.all()

  def get_context_data(self, *args, **kwargs):
    context = super(ScoreSearchView, self).get_context_data(*args, **kwargs)
    return context


def score_listview(request,):
    template_name = 'performance_collection/score_list.html'
    queryset = Score.objects.all()
    context = {
    }
    return render(request, template_name, context)

class ScoreListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = Score.objects.filter(
                    Q(collection__iexact=slug) |
                    Q(collection__icontains=slug)
                )
        else:
            queryset = Score.objects.all()
        return queryset
class ScoreDetailView(DetailView):
    queryset = Score.objects.all()

class OrchestralListView(ListView):
        def get_queryset(self):
            slug = self.kwargs.get("slug")
            if slug:
                queryset = Score.objects.filter(
                        Q(collection__iexact=slug) |
                        Q(collection__icontains=slug)
                    )
            else:
                queryset = Score.objects.filter(collection__iexact="Orchestral")
            return queryset

class ChoralListView(ListView):
        def get_queryset(self):
            slug = self.kwargs.get("slug")
            if slug:
                queryset = Score.objects.filter(
                        Q(collection__iexact=slug) |
                        Q(collection__icontains=slug)
                    )
            else:
                queryset = Score.objects.filter(collection__iexact="Choral")
            return queryset
class BandListView(ListView):
        def get_queryset(self):
            slug = self.kwargs.get("slug")
            if slug:
                queryset = Score.objects.filter(
                        Q(collection__iexact=slug) |
                        Q(collection__icontains=slug)
                    )
            else:
                queryset = Score.objects.filter(collection__iexact="Concert Band")
            return queryset

