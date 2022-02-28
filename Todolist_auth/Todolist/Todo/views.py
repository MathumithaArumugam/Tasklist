
from django.shortcuts import render,redirect
from django.http import HttpResponse,QueryDict
from django.contrib import messages
from Todo.models import todo,Users
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def authhandler(request,operation=None):
    if (operation == "LOGIN" ):
        if("userid" in request.session):
            return(redirect("/Login"))
        data=request.GET if request.method == "GET" else request.POST
        user=Users.objects.filter(UserName=data["username"],Password=data["password"])
        if(len(user)==0):
            return redirect("/Login")
        else:
            request.session["userid"]=user.first().id
            return redirect("/tasks",permanent=True)
    elif (operation == "REGISTER" ):
        if("userid" in request.session):
            return(redirect("/Login"))
        data=request.GET if request.method == "GET" else request.POST
        user=Users.objects.filter(UserName=data["username"])
        if(len(user)>0):
            return redirect("/Login")
        if(data["password"]==data['Confirm-password']):
            user=Users(UserName=data["username"],Password=data["password"])
            user.save()
            request.session["userid"]=user.id
            return redirect("/tasks",permanent=True)
        else:
            return redirect("/Login")
    elif (operation == "LOGOUT" ):
        if("userid" in request.session):
            del request.session["userid"]
        return redirect("/Login")

def defaultpage(request):
    if("userid" in request.session):
        return redirect("/tasks")
    else:
        return redirect("/Login")

@csrf_exempt
def apihandler(request,dataid=None,operation=None):
    if (dataid == None and operation == None):
        pass
    elif (operation == "PUT" and dataid == None):
        data=request.GET if request.method == "GET" else request.POST
        print(data)
        TName=data["tname"]
        TTime=data["ttime"]
        s=todo(TaskName=TName,TaskTime=TTime,UserId=request.session["userid"],CompletionStatus=False)
        s.save()
        return HttpResponse("Ok " + str(s.id))
    elif (operation == "POST" and dataid != None):
        data=request.GET if request.method == "GET" else request.POST
        print(data)
        s=todo.objects.get(id=dataid)
        if "tname" in data:
            TName=data["tname"]
            s.TaskName=TName
        if "ttime" in data:
            TTime=data["ttime"]
            s.TaskTime=TTime
        if "status" in data:
            Status=data["status"]
            s.CompletionStatus=Status
        s.save()
        return HttpResponse("Ok " + str(s.id))

    elif(operation=="GET" and dataid==None):
        wholejson="["
        ojson=[]
        for stu in todo.objects.filter(UserId=request.session["userid"]):
            tjson="{"
            tjson+="\"ID\": \""+str(stu.id)+"\","
            tjson+="\"TaskName\": \""+stu.TaskName+"\","
            tjson+="\"TaskTime\": \""+stu.TaskTime+"\","
            tjson+="\"CompletionStatus\": "+str(stu.CompletionStatus).lower()+""
            tjson+="}"
            ojson.append(tjson)

        wholejson+=",".join(ojson)+"]"
        return(HttpResponse(wholejson,content_type="application/json"))
    elif(operation=="GET" and dataid!=None):
        wholejson="["
        stu=todo.objects.get(id=dataid)
        tjson="{"
        tjson+="\"ID\": \""+str(stu.id)+"\","
        tjson+="\"TaskName\": \""+stu.TaskName+"\","
        tjson+="\"TaskTime\": \""+stu.TaskTime+"\","
        tjson+="\"CompletionStatus\": "+str(stu.CompletionStatus).lower()+""
        tjson+="}"
        wholejson+=tjson+"]"
        return(HttpResponse(wholejson,content_type="application/json"))

    elif(operation=="DELETE" and dataid!=None):
        stu=todo.objects.get(id=dataid)
        stu.delete()
        return(HttpResponse("OK"))


