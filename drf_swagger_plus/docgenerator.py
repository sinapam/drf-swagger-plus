from rest_framework_swagger.docgenerator import DocumentationGenerator as RestFrameworkSwaggerDocumentationGenerator
from rest_framework_swagger.introspectors import IntrospectorHelper


class DocumentationGenerator(RestFrameworkSwaggerDocumentationGenerator):

    def generate(self, apis):
        """
        Returns documentation for a list of APIs
        """
        api_docs = {}
        for api in apis:
            api_docs[api['pattern'].name] = {
                'description': IntrospectorHelper.get_summary(api['callback']),
                'path': api['path'],
                'operations': self.get_operations(api, apis),
            }

        return api_docs
