from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('projetos/', include('projetos.urls')),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="projetos/index.html")),
]
