from django.core.exceptions import ValidationError
import re

def validate_item_and_notes(input):
    error_message = "Improper Charaters Entered"
    regex = r";"
    good_input = re.search(regex, input)
    if not good_input:
        return input
    else: 
        raise ValidationError(error_message, params={'input':input})