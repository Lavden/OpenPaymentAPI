import pandas as pd
import csv

def user_record():
    hospital = []
    physician = []
    company = []

    file_name = '../Data/2018/OP_DTL_RSRCH_PGYR2018_P01172020.csv'
    df = pd.read_csv(file_name)

    for idx, row in df.iloc[1:].iterrows():
        if row['Covered_Recipient_Type'] == 'Covered Recipient Teaching Hospital':
            # Hospital
            hospiatl_id = str(row['Teaching_Hospital_ID']).split('.')[0]
            hospital_name = row['Teaching_Hospital_Name']
            hospital_address = row['Recipient_Primary_Business_Street_Address_Line1']
            hospital_city = row['Recipient_City']
            hospital_state = row['Recipient_State']
            user_type = 'Hospital'
            hospital.append((hospiatl_id,hospital_name,hospital_address,hospital_city,hospital_state,user_type))
        elif row['Covered_Recipient_Type'] == 'Covered Recipient Physician':
            # Physician
            physician_id = str(row['Teaching_Hospital_ID']).split('.')[0]
            physician_name = row['Teaching_Hospital_Name']
            physician_address = row['Recipient_Primary_Business_Street_Address_Line1']
            physician_city = row['Recipient_City']
            physician_state = row['Recipient_State']
            user_type = 'Physician'
            physician.append((physician_id,physician_name,physician_address,physician_city,physician_state,user_type))
        # Company
        company_id = str(row['Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_ID']).split('.')[0]
        company_name = row['Submitting_Applicable_Manufacturer_or_Applicable_GPO_Name']
        company_address = None
        company_city = None
        company_state = row['Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_State']
        user_type = 'Company'
        company.append((company_id,company_name,company_address,company_city,company_state,user_type))

    with open('../Data/2018/userProfile.csv','w') as f:
        csv_f = csv.writer(f)
        csv_f.writerow(['user_id_id','user_name','address','city','state','user_type'])
        for row in hospital:
            csv_f.writerow(row)
        for row in physician:
            csv_f.writerow(row)
        for row in company:
            csv_f.writerow(row)

def auth_user():
    

if __name__ == '__main__':
    # hospital = []
    # physician = []
    # company = []

    # Create user records
    user_record()

    # Create user ids
    auth_user()


