ascii_art = """

 ██▓███   ██░ ██  ▒█████   ███▄    █ ▓█████      ██████  ██▓███ ▓██   ██▓
▓██░  ██▒▓██░ ██▒▒██▒  ██▒ ██ ▀█   █ ▓█   ▀    ▒██    ▒ ▓██░  ██▒▒██  ██▒
▓██░ ██▓▒▒██▀▀██░▒██░  ██▒▓██  ▀█ ██▒▒███      ░ ▓██▄   ▓██░ ██▓▒ ▒██ ██░
▒██▄█▓▒ ▒░▓█ ░██ ▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄      ▒   ██▒▒██▄█▓▒ ▒ ░ ▐██▓░
▒██▒ ░  ░░▓█▒░██▓░ ████▓▒░▒██░   ▓██░░▒████▒   ▒██████▒▒▒██▒ ░  ░ ░ ██▒▓░
▒▓▒░ ░  ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░   ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░  ██▒▒▒ 
░▒ ░      ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░   ░ ░▒  ░ ░░▒ ░     ▓██ ░▒░ 
░░        ░  ░░ ░░ ░ ░ ▒     ░   ░ ░    ░      ░  ░  ░  ░░       ▒ ▒ ░░  
          ░  ░  ░    ░ ░           ░    ░  ░         ░           ░ ░     
                                                                 ░ ░     
            \033[1mразработано @ARTIST для INFLUXION\033[0m                                                        
                                                                                                                 
                                                                  
"""
print(ascii_art)
import requests
import phonenumbers
from phonenumbers import geocoder, carrier

def lookup_phone_number(phone_number):
    try:
        # Parse the phone number using phonenumbers
        parsed_number = phonenumbers.parse(phone_number)
        country_name = geocoder.description_for_number(parsed_number, "en")
        carrier_name = carrier.name_for_number(parsed_number, "en")

        print(f"Detected Country: {country_name}")
        print(f"Carrier: {carrier_name}")

        # NumVerify API details
        api_url = "http://apilayer.net/api/validate"
        api_key = "c5748a6262019a92e4ca597acadd2894"  # Replace with your NumVerify API key
        params = {
            "access_key": api_key,
            "number": phone_number
        }

        # Send request to NumVerify API
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            phone_details = response.json()
            if phone_details.get("valid"):
                print("\nPhone Details:")
                print(f"  Number: {phone_details['number']}")
                print(f"  Local Format: {phone_details['local_format']}")
                print(f"  International Format: {phone_details['international_format']}")
                print(f"  Country: {phone_details['country_name']}")
                print(f"  Location: {phone_details['location']}")
                print(f"  Carrier: {phone_details['carrier']}")
                print(f"  Line Type: {phone_details['line_type']}")
            else:
                print("Invalid phone number.")
        else:
            print(f"Failed to retrieve details: {response.status_code} - {response.text}")

    except phonenumbers.NumberParseException as e:
        print(f"Invalid phone number format: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching details: {e}")

if __name__ == "__main__":
    phone_number = input("Enter the phone number (with country code): ")
    lookup_phone_number(phone_number)

