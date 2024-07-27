from django.urls import path
from .views import (RegisterPatientView, LoginView, LogoutView, 
                    UserListView, UserDetailView, AssignPrivilegesView, 
                    PatientListView, PatientDetailView)

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/assign_privileges/', AssignPrivilegesView.as_view(), name='assign-privileges'),
    path('patients/', PatientListView.as_view(), name='patient-list'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    
    path('patients/register/', RegisterPatientView.as_view(), name='register-patient'), 
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
