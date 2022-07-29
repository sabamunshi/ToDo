from django.http import HttpResponseRedirect
from django.shortcuts import render

from todoapp.models import TodoListItem

# Create your views here.
def todolistview(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items':all_todo_items})
  
def addtodoview(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deletetodoview(request, item):
    y = TodoListItem.objects.get(id= item)
    y.delete()
    return HttpResponseRedirect('/todo/')