from django.urls import path
from account.views import RegisterView, RegistrationsAPIView, UserDetailsAPI, UserUpdateAPIView, PassionAPIView, \
    IdealMatchAPIView, GenderAPIView, MaritalStatusAPIView, EducationAPIView, BodyTypeAPIView, UserMediaAPIView, \
    UserMediaPostAPIView, UserMediaPatchAPIView, UserMediaUpdateAPIView, UserMediaDeleteAPIView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('v1/registrations/', RegistrationsAPIView.as_view(), name='RegistrationsAPIView'),

    path('user/<uuid:pk>/patch/', UserDetailsAPI.as_view(), name='UserDetailsAPI'),
    path('user/<uuid:pk>/update/', UserUpdateAPIView.as_view(), name='UserUpdateAPIView'),

    path('passion/get/', PassionAPIView.as_view(), name='PassionAPIView'),
    path('ideal/match/get/', IdealMatchAPIView.as_view(), name='IdealMatchAPIView'),
    path('gender/get/', GenderAPIView.as_view(), name='GenderAPIView'),
    path('marital/status/get/', MaritalStatusAPIView.as_view(), name='MaritalStatusAPIView'),
    path('education//get/', EducationAPIView.as_view(), name='EducationAPIView'),
    path('body/type/get/', BodyTypeAPIView.as_view(), name='BodyTypeAPIView'),

    path('user/media/get/', UserMediaAPIView.as_view(), name='UserMediaAPIView'),
    path('user/media/post/', UserMediaPostAPIView.as_view(), name='UserMediaPostAPIView'),
    path('user/media/<uuid:pk>/patch/', UserMediaPatchAPIView.as_view(), name='UserMediaPatchAPIView'),
    path('user/media/<uuid:pk>/update/', UserMediaUpdateAPIView.as_view(), name='UserMediaUpdateAPIView'),
    path('user/media/<uuid:pk>/delete/', UserMediaDeleteAPIView.as_view(), name='UserMediaDeleteAPIView'),

]