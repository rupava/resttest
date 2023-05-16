from django.shortcuts import render,get_object_or_404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from .models import *

@login_required(login_url='/login/')
def todo_index(request):

    if request.method == 'POST':
        # print(list(request.POST.items()))
        task_name = request.POST.get('list_headding')
        
        data = Task_List()
        data.user = request.user
        data.task_title = task_name
        
        data.save()

    task_list = Task_List.objects.filter(user=request.user)

    context = {
        'data': task_list
    }
    return render(request, 'html/todo/todo_index.html', context)

# @login_required(login_url='/login/')
# def todo_edit(request):
#     slug = request.GET["pk"]
#     try:
#         task_id = Task_List.objects.get(id = slug, user = request.user)
#         dump = Tasks.objects.get(task_list = task_id) 
#     except dump.DoesNotExist:
#         dump = None

#     if task_id != "" or task_id != "null":
#         context = {
#             'data':task_id,
#             'dump':dump
#         }
#         return render(request, 'html/todo/edit.html', context)
    
#     raise PermissionDenied()

@login_required(login_url='/login/')
def todo_edit(request):

    slug = request.GET["pk"]

    task_id = Task_List.objects.get(id = slug, user = request.user)

    taskObj = Tasks.objects.filter(task_list = task_id.id) 
    print("---->",taskObj)
    if task_id != "" or task_id != "null":
        context = {
            'data':task_id
        }
        return render(request, 'html/todo/edit.html', context)
    
    raise PermissionDenied()