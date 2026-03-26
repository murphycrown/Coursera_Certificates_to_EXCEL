from bs4 import BeautifulSoup 
def linkextract(content):
    for i in content['elements']:
        with open('target_urls.txt','a') as file: 
            link="https://www.coursera.org/account/accomplishments/verify/"+i['verifyCode']+'?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=project'+'\n'
            file.write(link)
        with open('certificate_names.txt','a') as filen:
            filen.write(i['name']+'\n')
def verificationlinkSaver(context):
    linkCode=context['elements'][0]['customSlug']
    finalLink='https://coursera.org/share/'+linkCode+'\n'
    with open('verification_links.txt','a') as file:
        file.write(finalLink)
# if __name__=="__main__":
