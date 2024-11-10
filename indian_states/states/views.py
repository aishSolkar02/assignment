# states/views.py
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import State
from .forms import StateForm

class StateListView(ListView):
    model = State
    template_name = 'states/state_list.html'
    context_object_name = 'states'

class StateDetailView(DetailView):
    model = State
    template_name = 'states/state_detail.html'
    context_object_name = 'state'

class StateCreateView(CreateView):
    model = State
    template_name = 'states/state_form.html'
    form_class = StateForm
    success_url = reverse_lazy('state_list')

class StateUpdateView(UpdateView):
    model = State
    template_name = 'states/state_form.html'
    form_class = StateForm
    success_url = reverse_lazy('state_list')

class StateDeleteView(DeleteView):
    model = State
    template_name = 'states/state_confirm_delete.html'
    success_url = reverse_lazy('state_list')
