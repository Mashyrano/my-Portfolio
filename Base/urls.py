from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("signup", views.signup),
    path("projects", views.projects),
    path("contact", views.contact),
    path("about", views.about),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cv/<path:file_name>', views.serve_cv, name='serve_cv'),
]