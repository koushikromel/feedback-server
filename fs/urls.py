from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.Feedback_details.as_view()),
    # path("<int:pk>/", views.Feedback_Change.as_view()),
]