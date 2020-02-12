from django.db import models
from django.contrib.auth.models import AbstractUser, Group

class OpDtlRsrchPgyr2018P01172020(models.Model):
    covered_recipient_type = models.TextField(blank=True, null=True)
    teaching_hospital_id = models.TextField(blank=True, null=True)
    teaching_hospital_name = models.TextField(blank=True, null=True)
    physician_profile_id = models.TextField(blank=True, null=True)
    physician_first_name = models.TextField(blank=True, null=True)
    physician_last_name = models.TextField(blank=True, null=True)
    recipient_primary_business_street_address_line1 = models.TextField(blank=True, null=True)
    recipient_city = models.TextField(blank=True, null=True)
    recipient_state = models.TextField(blank=True, null=True)
    recipient_zip_code = models.TextField(blank=True, null=True)
    recipient_country = models.TextField(blank=True, null=True)
    physician_primary_type = models.TextField(blank=True, null=True)
    physician_specialty = models.TextField(blank=True, null=True)
    submitting_applicable_manufacturer_or_applicable_gpo_name = models.TextField(blank=True, null=True)
    applicable_manufacturer_or_applicable_gpo_making_payment_id = models.TextField(blank=True, null=True)
    applicable_manufacturer_or_applicable_gpo_making_payment_state = models.TextField(blank=True, null=True)
    applicable_manufacturer_or_applicable_gpo_making_payment_countr = models.TextField(blank=True, null=True)
    indicate_drug_or_biological_or_device_or_medical_supply_1 = models.TextField(blank=True, null=True)
    product_category_or_therapeutic_area_1 = models.TextField(blank=True, null=True)
    total_amount_of_payment_usdollars = models.TextField(blank=True, null=True)
    date_of_payment = models.TextField(blank=True, null=True)
    form_of_payment_or_transfer_of_value = models.TextField(blank=True, null=True)
    preclinical_research_indicator = models.TextField(blank=True, null=True)
    name_of_study = models.TextField(blank=True, null=True)
    record_id = models.TextField(primary_key=True)

    def __str__(self):
        return self.teaching_hospital_id + " " + self.physician_profile_id + " " + self.record_id

    class Meta:
        managed = False
        db_table = 'op_dtl_rsrch_pgyr2018_p01172020'
