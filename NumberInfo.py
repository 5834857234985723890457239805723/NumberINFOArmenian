import os
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from pystyle import Colorate, Colors

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_ascii_art():
    ascii_art = """

__________                         __                .__   
\____    /________________________/  |_  ____   ____ |  |  
  /     // __ \_  __ \___   /  _ \   __\/  _ \ /  _ \|  |  
 /     /\  ___/|  | \//    (  <_> )  | (  <_> |  <_> )  |__
/_______ \___  >__|  /_____ \____/|__|  \____/ \____/|____/
        \/   \/            \/                                   
                \n[+] By Ես գալիս եմ Կավկազից                   """


    colored_ascii_art = Colorate.Horizontal(Colors.yellow_to_red, ascii_art)
    print(colored_ascii_art)

def main():
    display_ascii_art()

    try:
        while True:
            phone_number = input(Colorate.Horizontal(Colors.yellow_to_red, "\nմուտքագրեք հեռախոսահամարը : "))
            print(Colorate.Horizontal(Colors.yellow_to_red, "Տեղեկությունների առբերում..."))

            try:
                parsed_number = phonenumbers.parse(phone_number, None)
                if phonenumbers.is_valid_number(parsed_number):
                    if phone_number.startswith("+"):
                        country_code = "+" + phone_number[1:3]
                    else:
                        country_code = "None"
                    operator = carrier.name_for_number(parsed_number, "fr")
                    type_number = "Mobile" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "Fixe"
                    timezones = timezone.time_zones_for_number(parsed_number)
                    timezone_info = timezones[0] if timezones else "None"
                    country = phonenumbers.region_code_for_number(parsed_number)
                    region = geocoder.description_for_number(parsed_number, "fr")
                    status = "Valid"
                    
                    print(Colorate.Horizontal(Colors.yellow_to_red, f"""
[+] Հեռախոս            : {phone_number}
[+] Երկրի կոդը         : {country_code}
[+] Երկիր              : {country}
[+] Տարածաշրջան        : {region}
[+] Ժամային գոտի       : {timezone_info}
[+] Օպերատոր           : {operator}
[+] Մուտքագրեք համարը  : {type_number}
[+] Telegram >> https://t.me/{phone_number}
[+] Whatsapp >> https://wa.me/{phone_number}
[+] Viber >> https://viber.click/{phone_number} """))
                    
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, " Անվավեր ձևաչափ: [Օրինակ՝ +442012345678 կամ +33623456789]"))

            except Exception as e:
                print(Colorate.Horizontal(Colors.yellow_to_red, f" Բացառություն կա: {e}"))

            choice = input(Colorate.Horizontal(Colors.yellow_to_red, "Ցանկանու՞մ եք շարունակել։ (y/n): ")).strip().lower()
            if choice != 'y':
                break
            else:
                clear_terminal()
                display_ascii_art()

    except Exception as e:
        print(f"Սխալ: {e}")

if __name__ == "__main__":
    main()
