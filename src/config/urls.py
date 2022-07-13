from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json


schema_view = get_schema_view(
   openapi.Info(
      title="UAVoiceGenerator API",
      default_version='v1',
      description="UAVoiceGenerator API",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


@login_required()
def userdata(request):
    user = request.user
    return HttpResponse(
        json.dumps({
            'username': user.username
        }),
        content_type='application/json'
    )


urlpatterns = [
    path('admin/', admin.site.urls),

    # Apps
    path('', include('users.urls')),
    path('', include('voices.urls')),
    path('api/', include('api.urls')),

    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('userdata', userdata, name='userdata'),

    # Swagger
    path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
