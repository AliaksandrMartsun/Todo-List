from django.shortcuts import render

from django.views.generic import ListView
from .models import Todo, Category


class TodoView(ListView):
    model = Todo
    queryset = Todo.objects.filter(draft=False)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["categories"] = Category.objects.all
        return context
