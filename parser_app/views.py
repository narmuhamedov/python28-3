from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView, FormView
from . import models, forms, parser


class FilmListView(ListView):
    model = models.TvParser
    template_name = "film_list.html"

    def get_queryset(self):
        return models.TvParser.objects.all()


class ParserFormView(FormView):
    template_name = "parser_film.html"
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse("<h1>Данные взяты ........</h1>")

        else:
            return super(ParserFormView).post(*args, **kwargs)


#
# class SearchParse(ListView):
# 	template_name = 'film_list.html'
# 	context_object_name = 'films'
# 	paginate_by = 5
#
# 	def get_queryset(self):
# 		return models.TvParser.objects.filter(title_icontains=self.request.GET.get("parse"))
# 	def get_context_data(self, *, object_list=None, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context['parse'] = self.request.GET.get("parse")
# 		return context
