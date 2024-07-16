from django.urls import path, include
from .views import ExpenseView
from rest_framework import routers


router = routers.SimpleRouter()
router.register('expenses', ExpenseView)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]