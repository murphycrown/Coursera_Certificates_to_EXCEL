import requests
import math

def makeRequest(count,cookie):
    my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',

    'Referer': 'https://www.coursera.org'
}
    url='https://www.coursera.org/api/courseAccomplishments.v1/?q=byUser&userId=196790661&start={}&limit=10'

    response=requests.get(url.format(count),cookies=cookie,headers=my_headers)

    return(response.text)
def makeRequestLink(targetUrl):
    url="https://www.coursera.org/api/customUrls.v1"
    headers={
        "Content-type":"application/json"}
    data={
    "customSlug":"",
    "targetUrl":targetUrl
    }
    response = requests.post(url,headers=headers,json=data)
    return response.text

