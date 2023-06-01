from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic

#не полная информация
class PersonView(generic.ListView):
    template_name = 'meeting/meeting.html'
    queryset = models.Meeting.objects.all()

    def get_queryset(self):
        return models.Meeting.objects.all()


# def person_view(request):
#     persons = models.Meeting.objects.all()
#     return render(request, 'meeting/meeting.html', {'persons': persons})
#

#детальная информация
class PersonDetailView(generic.DetailView):
    template_name = 'meeting/meeting_detail.html'

    def get_object(self, **kwargs):
        person_id = self.kwargs.get('id')
        return get_object_or_404(models.Meeting, id=person_id)
# def person_detail_view(request, id):
#     person_id = get_object_or_404(models.Meeting, id=id)
#     return render(request, 'meeting/meeting_detail.html', {'person_id': person_id})


#создание анкеты #POST GET DELETE PUT
class CreatePersonView(generic.CreateView):
    template_name = 'crud/create_person.html'
    form_class = forms.MeetingForm
    queryset = models.Meeting.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreatePersonView, self).form_valid(form=form)


# def create_person_view(request):
#     method = request.method
#     if method == "POST":
#         form = forms.MeetingForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Анкета успешно добавлена!")
#     else:
#         form = forms.MeetingForm()
#     return render(request, "crud/create_person.html", {"form": form})

#удаление анкеты
class DeletePersonView(generic.DeleteView):
    template_name = 'crud/confirm_delete.html'
    success_url = '/'

    def get_object(self, **kwargs):
        person_id = self.kwargs.get('id')
        return get_object_or_404(models.Meeting, id=person_id)

# def delete_person_view(request, id):
#     person_id = get_object_or_404(models.Meeting, id=id)
#     person_id.delete()
#     return HttpResponse("Анкета удалена")


#Обновление
class UpdatePersonView(generic.UpdateView):
    template_name = 'crud/update_person.html'
    form_class = forms.MeetingForm
    success_url = '/'

    def get_object(self, **kwargs):
        person_id = self.kwargs.get('id')
        return get_object_or_404(models.Meeting, id=person_id)

    def form_valid(self, form):
        return super(UpdatePersonView, self).form_valid(form=form)

# def update_person_view(request, id):
#     person_id = get_object_or_404(models.Meeting, id=id)
#     if request.method == "POST":
#         form = forms.MeetingForm(instance=person_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Данные успешно обновлены')
#     else:
#         form = forms.MeetingForm(instance=person_id)
#     context = {
#         "form": form,
#         "person_id": person_id
#     }
#     return render(request, "crud/update_person.html", context)
class Search(generic.ListView):
    template_name = 'meeting/meeting.html'
    context_object_name = 'person'
    paginate_by = 5

    def get_queryset(self):
        return models.Meeting.objects.filter(name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

