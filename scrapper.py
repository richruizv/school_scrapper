import requests as req
import lxml.html as html
import os
import datetime
import csv  

def parse_link( link ,xptitle, xpmodality,xpduration,xpprice,test):
    try:
        print('single link = ' + link)
        if test == 1:
            print('title = ' + xptitle)
            print('modality = ' + xpmodality)
            print('duration = ' + xpduration)
            print('price = ' + xpprice)
        response = req.get(link)
        if response.status_code== 200:
            continue_education = response.content.decode('utf-8')
            parsed = html.fromstring(continue_education)
            #print(continue_education)
            try:
                if not xptitle:
                    title = ''
                else:
                    xtitle = parsed.xpath(xptitle)
                    if len(xtitle) > 0:
                        title = xtitle[0].strip(' \t\n\r')
                    else:
                        title = ''

                if not xpmodality:
                    modality = ''
                else:
                    xmodality = parsed.xpath(xpmodality)
                    if len(xmodality) > 0:
                        modality = xmodality[0].strip(' \t\n\r')
                    else:
                        modality = ''

                if not xpduration:
                    duration = ''
                else:
                    xduration = parsed.xpath(xpduration)
                    if len(xduration) > 0:
                        duration = xduration[0].strip(' \t\n\r')
                    else:
                        duration = ''

                if not xpprice:
                    price = ''
                else:
                    xprice = parsed.xpath(xpprice)
                    if len(xprice) > 0:
                        price = xprice[0].strip(' \t\n\r')
                    else:
                        price = ''

                print("Title "+title)
                print("Modality "+modality)
                print("Duration "+duration)
                print("Price "+price)
                return [title,modality,duration,price]
            except IndexError:
                print('We cant find information in the Xpath '+IndexError)  
        else:
            raise ValueError(response.status_code)
    except ValueError as e:
        print(e)

def parse_page(reg,test):	

    try:
        university_name = reg[0]
        home_link = reg[4]
        article_link = reg[5]
        complete_url = reg[6]
        no_pages = reg[7]
        xpath_article = reg[8]
        
        if test == 1:
            print('university_name = '+university_name)
            print('home_link = '+home_link)
            print('article_link = '+article_link)
            print('complete_url = '+str(complete_url))
            print('xpath_article = '+xpath_article)
            dir_location = 'test'
        else:
            dir_location = 'prod'
        
        no_pages = int(no_pages)

        # We open the file to save de info
        url_uni = 'csv/'+dir_location+'/    '+university_name+'.csv'
        with open(url_uni, 'w', encoding='utf-8') as f:

            for page in range(no_pages):
                if no_pages > 1:
                    response = req.get(article_link+str(page))
                else:
                    response = req.get(article_link)

                if response.status_code== 200:
                    home = response.content.decode('UTF-8')
                    parsed = html.fromstring(home)
                    links_to_notices = parsed.xpath(xpath_article)
                    
                    writer = csv.writer(f)
                    # write the data
                    for link in links_to_notices:
                        if(complete_url == 0):
                            link = home_link+ link    
                        info = parse_link(link,reg[9],reg[10],reg[11],reg[12],test)
                        if info is not None:
                            writer.writerow(info)
                        if test == 1:
                            exit()
                        
                else: 
                    raise ValueError(response.status_code)
    except ValueError as e:
        print(e)

def parse_page_from_url_list(reg,test):
    try:
        #university
        reg[0]='Pontificia Universidad Javeriana'
        #home
        reg[4]='https://www.javeriana.edu.co/'
        #complete_url
        reg[6] = 1
        #title
        reg[9] = '//h2[@class="font-weight-bold mb-md-0"]/div/text()'
        #modality
        reg[10] = ''
        #duration
        reg[11] = '//div[contains(text(),"HORAS")]/text()'
        #cost
        reg[12] = '//span[@class="course-price"]/div/text()'

        university_name = reg[0]
        home_link = reg[4]
        article_link = reg[5]
        complete_url = reg[6]
        no_pages = reg[7]
        xpath_article = reg[8]

        if test == 1:
            print('university_name = '+university_name)
            print('home_link = '+home_link)
            print('article_link = '+article_link)
            print('complete_url = '+str(complete_url))
            print('xpath_article = '+xpath_article)
            dir_location = 'test'
        else:
            dir_location = 'prod'

        url_uni = 'csv/'+dir_location+'/    '+university_name+'.csv'
        with open(url_uni, 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            flist =open("url_list/"+university_name+".txt",encoding="utf-8")
            for element in flist:
                if(complete_url == 0):
                    link = reg[4] + element[1:-2]
                else:
                    link = element[1:-2]
                info = parse_link(link,reg[9],reg[10],reg[11],reg[12],test)
                if info is not None:
                    writer.writerow(info)
                    if test == 1:
                        exit()
    except ValueError as e:
        print(e)


