from rest_framework_swagger.docgenerator import DocumentationGenerator as RestFrameworkSwaggerDocumentationGenerator
from rest_framework_swagger.introspectors import IntrospectorHelper


class APIGenerator(RestFrameworkSwaggerDocumentationGenerator):

    def generate(self, apis):
        """
        Returns documentation for a list of APIs
        """
        api_docs = {}
        for api in apis:
            api_docs[api['pattern'].name] = {
                'path': api['path'],
            }

        return api_docs
