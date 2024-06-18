import requests
import json
import re
import pytest

res= requests.get('https://gorest.co.in/public/v2/comments')

response = res.json()

#print(response)

def email_count():
    sum_of_email_cont_exam = 0
    for each in response:
        if 'example' in each['email']:
            sum_of_email_cont_exam = sum_of_email_cont_exam + 1
    return sum_of_email_cont_exam

print(email_count())

def test_case_to_validate_count():
    assert email_count() > 5



