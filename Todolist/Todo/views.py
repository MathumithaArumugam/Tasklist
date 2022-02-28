
from django.shortcuts import render,redirect
from django.http import HttpResponse,QueryDict
from django.contrib import messages
from Todo.models import todo
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt
def apihandler(request,dataid=None,operation=None):
    if (dataid == None and operation == None):
        pass
    elif (operation == "PUT" and dataid == None):
        data=request.GET if request.method == "GET" else request.POST
        print(data)
        TName=data["tname"]
        TTime=data["ttime"]
        s=todo(TaskName=TName,TaskTime=TTime,CompletionStatus=False)
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
        for stu in todo.objects.all().iterator():
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


