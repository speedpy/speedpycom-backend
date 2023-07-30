from django.urls import path
from django.views.generic import RedirectView

from .api.user import UserInfoAPIView

urlpatterns = [
    path('', RedirectView.as_view(url='/api/schema/swagger-ui/', permanent=False)),
    path('user/info', UserInfoAPIView.as_view(), name='user_info'),
]
