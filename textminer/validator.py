import re


def binary(text):
    return re.findall(r'^([0]|[1])+$', text)


def binary_even(text):
    return re.findall(r'^([0]|[1])*[0]$', text)



def hex(text):
    return re.findall(r'^[A-F0-9]+$', text)


def word(text):
    return re.findall(r'^[\w]*[-]*[A-Za-z]+$', text)


def words(text, count=None):
    result = re.findall(r'\b[\w]*[-]*[A-Za-z]+\b', text)
    if count:
        if len(result) != count:
            return None
    return re.findall(r'\b[\w]*[-]*[A-Za-z]+\b', text)


def phone_number(text):
    return re.findall(r'[(]{0,1}[\d]{3}[\D]*[\d]{3}[\D]{0,1}[\d]{4}', text)


def money(text):
    return re.findall(r'^[$](([\d]+([.][\d]{2}){0,1})$|'
                      r'([\d]{1,3}([,][\d]{3})+([.][\d]{2}){0,1}))', text)


def zipcode(text):
    return re.findall(r'^[\d]{5}([-][\d]{4}){0,1}$', text)


def date(text):
    return re.findall(r'([\d]{1,2}[/]){2}[\d]{4}|[\d]{4}([-][\d]{2}){2}', text)


## ADVANCED MODE BEGINS


def advanced_date(text):
    # return re.findall(r'', text)
    pass


def email(text):
    # return re.findall(r'', text)
    pass


def address(text):
    # return re.findall(r'', text)
    pass
