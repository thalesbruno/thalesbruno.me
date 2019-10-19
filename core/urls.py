from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from home.views import home, thanks
from blog.views import blog_home, blog_post

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('thanks/', thanks, name='thanks'),
    path('blog/', blog_home, name='blog_home'),
    path('blog/post/<id>/', blog_post, name='blog_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)