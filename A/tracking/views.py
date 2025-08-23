from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .mixins import LoggingMixin


class HomeView(LoggingMixin, APIView):
    def get(self, request):
        return Response("hello , hi ")
