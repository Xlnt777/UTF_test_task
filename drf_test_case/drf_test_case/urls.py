from django.contrib import admin
from django.urls import path
from menu.views import FoodApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/foods/',FoodApiView.as_view())
]
