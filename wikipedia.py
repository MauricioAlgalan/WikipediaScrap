#!/usr/bin/env python

""" Script para bajar solo el articulo de la pagina de wikipedia|

"""


import requests
from lxml import html
import urlparse
import sys
import validators

def sep(pagina=''):
    """ La base para imagenes es http://  """
    base_img='https://'
    """ La base para las almoadillas # es la pagina """
    base_section=pagina
    try:
        pagina=html.fromstring(requests.get(pagina).text).xpath('//div[@id="bodyContent"]')[0]
    except:
        sys.exit(1)
    
    for imgs in pagina.xpath('//img'):
        try:
            imgs.attrib["src"]=urlparse.urljoin(base_img,imgs.attrib["src"])
        except:
            continue
    for links in pagina.xpath('//a'):
        try:
            if links.attrib["href"].startswith('#'):
                continue
            links.attrib["href"]=urlparse.urljoin(base_section,links.attrib["href"])
        except:
            continue
    archivo=open('out.html','w')
    archivo.write(html.tostring(pagina))
    archivo.close()
    

if __name__=='__main__':
    argumentos=sys.argv
    if validators.url(sys.argv[1]):
        sep(sys.argv[1])
    else:
        if validators.domain(sys.argv[1]):
            sep('http://'+sys.argv[1])
    #busqueda=''
    #for x in argumentos[1:]:
        #busqueda=str(x)+'+'
    #if busqueda=='':
        #listax()
    #else:
        #listax(busqueda)

