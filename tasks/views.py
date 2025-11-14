from django.shortcuts import render, redirect
from django.db.models import Count, Q
from django.core.paginator import Paginator
from datetime import date

from .models import Task, Category
from .forms import TaskForm


def task_list(request):
    # 1. Read filter from URL
    status = request.GET.get('status')
    query = request.GET.get('query')

    # 2. Base queryset
    tasks = Task.objects.all().order_by('deadline')

    # 3. Search filter
    if query:
        tasks = tasks.filter(
            Q(title__icontains=query)
        )

    # 4. Status filter
    if status == "completed":
        tasks = tasks.filter(completed=True)

    if status == "pending":
        tasks = tasks.filter(completed=False)

    # 5. Pagination
    paginator = Paginator(tasks, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # 6. Category count (One-to-Many)
    categories = Category.objects.annotate(task_count=Count('task'))

    # 7. Send to template
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'filter_status': status,   # <-- needed for pagination links
        'today': date.today(),
        'query': query,
    }

    return render(request, "tasks/task_list.html", context)



def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, "tasks/add_task.html", {'form': form})
