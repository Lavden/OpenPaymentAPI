from rest_framework import serializers
from payments.models import OpDtlRsrchPgyr2018P01172020

class RsrchSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpDtlRsrchPgyr2018P01172020
        fields = ['covered_recipient_type', 'teaching_hospital_id', 'teaching_hospital_name',
        'physician_profile_id', 'physician_first_name', 'recipient_primary_business_street_address_line1','physician_specialty',
        'submitting_applicable_manufacturer_or_applicable_gpo_name','total_amount_of_payment_usdollars','date_of_payment',
        'record_id']

