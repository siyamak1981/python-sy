import requests
import urllib

# req = urllib.request.urlopen('https://zerotohero.ir/')
# print(req.status)




#  imagefile
# url = 'https://www.python.org/static/opengraph-icon-200x200.png'
# urllib.request.urlretrieve(url, "image-urllib.png")
# با استفاده از request

# url = 'https://www.python.org/static/opengraph-icon-200x200.png'
# x = requests.get(url)
# with open("poing.png", "wb") as file:
#     file.write(x.content)

# PDF
# url = 'https://media.readthedocs.org/pdf/urllib3/latest/urllib3.pdf'
# urllib.request.urlretrieve(url, "pdf-urllib.pdf")



# url = 'https://media.readthedocs.org/pdf/urllib3/latest/urllib3.pdf'
# s = requests.get(url)
# with open("poing2.pdf", "wb") as filezip:
#     filezip.write(s.content)


# FILEZIPE
 
url = 'https://docs.python.org/2/archives/python-2.7.14-docs-pdf-a4.zip'
urllib.request.urlretrieve(url, "zip-urllib.zip")

