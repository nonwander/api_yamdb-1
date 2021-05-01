from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import UserViewSet, MyTokenObtainPairView, get_confirmation_code

API_VER = 'v1'


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path(f'{API_VER}/', include(router.urls)),
    path(f'{API_VER}/auth/email/',  get_confirmation_code, name='get_confirmation_code'),
    path(f'{API_VER}/auth/token/',
         MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'
         ),
    path(f'{API_VER}/token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'
         ),
]
