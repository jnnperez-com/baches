from django.shortcuts import render

from .models import Reporte
from rest_framework import viewsets
from .serializers import ReporteSerializer, UserSerializer, SetPassword
#restgramework
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import  status
from rest_framework.decorators import detail_route


class Userviewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    lookup_field = 'id'

    @detail_route(methods=['post'])
    def set_password(self, request, id=None):
        user = self.get_object()
        serializer = SetPassword(data=request.DATA)
        if user == request.user:
            if serializer.is_valid():
                user.set_password(serializer.data['password1'])
                user.save()
                return Response({'status':'Cambio realizado con exito'})
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Este no es su usuario'},status=status.HTTP_403_FORBIDDEN)


class ReporteViewSet(viewsets.ModelViewSet):
    serializer_class = ReporteSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Reporte.objects.all()
    lookup_field = 'id'


    def list(self, request, *args, **kwargs):
        print(request.user)
        return super(ReporteViewSet, self).list(request, *args, **kwargs)


    def perform_create(self, serializer):
       # print(self.get_object())
        serializer.save(owner=self.request.user,)

