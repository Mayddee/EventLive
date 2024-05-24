from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')
        
        #already set function to check hashed password
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        #for creating tokens
        payload = {
            'id': user.id,
            #time for session be expired
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            #date when token is created
            'iat': datetime.datetime.utcnow()     
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        #to set cookies with http only 
        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'jwt': token
            }

        return response


class UserView(APIView):

    #to get user cookie
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        # user = User.objects.filter(id=payload['id']).first()
        user = User.objects.filter(id=payload['id']).first()

        serializer = UserSerializer(user)

        return Response(serializer.data)
    
class LogoutView(APIView):
    #delete cookie of jwt to logout
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
