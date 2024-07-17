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
    
    # Return data
    account_data = {
        "uid": account.uid,
        "country_code": account.country_code,
        "vat_number": account.vat_number,
        "valid": account.valid,
        "trader_name": account.trader_name,
        "trader_company_type": account.trader_company_type,
        "trader_address": account.trader_address,
        "id": account.id,
        "date": account.date,
        "source": account.source,
        "updated": datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    }

    # Define the file path
    file_path = os.path.join(os.path.expanduser('~'), 'Documents', 'kuubix_VIES', "VIES.json")

    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Save eID contact as JSON
    with open(file_path, "w") as VIES_file:
        json.dump(account_data, VIES_file, indent=4)

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
