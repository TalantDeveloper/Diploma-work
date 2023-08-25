from django.contrib import admin
from django.urls import path, include
# model translation urls
from django.conf.urls.i18n import i18n_patterns
# ckeditor urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('api/', include('main.api.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]


# model-translation urls
urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
