# -*-coding: utf-8-*-
"""
1.login vào site http://45.79.43.178/source_carts/wordpress/wp-admin bằng code python.
Sau khi login thành công thì lấy ra name của user vừa login
email': 'admin', 'password': ''
"""
import requests
from bs4 import BeautifulSoup

wp_admin = "http://45.79.43.178/source_carts/wordpress/wp-admin"
wp_login = "http://45.79.43.178/source_carts/wordpress/wp-login.php"

username = "admin"
password = ""

with requests.Session() as session:
    headers = {"Cookie":"Wordpress_test_cookie=WP test cookie"}
    payload = {
        'log':username, 'pwd':password, 'wp-submit':'Log In',
        'redirect_to':wp_admin, 'testcookie':'1'
    }

    session.post(wp_login, data=payload, headers=headers)
    re = session.get(wp_admin)

    # print(re.text)
    # content = str(re.text)
    # file = open('test.html', 'w')
    # file.write(str(content))
    # file.close()

soup = BeautifulSoup(re.content, 'html.parser')
tag = soup.find('span', {'class':'display-name'}) # <span class="display-name">admin</span>
name_user = tag.text
print(name_user) # admin