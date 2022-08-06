from django.contrib import admin
from django.urls import path, include
from social import views

#import done for managing media
from django.conf import settings                     
from django.conf.urls.static import static


# Added Manually To Change Django Admin Text

admin.site.site_header = "TalentServe Admin"
admin.site.index_title = "TalentServe"
admin.site.site_title = "TalentServe"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
