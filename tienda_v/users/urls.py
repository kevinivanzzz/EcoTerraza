from django.urls import path
from users.views import login_user, registrarse
from  django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('registrarse/', registrarse, name="registrarse"),
    path('iniciar_sesion/', login_user, name = "iniciar_sesion"),
    path('', LoginView.as_view(template_name='index.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)