from core.models import Portal
import settings

class PortalMiddleware(object):
    def process_request(self, request):
        request.portal = Portal.objects.all()[0]
	request.portal.feedback = settings.FEEDBACK_MAIL
        return None
