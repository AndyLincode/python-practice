import bs4
import requests

result = requests.get(
    "https://zh.wikipedia.org/zh-tw/%E5%93%88%E5%88%A9%C2%B7%E6%B3%A2%E7%89%B9")
soup = bs4.BeautifulSoup(result.text, 'lxml')

images_list = soup.select("img.mw-file-element")

target_image = ""
for image in images_list:
    if image["data-file-width"] == "640":
        target_image = image

result2 = requests.get(f"https:{target_image['src']}")

with open("harry_image.jpg", "wb") as f:
    f.write(result2.content)
