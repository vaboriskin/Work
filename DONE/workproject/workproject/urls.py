from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Административная панель
    path('accounts/', include('accounts.urls')),  # URL-ы для регистрации и входа
    path('', include('main.urls')),  # Главная страница
    path('vote/', include('vote.urls')),
    path('Table/', include('Table.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
