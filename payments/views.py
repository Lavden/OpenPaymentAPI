from rest_framework import generics
from rest_framework.views import APIView
from payments.models import OpDtlRsrchPgyr2018P01172020
from payments.serializers import RsrchSerializer
from payments.permissions import CustomPermissionClass
from django.http import HttpResponseForbidden

class PaymentList(generics.ListCreateAPIView):
    queryset = OpDtlRsrchPgyr2018P01172020.objects.all()
    serializer_class = RsrchSerializer

class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OpDtlRsrchPgyr2018P01172020.objects.all()
    serializer_class = RsrchSerializer

class EachPhysicianRecordList(generics.ListCreateAPIView):
    permission_classes = [CustomPermissionClass, ]
    serializer_class = RsrchSerializer

    def get_queryset(self):
        username = self.kwargs['physicianid']
        return OpDtlRsrchPgyr2018P01172020.objects.filter(physician_profile_id=username)

class EachHospitalRecordList(generics.ListCreateAPIView):
    permission_classes = [CustomPermissionClass, ]
    serializer_class = RsrchSerializer

    def get_queryset(self):
        username = self.kwargs['hospitalid']
        return OpDtlRsrchPgyr2018P01172020.objects.filter(teaching_hospital_id=username)

class EachCompanyRecordList(generics.ListCreateAPIView):
    permission_classes = [CustomPermissionClass, ]
    serializer_class = RsrchSerializer

    def get_queryset(self):
        username = self.kwargs['companyid']
        return OpDtlRsrchPgyr2018P01172020.objects.filter(applicable_manufacturer_or_applicable_gpo_making_payment_id=username)
