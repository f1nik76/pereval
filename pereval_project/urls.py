from django.contrib import admin
from django.urls import path, include
from pereval import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register(r'submitData', views.PerevalViewset, basename='submitData')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]