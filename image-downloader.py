import random
import urllib.request

def download_image(url):
	name = random.randrange(1,100)
	file_name = str(name) + ".jpg"
	urllib.request.urlretrieve(url,file_name)

print("Enter the URL:-")
x = input()
download_image(x)
print("Image Downloaded Please Check Folder")