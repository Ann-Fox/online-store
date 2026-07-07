from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SiteSettings
from .serializers import SiteSettingsSerializer

class SiteSettingsView(APIView):
    def get(self, request):
        settings = SiteSettings.get_solo()
        serializer = SiteSettingsSerializer(settings)
        return Response(serializer.data)