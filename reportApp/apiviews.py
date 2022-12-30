from .models import Report
from .serializers import ReportSerializer, CustomUserSerializer

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import authenticate, logout

class ReportViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def get_queryset(self):
        return Report.objects.filter(user=self.request.user)


class CustomUserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = CustomUserSerializer

class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({"success": "Successfully logged out."}, status=status.HTTP_200_OK)