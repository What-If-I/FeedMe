import requests

user_agent = {'User-agent': 'Mozilla/5.0'}

requests.session()

p = requests.post(
    url="https://www.delivery-club.ru/ajax/user_otp",
    data={"phone": "79600403440"},
    headers=user_agent,
)
request_id = p.json()["payload"]["request_id"]

otp = input("Enter your code:")
pp = requests.post(
    "https://www.delivery-club.ru/ajax/login_otp",
    data={"request_id": request_id, "otp": otp},
    headers=user_agent,
)

print(pp)

# {
# '/': {'PHPSESSID': Cookie(version=0, name='PHPSESSID',
# value='b9uqumqjgoptuedle9783f2ev3', port=None, port_specified=False,
# domain='.delivery-club.ru', domain_specified=True, domain_initial_dot=True,
# path='/', path_specified=True, secure=True, expires=1566998544, discard=False,
# comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False),
# 'dcse': Cookie(version=0, name='dcse', value='0', port=None, port_specified=False,
# domain='.delivery-club.ru', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False,
# expires=1593350544, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False), '_delivery_visitor_cookie': Cookie(version=0,
# name='_delivery_visitor_cookie', value='%7B%22id%22%3A%221c25cff5dc885ac8bc70ce45d163ce4dffc98d93e9f54480ad8fdac8667d294b%22%2C%22timestamp%22%3A1561814593%2C%22entrance_url%22%3A%22%252Fajax%252Flogin_otp%22%2C%22referer_url%22%3A%22%22%2C%22user_agent%22%3A%22Mozilla%252F5.0%22%7D', port=None, port_specified=False, domain='.delivery-club.ru', domain_specified=True,
# domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=1877174544, discard=False, comment=None, comment_url=None,
# rest={}, rfc2109=False),
# '_delivery_menu_fullsize_photo_experiment': Cookie(version=0, name='_delivery_menu_fullsize_photo_experiment', value='1', port=None, port_specified=False, domain='.delivery-club.ru', domain_specified=True, domain_initial_dot=True,
# path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={}, rfc2109=False),
# 'auth_check': Cookie(version=0, name='auth_check', value='e9166bfc', port=None, port_specified=False, domain='.delivery-club.ru',
# domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=1566998544, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False)}