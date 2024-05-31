from django.urls import path
from productos.views import productos, nosotros
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('productos/', productos, name="productos"),
   path('nosotros/', nosotros, name="nosotros"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)