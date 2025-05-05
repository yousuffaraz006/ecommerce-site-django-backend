from rest_framework_simplejwt.views import TokenRefreshView
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from base.views import *
from backend.settings import BASE_DIR
import os

urlpatterns = [
  path('admin/', admin.site.urls),
  path('user/register/', CreateUserView.as_view(), name='register'),
  path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('', include('base.urls')),
]

if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(BASE_DIR, 'base/static'))
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)