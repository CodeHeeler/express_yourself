import re


def words(text):
    result = re.findall(r'[\w]*[-]*[A-Za-z]+', text)
    if result == []:
        return None
    return result


def phone_number(text):
    result = re.search(r'[(]{0,1}(?P<area>[\d]{3})[\D]*'
                       r'(?P<first>[\d]{3})[\D]{0,1}(?P<last>[\d]{4})', text)
    if result:
        return {'area_code': result.group('area'),
                'number': result.group('first') + "-" + result.group('last')}
    return None


def money(text):
    result = re.search(r'^(?P<symbol>[$]{1})'
                       r'(?P<number>(([\d]+([.][\d]{2}){0,1})$'
                       r'|([\d]{1,3}([,][\d]{3})+([.][\d]{2}){0,1})))', text)
    if result:
        return {'currency': result.group('symbol'),
                'amount': float(re.sub('[,]', '', result.group('number')))}
    return None


def zipcode(text):
    result = re.search(r'^(?P<original>[\d]{5})'
                       r'([-](?P<extra>[\d]{4})){0,1}$', text)
    if result:
        return {'zip': result.group('original'),
                'plus4': result.group('extra')}
    return None

def date(text):
    result = re.search(r'(?P<forward>(?P<my_month>([\d]{1,2}[/]))'
                       r'(?P<my_day>([\d]{1,2}[/]))(?P<my_year>[\d]{4}))'
                       r'|(?P<rev_year>[\d]{4})(?P<rev_month>([-][\d]{2}))'
                       r'(?P<rev_day>([-][\d]{2}))', text)
    if result:
        if result.group('forward'):
            return {'month': int(re.sub('^[0]', '',
                                        re.sub('[/]', '',
                                               result.group('my_month')))),
                    'day': int(re.sub('^[0]', '',
                                      re.sub('[/]', '',
                                             result.group('my_day')))),
                    'year': int(result.group('my_year'))}
        return {'month': int(re.sub('^[0]', '',
                                    re.sub('[-]', '',
                                           result.group('rev_month')))),
                'day': int(re.sub('^[0]', '',
                                  re.sub('[-]', '',
                                         result.group('rev_day')))),
                'year': int(result.group('rev_year'))}
    return None


## ADVANCED MODE BEGINS

# duplicate of above function--duplicate test case also, confused me a while
# def date(text):
#     # return re.findall(r'', text)
#     pass


def advanced_date(text):
    # return re.findall(r'', text)
    pass


def email(text):
    # return re.findall(r'', text)
    pass


def address(text):
    # return re.findall(r'', text)
    pass
