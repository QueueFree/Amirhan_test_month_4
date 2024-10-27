from django.shortcuts import render
from tasks.models import *
from django.db.models import Q
from tasks.forms import *


def based_view(request):
    if request.method == 'GET':
        return render(request, 'base.html')


def task_list_view(request):
    if request.method == "GET":
        search = request.GET.get('search', None)
        tag = request.GET.getlist('tag', None)

        tasks = Task.objects.all()

        if search:
            tasks = tasks.filter(
                Q(title__icontains=search) | Q(description__icontains=search))

        if tag:
            tasks = tasks.filter(tags__id__in=tag)

        form = SearchForm
        return render(request, 'list_view.html', {
            'tasks': tasks,
            'form': form,
        })


def task_detail(request, task_id):
    if request.method == "GET":
        task = Task.objects.get(id=task_id)
        return render(request, 'task_detail.html', {'task': task})

