# urls.py

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserListView, UserDetailView, AssignPrivilegesView, PatientListView, PatientDetailView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/assign_privileges/', AssignPrivilegesView.as_view(), name='assign-privileges'),
    path('patients/', PatientListView.as_view(), name='patient-list'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)