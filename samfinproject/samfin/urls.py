from django.urls import path
from .views import Happy

urlpatterns = [
    path('v1/', Happy.as_view()),

]
