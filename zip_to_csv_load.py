from zipfile import ZipFile
import csv
import urllib.request

def download_notary_zip(url_path, dest_path):
    """Download file from path"""
    print("Downloading notary zip file...")
    urllib.request.urlretrieve(url_path, dest_path)

def extract_zip_file(src_path, dest_path):
    """Extract zip file from source path to desp_path"""
    print("Extracting Zip file...")
    with ZipFile(src_path, 'r') as zipObj:
        zipObj.extractall(dest_path)

def convert_text_to_csv(src_path, dest_path):
    """Convert text file in src path and place store in dest path"""
    print("Converting text to formatted csv...")
    with open(src_path, 'r') as text_file:
        organized_rows = []
        stripped = (line.strip() for line in text_file)
        lines = (line.split("\t") for line in stripped if line)
        for line in lines:
            first_name = line[0].split(',')[1].strip()
            last_name = line[0].split(',')[0].strip()
            business_name = line[1].strip()
            business_address = line[2].strip() + " " + line[3].strip() + " "+ line[4].strip()
            zip_code = line[5].strip()
            filling_country_code = line[6].strip()
            notary_comission_number = line[7].strip()
            notary_expiry_date = line[8].strip()
            organized_rows.append(
                (
                    first_name,
                    last_name,
                    business_name,
                    business_address,
                    zip_code,
                    filling_country_code,
                    notary_comission_number,
                    notary_expiry_date
                )
            )
        with open(dest_path, 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('first_name','last_name', 'business_name', 'business_address', 'zip_code', 'filling_country_code', 'notary_commission_number', 'notary_expiry_date'))
            writer.writerows(organized_rows)
    pass

# Download zip file from path
url_path = "https://notary.cdn.sos.ca.gov/export/active-notary.zip"
download_notary_zip(url_path, 'active_notary/active-notary.zip')
# Extract zip to destination
extract_zip_file('active_notary/active-notary.zip', 'active_notary')
# Convert text to compatible csv
convert_text_to_csv('active_notary/active-notary.txt', 'active_notary/active_notary.csv')