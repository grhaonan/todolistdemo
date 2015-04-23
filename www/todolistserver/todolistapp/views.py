#!/usr/bin/python
#coding=utf-8
#-*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import Http404
from models import Todo
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# Define home page 



def todolist(request):
	todolist=Todo.objects.filter(flag=1)
	finishtodos=Todo.objects.filter(flag=0)
	return render_to_response('ToDolistHome.html',{'todolist':todolist,'finishtodos':finishtodos},context_instance=RequestContext(request))
    



def todoredo(request, id=''):
    todo = Todo.objects.get(id=id)
    if todo.flag == '0':
        todo.flag = '1'
        todo.save()
        return HttpResponseRedirect('/redirforredo/')
    todolist = Todo.objects.filter(flag=1)
    return render_to_response('simpleTodo.html', {'todolist': todolist},
        context_instance=RequestContext(request))



def todofinish(request, id=''):
    todo = Todo.objects.get(id=id)
    if todo.flag == '1':
        todo.flag = '0'
        todo.save()
        return HttpResponseRedirect('/redirforfinish/')
    todolist = Todo.objects.filter(flag=1)
    return render_to_response('simpleTodo.html', {'todolist': todolist},
        context_instance=RequestContext(request))


def tododelete(request, id=''):
    try:
        todo = Todo.objects.get(id=id)
    except Exception:
            raise Http404
    if todo:
        todo.delete()
        return HttpResponseRedirect('/redirfordelete/')
    todolist = Todo.objects.filter(flag=1)
    return render_to_response('simpleTodo.html', {'todolist': todolist},
        context_instance=RequestContext(request))


def addTodo(request):
    if request.method == 'POST':
        atodo = request.POST['todo']
        priority = request.POST['priority']
        user = User.objects.get(id='1')
        todo = Todo(user=user, todo=atodo, priority=priority, flag='1')
        todo.save()
        todolist = Todo.objects.filter(flag='1')
        finishtodos = Todo.objects.filter(flag=0)
        return render_to_response('showtodo.html',
            {'todolist': todolist, 'finishtodos': finishtodos},
            context_instance=RequestContext(request))
    else:
        todolist = Todo.objects.filter(flag=1)
        finishtodos = Todo.objects.filter(flag=0)
        return render_to_response('simpleTodo.html',
            {'todolist': todolist, 'finishtodos': finishtodos})


def updatetodo(request, id=''):
    if request.method == 'POST':
        try:
            todo = Todo.objects.get(id=id)
        except Exception:
            return HttpResponseRedirect('/todos/')
        atodo = request.POST['todo']
        priority = request.POST['priority']
        todo.todo = atodo
        todo.priority = priority
        todo.save()
        return HttpResponseRedirect('/redirupdate/')

    else:
        try:
            todo = Todo.objects.get(id=id)
        except Exception:
            raise Http404
        return render_to_response('updatatodo.html', {'todo': todo},
            context_instance=RequestContext(request))

