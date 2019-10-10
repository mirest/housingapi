from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serializers import LoginSerializer, RegistrationSerializer
from .models import User


class RegistrationAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()


class LoginAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)
