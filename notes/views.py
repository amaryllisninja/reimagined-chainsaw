from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.edit import DeleteView

from .forms import NotesForm
from .models import Notes

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = "notes/notes_delete.html"

def add_like_view(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    note.likes += 1
    note.save()
    return HttpResponseRedirect(reverse("notes.detail", args=(pk,)))