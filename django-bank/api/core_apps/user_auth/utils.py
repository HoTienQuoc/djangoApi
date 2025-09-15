# from django.test import TestCase #noqa

# # Create your tests here.

import random
import string

def generate_otp(length=6) -> str:
    return "".join(random.choices(string.digits, k=length))
