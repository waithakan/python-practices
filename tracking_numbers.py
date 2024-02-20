import phonenumbers
from phonenumbers import geocoder, carrier
phone_number1 = phonenumbers.parse("+254745839108")
phone_number2 = phonenumbers.parse("+254729587309")
phone_number3 = phonenumbers.parse("+254741218444")
phone_number4 = phonenumbers.parse("+917294536271")

print("\n Phone numbers location\n")
print(geocoder.description_for_number(phone_number1, "en"))
print(geocoder.description_for_number(phone_number2, "en"))
print(geocoder.description_for_number(phone_number3, "en"))
print(geocoder.description_for_number(phone_number4, "en"))
carrier_name = carrier.name_for_number(phone_number4, "en")
print(carrier_name)