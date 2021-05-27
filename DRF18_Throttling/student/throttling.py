from rest_framework.throttling import UserRateThrottle


class CustomRateThrottle(UserRateThrottle):
    scope = 'custom'  # Use this scope name to set throttle rate in settings.py
