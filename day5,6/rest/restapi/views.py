from django.shortcuts import render,redirect
from django.http import HttpResponse,QueryDict
from django.contrib import messages
from restapi.models import student
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
        SName=data["sname"]
        RollNo=data["rollno"]
        TGrade=data["grade"]
        PhoneNo=data["phoneno"]
        FName=data["fname"]
        MName=data["mname"]
        TAddress=data["address"]
        s=student(StudentName=SName,RollNumber=RollNo,Grade=TGrade,PhoneNumber=PhoneNo,FatherName=FName,MotherName=MName,Address=TAddress)
        s.save()
        return HttpResponse("Ok " + str(s.id))
    elif (operation == "POST" and dataid != None):
        data=request.GET if request.method == "GET" else request.POST
        print(data)
        SName=data["sname"]
        RollNo=data["rollno"]
        TGrade=data["grade"]
        PhoneNo=data["phoneno"]
        FName=data["fname"]
        MName=data["mname"]
        TAddress=data["address"]
        s=student.objects.get(id=dataid)
        s.StudentName=SName
        s.RollNumber=RollNo
        s.Grade=TGrade
        s.PhoneNumber=PhoneNo
        s.FatherName=FName
        s.MotherName=MName
        s.Address=TAddress
        s.save()
        return HttpResponse("Ok " + str(s.id))

    elif(operation=="GET" and dataid==None):
        wholejson="["
        ojson=[]
        for stu in student.objects.all().iterator():
            tjson="{"
            tjson+="\'ID\': \'"+str(stu.id)+"\',"
            tjson+="\'StudentName\': \'"+stu.StudentName+"\',"
            tjson+="\'RollNumber\': \'"+stu.RollNumber+"\',"
            tjson+="\'Grade\': \'"+stu.Grade+"\',"
            tjson+="\'PhoneNumber\': \'"+stu.RollNumber+"\',"
            tjson+="\'FatherName\': \'"+stu.FatherName+"\',"
            tjson+="\'MotherName\': \'"+stu.MotherName+"\',"
            tjson+="\'Address\': \'"+stu.Address+"\'"
            tjson+="}"
            ojson.append(tjson)

        wholejson+=",".join(ojson)+"]"
        return(HttpResponse(wholejson,content_type="application/json"))
    elif(operation=="GET" and dataid!=None):
        wholejson="["
        stu=student.objects.get(id=dataid)
        tjson="{"
        tjson+="\'ID\': \'"+str(stu.id)+"\',"
        tjson+="\'StudentName\': \'"+stu.StudentName+"\',"
        tjson+="\'RollNumber\': \'"+stu.RollNumber+"\',"
        tjson+="\'Grade\': \'"+stu.Grade+"\',"
        tjson+="\'PhoneNumber\': \'"+stu.RollNumber+"\',"
        tjson+="\'FatherName\': \'"+stu.FatherName+"\',"
        tjson+="\'MotherName\': \'"+stu.MotherName+"\',"
        tjson+="\'Address\': \'"+stu.Address+"\'"
        tjson+="}"
        wholejson+=tjson+"]"
        return(HttpResponse(wholejson,content_type="application/json"))

    elif(operation=="DELETE" and dataid!=None):
        stu=student.objects.get(id=dataid)
        stu.delete()
        return(HttpResponse("OK"))

