from django.urls import path, re_path, include
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns

from payments.views import *

urlpatterns = [
    path("profiles",UserProfileList.as_view(),name="all-profiles"),
    path("profile/<int:pk>",UserProfileDetail.as_view(),name="profile"),
    path("records",RecordList.as_view(),name="all-records"),
    path("record/<int:pk>",RecordDetail.as_view(),name="record"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
