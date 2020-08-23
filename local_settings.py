from nsupdate.settings.dev import *
SECRET_KEY='f4MgZiERfgX6WRdFFXpHcmzS'

# service contact for showing on the "about" page:
SERVICE_CONTACT = 'nsupdate@'

# sender address for e.g. user activation emails
DEFAULT_FROM_EMAIL = 'nsupdate@'

# nameservers used e.g. for MX lookups in the registration email validation.
# google / cloudflare DNS IPs are only given as example / fallback -
# please configure your own nameservers in your local settings file.
NAMESERVERS = ['1.1.1.1', ]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Manila'

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

REGISTRATION_OPEN = False

DEBUG = False

WE_HAVE_TLS = True  # True if you run a https site also, suggest that site to users if they work on the http site.
CSRF_COOKIE_SECURE = WE_HAVE_TLS
SESSION_COOKIE_SECURE = WE_HAVE_TLS

# these are the service host names we deal with
BASEDOMAIN = 'nsupdate.way-of-the-blade.com'
# do NOT just use the BASEDOMAIN for WWW_HOST, or you will run into troubles
# when you want to be on publicsuffix.org list and still be able to set cookies
WWW_HOST = BASEDOMAIN  # a host with a ipv4 and a ipv6 address
# hosts to enforce a v4 / v6 connection (to determine the respective ip)
WWW_IPV4_HOST = 'ipv4-' + BASEDOMAIN  # a host with ONLY a ipv4 address
WWW_IPV6_HOST = 'ipv6-' + BASEDOMAIN  # a host with ONLY a ipv6 address

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [WWW_HOST, WWW_IPV4_HOST, WWW_IPV6_HOST]

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'local.middleware.SetRemoteAddrFromForwardedFor',
)
