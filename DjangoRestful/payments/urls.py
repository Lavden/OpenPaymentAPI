from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from payments import views
from django.conf.urls import include

urlpatterns = [
    path('paymentrecords/', views.PaymentList.as_view()),
    path('paymentrecords/<int:pk>/', views.PaymentDetail.as_view()),
    re_path('physicianrecords/(?P<physicianid>.+)/$', views.EachPhysicianRecordList.as_view()),
    re_path('hospitalrecords/(?P<hospitalid>.+)/$', views.EachHospitalRecordList.as_view()),
    re_path('companyrecords/(?P<companyid>.+)/$', views.EachCompanyRecordList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
