# from rest_framework import  viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .permissions import IsFromAllowedDomain
from rest_framework import status

from .models import *
from .serializers import *


class HomepageListView(viewsets.ReadOnlyModelViewSet):
    queryset = Homepage.objects.all()
    serializer_class = HomepageSerializer

class FormPageListView(viewsets.ReadOnlyModelViewSet):
    queryset = FormPage.objects.all()
    serializer_class = FormPageSerializer

class HeaderFooterListView(viewsets.ReadOnlyModelViewSet):
    queryset = HeaderFooter.objects.all()
    serializer_class = HeaderFooterSerializer
    
class FormSectionsListView(viewsets.ReadOnlyModelViewSet):
    queryset = FormSections.objects.all()
    serializer_class = FormSectionsSerializer

class RegisteredListView(APIView):
    permission_classes = [IsFromAllowedDomain]  # Use the custom permission

    def post(self, request, *args, **kwargs):
        serializer = RegisteredSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()  # Save the instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @classmethod
    def get_extra_actions(cls):
        return []