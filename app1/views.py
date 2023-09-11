from django.shortcuts import render,get_object_or_404
from .models import InfoModel
from .serializers import InfoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

class AllInfoView(APIView):
    def get(self,request):
        all_info = InfoModel.objects.all()
        serializer = InfoSerializer(all_info,many=True)
        return Response(serializer.data)

class DetailInfoView(APIView):
    def get(self,request,*args,**kwargs):
        info = get_object_or_404(InfoModel,id = kwargs['info_id'])
        serializer = InfoSerializer(info)
        return Response(serializer.data)
    
class UpdateInfoView(APIView):
    def patch(self,request,*args,**kwargs):
        info = get_object_or_404(InfoModel,id=kwargs['info_id'])
        serializer = InfoSerializer(info,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
class CreateInfoView(APIView):
    def post(self,request):
        serializer = InfoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
class DeleteInfoView(APIView):
    def delete(self,*args,**kwargs):
        info =get_object_or_404(InfoModel,id=kwargs['info_id'])

        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class Find_H_View(APIView):
    def get(self,request,*args,**kwargs):
        data = 'Hilola'
        info = InfoModel.objects.filter(name= data)
        serializer = InfoSerializer(info,many =True)
        return Response(serializer.data) 
        

    
        
    
    