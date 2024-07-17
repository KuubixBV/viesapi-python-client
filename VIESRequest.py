from viesapi import VIESAPIClient
import datetime
import json
import sys
import os

def main(Id, Key, euvat):

    # Create client object and establish connection to the test system
    viesapi = VIESAPIClient(Id, Key)

    # Check if viesapi is OK
    if not viesapi:
        exit()

    # Get current account status
    account = viesapi.get_account_status()

    # Check if account is returned
    if not account:
        exit()

    # Get VAT data
    vies_data_response = viesapi.get_vies_data(euvat)

    # Check if vies response is returned
    if not vies_data_response:
        exit()
    
    # Return data
    vies_data = {
        "uid": vies_data_response.uid,
        "country_code": vies_data_response.country_code,
        "vat_number": vies_data_response.vat_number,
        "valid": vies_data_response.valid,
        "trader_name": vies_data_response.trader_name,
        "trader_company_type": vies_data_response.trader_company_type,
        "trader_address": vies_data_response.trader_address,
        "id": vies_data_response.id,
        "date": vies_data_response.date,
        "source": vies_data_response.source,
        "updated": datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    }

    # Define the file path
    file_path = os.path.join(os.path.expanduser('~'), 'Documents', 'kuubix_VIES', "VIES.json")

    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Save eID contact as JSON
    with open(file_path, "w") as VIES_file:
        json.dump(vies_data, VIES_file, indent=4)

if __name__ == "__main__":

    # Check for valid input
    if len(sys.argv) != 4:
        exit()
        print("Usage: python script.py <Id> <Key> <euvat>")

    # Get inputs
    Id = sys.argv[1]
    Key = sys.argv[2]
    euvat = sys.argv[3]

    # Run VIES check
    main(Id, Key, euvat)
