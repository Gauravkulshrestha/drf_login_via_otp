from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def send_otp(request):
    data = request.data

    if data.get('phone_number') is None:
        return Response({

            'status':400,
            'message':'phone number is required'
        })
    if data.get('password') is None:
        return Response({

            'status':400,
            'message':'passowrd is required'
        })
