from .views import *
from django.urls import re_path as url
from django.urls import include
from rest_framework import routers
from django.urls import path

router = routers.DefaultRouter()
router.register("homepage", HomepageListView)
router.register("form_page", FormPageListView)
router.register("form_sections", FormSectionsListView)
router.register("header-footer", HeaderFooterListView)

urlpatterns = [
  url(r'^api/', include(router.urls)),
  path('register/', RegisteredListView.as_view(), name='register'),
]
