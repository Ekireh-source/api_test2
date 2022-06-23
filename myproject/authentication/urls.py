# from django.urls import path
# # from .views import RegistrationView
# from .apis import RegisterAPI, LoginAPI
# from knox import views as knox_views

# urlpatterns = [ 
#    # path('register', RegistrationView.as_view()),
#    # path('register/', RegisterAPI.as_view()),
#    # path('login/', LoginAPI.as_view()),
#    # path('logout/',knox_views.LogoutView.as_view()),
#    # path('logoutall/', knox_views.LogoutAllView.as_view()),
    
# ]

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)
from django.urls import path

from .import apis
from rest_framework_simplejwt.views import TokenVerifyView


urlpatterns = [
   path('register/', apis.RegisterApi.as_view(), name="register"),
   path('login/', apis.LoginApi.as_view(), name="login"),
   path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
   path('me/', apis.UserApi.as_view(), name="me"),
   path('logout/', apis.LogOutApi.as_view(), name="logout"),
]
