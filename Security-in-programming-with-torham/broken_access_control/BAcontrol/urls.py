from django.contrib import admin
from django.urls import path
from Bug.views import AdminsList, CheckAccess, ChangeAccess

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AdminsList.as_view()),
    path('check/<int:user_pk>/', CheckAccess.as_view()),
    path('change/<int:user_pk>/<str:access_level>/', ChangeAccess.as_view()),

]
