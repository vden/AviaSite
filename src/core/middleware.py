from core.models import Portal

class PortalMiddleware(object):
    def process_request(self, request):
        request.portal = Portal.objects.all()[0]
        return None
