from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from .models import Passion, IdealMatch, Gender, MaritalStatus, Education, BodyType, UserMedia
from .serializers import RegisterSerializer, UserDetailsSerializer, PassionSerializers, IdealMatchSerializers, \
    GenderSerializers, MaritalStatusSerializers, EducationSerializers, BodyTypeSerializers, UserMediaSerializers, \
    UserMediaPostSerializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class RegistrationsAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Registrations Successfully !", "is_status": True, 'data': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response({'msg': "Email Already Exists !", "is_status": False, 'errors': serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)


class UserDetailsAPI(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer


class UserUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer


class PassionAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Passion.objects.all()
    serializer_class = PassionSerializers


class IdealMatchAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = IdealMatch.objects.all()
    serializer_class = IdealMatchSerializers


class GenderAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Gender.objects.all()
    serializer_class = GenderSerializers


class MaritalStatusAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = MaritalStatus.objects.all()
    serializer_class = MaritalStatusSerializers


class EducationAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Education.objects.all()
    serializer_class = EducationSerializers


class BodyTypeAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = BodyType.objects.all()
    serializer_class = BodyTypeSerializers


class UserMediaAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        queryset = UserMedia.objects.filter(Q(user=user)).distinct()
        serializer = UserMediaSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserMediaPostAPIView(generics.ListCreateAPIView):
    serializer_class = UserMediaPostSerializers
    queryset = UserMedia.objects.all()


class UserMediaUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserMediaSerializers
    queryset = UserMedia.objects.all()


class UserMediaDeleteAPIView(generics.DestroyAPIView):
    serializer_class = UserMediaSerializers
    queryset = UserMedia.objects.all()


class UserMediaPatchAPIView(generics.RetrieveAPIView):
    serializer_class = UserMediaSerializers
    queryset = UserMedia.objects.all()
