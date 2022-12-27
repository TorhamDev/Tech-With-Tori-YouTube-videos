from django.shortcuts import render
from Bug.serializer import AdminsListSerializer
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from Bug.models import Admins


class AdminsList(ListAPIView):
    serializer_class = AdminsListSerializer
    queryset = Admins.objects.all()


class CheckAccess(APIView):
    def get(self, request, user_pk, format=None):

        admin_data = Admins.objects.get(pk=user_pk)
        
        if admin_data.access_level == "l":
            return Response({
                "access_level":admin_data.access_level,
                "message":"You don't have access",
            })
        elif admin_data.access_level == "m":
            return Response({
                "access_level":admin_data.access_level,
                "message":"You have some access",
            })
        elif admin_data.access_level == "h":
            return Response({
                "access_level":admin_data.access_level,
                "message":"Welcome dear Admin!",
            })
        else:
            return Response({
                "access_level":admin_data.access_level,
                "message":"Invalid admin access_level",
            })


class ChangeAccess(APIView):
    def get(self, request, user_pk, access_level, format=None):

        admin_data = Admins.objects.get(pk=user_pk)
        admin_data.access_level = access_level
        admin_data.save()

        return Response({"statute":"ok"})
