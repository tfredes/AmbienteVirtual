from django.contrib import admin
from django.urls import path, include
from rest_framework import routers,serializers, viewsets
from .models import Plan

# Clase serializadora de Usuarios
class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan 
        fields = ['id','name','description','review', 'price']

# Clase de viewset que hace el puente entre bd - serealizacion
class PlanViewSet(viewsets.ModelViewSet):
    # Query que ejecutara a la bd
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

router = routers.DefaultRouter()
router.register(r'', PlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
