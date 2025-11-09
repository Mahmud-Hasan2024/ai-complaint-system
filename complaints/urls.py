from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("my_complaints/", views.my_complaints, name="my_complaints"),
    path("update_status/<int:complaint_id>/", views.update_status, name="update_status"),
    path("delete_complaint/<int:complaint_id>/", views.delete_complaint, name="delete_complaint"),
    path("notifications/", views.notifications, name="notifications"),
]
