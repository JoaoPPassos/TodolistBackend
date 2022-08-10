from django.urls import path

from . import views


urlpatterns = [
  path("create/",views.create_user_view),
  path("login/",views.user_auth_view),
  path("user/",views.detail_user_view)
]
