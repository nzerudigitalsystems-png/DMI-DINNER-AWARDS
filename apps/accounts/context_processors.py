from django.conf import settings


def google_oauth_status(request):
    return {'google_oauth_enabled': settings.GOOGLE_OAUTH_ENABLED}
