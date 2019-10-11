from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('apps.authentication.urls', 'user')),),
    # path('users/', include('django.contrib.auth.urls')),
    path('', include_docs_urls(title='API documentation')),
    
]