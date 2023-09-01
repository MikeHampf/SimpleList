from django.core.exceptions import ValidationError
import re

def validate_name(input):
    error_message = "Improper Charaters Entered"
    regex = r";"
    good_name = re.search(regex, input)
    if not good_name:
        return input
    else: 
        raise ValidationError(error_message, params={'input':input})