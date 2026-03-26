import re
def cookie_parser(cookie):
    cookie_pattern = re.compile(r'([\w\-\.]+)\s*=\s*([^;]+)')
    matches = cookie_pattern.findall(cookie)
    cookie_dict = {key: value.strip() for key, value in matches}
    return cookie_dict
# if __name__=="__main__":
#     cookie=input()
#     print(cookie_parser(cookie))
   