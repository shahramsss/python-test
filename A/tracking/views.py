from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .mixins import LoggingMixin


class HomeView(LoggingMixin, APIView):
    # logging_methods = ['GET' , 'POST']

    def should_log(self, response, request):
        return response.status_code > 400

    def get(self, request):
        return Response("hello , hi ")
