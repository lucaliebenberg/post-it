import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException
from django.core.exceptions import ValidationError

def clean_msisdn(msisdn):
    """
    :param msisdn:
    :return:
    """
    if not msisdn:
        return None
    if msisdn.replace(" ", "") == "":
        return None

    international_start_digits = ["27", "88239", "2796020", "46719", "883120", "3277"]
    for digits in international_start_digits:
        if msisdn.startswith(digits):
            msisdn = "+" + msisdn
            break
    try:
        x = phonenumbers.parse(msisdn, "ZA")
        return phonenumbers.format_number(
            x, phonenumbers.PhoneNumberFormat.E164
        ).replace("+", "")
    except NumberParseException as e:
        raise ValidationError("MSISDN: %s ERROR: %s" % (msisdn, e))
def validate_msisdn(msisdn):
    """
    :param msisdn:
    """
    msisdn = clean_msisdn(msisdn)
    try:
        msisdn_len = len(msisdn)
        if msisdn_len:
            x = phonenumbers.parse(msisdn, "ZA")
            return x
        else:
            raise ValidationError("Msisdn needs to be a valid length")  # noqa: F841
    except NumberParseException as e:
        raise ValidationError("%s %s" % (msisdn, e))