from django.conf.urls import url 
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^api/atencion/$',views.AtencionViewSet.as_view()),
    url(r'^api/tipoatencion/$',views.TipoAtencionViewSet.as_view()),
    url(r'^api/atencion_buscar/(?P<id>.+)/$',views.AtencionBuscarViewSet.as_view()),
    url(r'^api/tipoatencion_buscar/(?P<id>.+)/$',views.TipoAtencionBuscarViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)