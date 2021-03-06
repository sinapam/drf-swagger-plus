from rest_framework.response import Response
import rest_framework_swagger as rfs
from rest_framework_swagger.views import SwaggerApiView
from drf_swagger_plus.docgenerator import APIGenerator


class APIRootView(SwaggerApiView):
    authentication_classes = ()

    def get(self, request):
        apis = self.get_apis_for_resource('')
        generator = APIGenerator(for_user=request.user)
        return Response({
            'apiVersion': rfs.SWAGGER_SETTINGS.get('api_version', ''),
            'swaggerVersion': '1.2',
            'basePath': self.api_full_uri.rstrip('/'),
            'apis': generator.generate(apis),
        })
