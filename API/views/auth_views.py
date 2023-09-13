from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from API.serializers import LoginSerializer, RegisterSerializer


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "data": serializer.data,
                    "message": "Cuenta creada exitosamente",
                    "status": "ok",
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"error": serializer.errors, "status": "failed"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
