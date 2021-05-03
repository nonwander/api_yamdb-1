from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

#from allauth.account.views import confirm_email
#from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_users_auth.urls')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('api.urls')),
    path('api/', include('titles.urls')),
]
