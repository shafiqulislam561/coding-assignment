from django.shortcuts import render

# Create your views here.
from app import serialize
from app.models import Parent, Child
from app.serialize import ParentSerializer, ChildSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class ParentListView(APIView):

    def get(self,request):
        parentObj=Parent.objects.all()
        parentSerializeObj=ParentSerializer(parentObj,many=True)
        return Response(parentSerializeObj.data)

    
class ParentCreate(APIView):

    def post(self,request):
        serializeobj=ParentSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)    

class ParentUpdate(APIView):

    def post(self,request,pk):
        try:
            parentObj=Parent.objects.get(pk=pk)
        except:
            return Response("Not Found in Database")

        serializeobj=ParentSerializer(parentObj,data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)


class ParentDelete(APIView):

    def post(self,request,pk):
        try:
            parentObj=Parent.objects.get(pk=pk)
        except:
            return Response("Not Found in Database")
        parentObj.delete()
        return Response(200)

class ChildListView(APIView):

    def get(self,request):
        childObj=Child.objects.all()
        childSerializeObj=ChildSerializer(childObj,many=True)
        return Response(childSerializeObj.data)

    
class ChildCreate(APIView):

    def post(self,request):
        serializeobj=ChildSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)    

class ChildUpdate(APIView):

    def post(self,request,pk):
        try:
            childObj=Child.objects.get(pk=pk)
        except:
            return Response("Not Found in Database")

        serializeobj=ChildSerializer(childObj,data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)


class ChildDelete(APIView):

    def post(self,request,pk):
        try:
            childObj=Child.objects.get(pk=pk)
        except:
            return Response("Not Found in Database")
        childObj.delete()
        return Response(200)