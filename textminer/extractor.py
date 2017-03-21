import re


def phone_numbers(text):
    return re.findall(r'[(][\d]{3}[)] [\d]{3}[\D][\d]{4}', text)


## ADVANCED MODE BEGINS

def emails(text):
    return re.findall(r'[\w]+[.]*[\w]+[@][\w]+[.][\w]{2,4}', text)
