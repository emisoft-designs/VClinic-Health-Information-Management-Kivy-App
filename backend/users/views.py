# views.py

from django.contrib.auth import get_user_model, authenticate, login, logout
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework import generics, status, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .privileges import PrivilegeManager
from .serializers import (
    UserLoginSerializer, 
    UserRegisterSerializer, 
    PatientSerializer
)
from .models import Patient

CustomUser = get_user_model()

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            print(f"backend - serializer: {serializer.data}")
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            print(f"Username: {username}, Password: {password}")

            user = authenticate(request, username=username, password=password)
            
            if user:
                token, created = Token.objects.get_or_create(user=user)
                response = {
                    'success': True,
                    'username': user.username,
                    'email': user.email,
                    'token': token.key, 
                    'detail': 'Login Successful' 
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'detail':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({"success":True, "detail": "Logout successful"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e), 'detail':'Error Occured!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserRegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):

        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            print(serializer.data)

            token = Token.objects.get(
                user=CustomUser.objects.get(
                    username=serializer.data['username'])).key
            
            response = {
                'success': True,
                'user': serializer.data,
                'token': token
            }
            return Response(response, status=status.HTTP_200_OK)
        raise ValidationError(
            serializer.errors, code=status.HTTP_406_NOT_ACCEPTABLE
        )

class RegisterPatientView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request): 
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RegisterStaffView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [IsAuthenticated]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [IsAuthenticated]

class AssignPrivilegesView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        user = self.get_object()
        privilege = request.data.get('privilege')
        if not PrivilegeManager.has_privilege(request.user, 'assign_privileges'):
            return Response(status=status.HTTP_403_FORBIDDEN)
        if PrivilegeManager.assign_privilege(user, privilege):
            return Response({'status': 'privilege assigned'})
        return Response({'status': 'failed to assign privilege'}, status=status.HTTP_400_BAD_REQUEST)

class PatientListView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]
