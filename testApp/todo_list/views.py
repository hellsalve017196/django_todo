from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json


# loading template
def home(request):
    return render(request,'home.html',{'title' : 'todo_list'})


@csrf_exempt
def getting_in(request):
    data = {}

    packet = json.loads(request.POST.get("login"))
    Queryset = User.objects.filter(email=packet["email"],password=packet["password"])

    if Queryset.count() == 1 :
        data = {"status" : "success","data" : list(Queryset.values())}
    else :
        data = {"status" : "error","message" : "Invalid Username or  Password"}

    return HttpResponse(json.dumps(data),content_type="application/json")

@csrf_exempt
def sign_up(request):
    data = {}

    packet = json.loads(request.POST['sign_up'])

    # checking email available or not
    if (User.objects.filter(email=packet["email"])):
        data = {'status' : 'error','message' : 'Email Already exists'}
    else:
        try:
            if User.objects.create(full_name = packet["full_name"],email = packet["email"],password = packet["password"]):
                data = {'status' : 'success','message' : 'Successfully signed up'}
            else:
                data = {'status' : 'error','message' : 'Error from server'}
        except Exception as e:
            data = {'status' : 'error','message' : str(e)}


    return HttpResponse(json.dumps(data),content_type="application/json")

# viewing current users
def user_list(request):
    data = {}

    #get request
    user_id = request.GET.get("u_id")

    # getting users beside self
    user_data = User.objects.filter(~Q(u_id=user_id)).values('email','full_name')
    packet = []

    for temp in user_data:
        packet.append(temp)

    data = {"status" : "success","data" : packet}

    return HttpResponse(json.dumps(data),content_type="application/json")


# insert a todo
@csrf_exempt
def create_todo(request):
    data = {}

    #post request
    todo_list = json.loads(request.POST.get("todo"))

    if(Todo.objects.filter(t_title=todo_list["t_title"])):
        data = {'status' : 'error','message' : 'Already Added to the list'}
    else:
        if(Todo.objects.create(u_id=todo_list['u_id'],t_title=todo_list['t_title'],t_date=todo_list['t_date'],t_priority=todo_list['t_priority'],t_choice=todo_list['t_choice'])):
            data = {'status' : 'success','message' : 'successfully added'}
        else:
            data = {'status' : 'error','message' : 'error from server'}

    return HttpResponse(json.dumps(data),content_type="application/json")

# displaying all the todo for a user
def todo_by_user(request):
    data = {}

    #get request
    user_id = request.GET.get('u_id')
    todo_query = Todo.objects.filter(u_id=user_id)

    if todo_query.count() > 0:
        todo_list = list(todo_query.values())
        data = {"status" : "success","data" : todo_list}
    else:
        data = {"status" : "error","message" : "no todo has been added"}

    return HttpResponse(json.dumps(data),content_type="application/json")

# update todolist for a user
@csrf_exempt
def update_todo(request):
    data = {}

    #post request
    todo = json.loads(request.POST.get('todo'))

    todoQuery = Todo.objects.filter(t_id=todo["t_id"],u_id=todo["u_id"])

    if todoQuery.count() > 0:
        try:
            if Todo.objects.filter(t_title=todo["t_title"]).count() == 0:
                if todoQuery.update(t_title=todo["t_title"],t_date=todo["t_date"],t_priority=todo["t_priority"],t_choice=todo["t_choice"]):
                    data = {"status" : "success","message" : "successfully updated"}
                else:
                    data = {"status" : "error","message" : "Error from server"}
            else:
                data = {"status" : "error","message" : "already in the list"}
        except Exception as e:
            data = {"status" : "error","message" : str(e)}
    else:
        data = {"status" : "error","message" : "invalid todo"}

    return HttpResponse(json.dumps(data),content_type="application/json")

#delete from todo
def delete_todo(request):
    data = {}

    # get request
    user_id = request.GET.get('u_id')
    task_id = request.GET.get('t_id')

    QuerySet = Todo.objects.filter(u_id=user_id,t_id=task_id)

    if QuerySet.count() > 0:
        if QuerySet.delete():
            data = {"status" : "success","message" : "Successfully Removed"}
        else :
            data = {"status" : "error","message":"Error from Serverr"}
    else:
        data = {"status" : "error","message":"invalid todo and user"}

    return HttpResponse(json.dumps(data),content_type="application/json")