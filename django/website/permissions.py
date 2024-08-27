
from rest_framework.permissions import BasePermission

ALLOWED_DOMAIN = 'https://ksaa.gov.sa'

class IsFromAllowedDomain(BasePermission):
    """
    Custom permission to only allow requests from a specific domain.
    """

    def has_permission(self, request, view):
        origin = request.META.get('HTTP_ORIGIN')
        referer = request.META.get('HTTP_REFERER')

        # Check if the origin or referer matches the allowed domain
        if origin and origin != ALLOWED_DOMAIN:
            return False
        if referer and referer.split('/')[2] != ALLOWED_DOMAIN.split('//')[1]:
            return False
        
        return True
    
    