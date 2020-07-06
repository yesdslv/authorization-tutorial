from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from marks.views import home, teacher_dashboard, StudentDashboardView, StudentView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='marks/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('student/<int:id>', StudentView.as_view(), name='student'),
    path('teacher-dashboard', teacher_dashboard, name='teacher-dashboard'),
    path('student-dashboard', StudentDashboardView.as_view(), name='student-dashboard'),
    path('', home, name='home'),
]