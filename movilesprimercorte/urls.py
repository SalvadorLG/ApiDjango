from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include(('api.urls', 'api'))),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    #path('productos/', include(('productos.urls', 'productos'))),
    path('admin/', admin.site.urls),
    path('api/accounts/', include(('tienda.urls', 'tienda-accounts'))),
    path('tienda/', include(('tienda.urls', 'tienda'))),
]