from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .helpers import send_otp_to_phone
from .models import User

@api_view(['POST'])
def send_otp(request):
    data = request.data

    if data.get('phone_number') is None:
        return Response({
            'status':400,
            'message':'phone number is required'
        })

    elif data.get('password') is None:
        return Response({
            'status':400,
            'message':'passowrd is required'
        })
    else:
        user = User.objects.create(
        phone_number = data.get('phone_number'),
        otp = send_otp_to_phone(data.get('phone_number'))
        )
        user.set_password(data.get('set_password'))
        user.save()

        return Response({

            'status':200,
            'message':'otp sent successfully'
        })

@api_view(['POST'])
def verify_otp(request):
    data = request.data

    if data.get('phone_number') is None:
        return Response({
            'status':400,
            'message':'phone number is required'
        })

    if data.get('otp') is None:
        return Response({
            'status':400,
            'message':'otp is required'
        })
    else:
        try:
            user_obj = User.objects.get(phone_number = data.get('phone_number'))
        except Exception as e:
            return Response({
                'status':400,
                'message':'Invalid phone number'
            })
        
        if user_obj.otp == data.get('otp'):
            user_obj.Is_phone_verified = True
            user_obj.save()
            return Response({
                'status':200,
                'message':'otp verified successfully'
            })
        else:
            return Response({
                'status':400,
                'message':'Invalid otp'
            })