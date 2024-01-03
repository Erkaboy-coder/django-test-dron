from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('list/', GetDronsAPI.as_view()),
    path('categories/', GetDronCategoriesAPI.as_view()),
    path('actions/', DronActionsAPI.as_view()),
    path('category/actions/', DronCategoryActionsAPI.as_view()),
    path('deliver/', DeliverProductAPI.as_view()),
    path('deliver_status_changer/', DeliverProductStatusChangerAPI.as_view()),
    path('avaible_drones/', AvaibleDronesAPI.as_view()),
]
