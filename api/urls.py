from django.urls import path
from api import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', home, name="home"),
  path('resume/', views.ProfileView.as_view(), name='resume'),
  path('list/', views.ProfileView.as_view(), name='list')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)