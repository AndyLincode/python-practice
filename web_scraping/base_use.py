from bs4 import BeautifulSoup

text = """<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Web Scraping HTML</title>
</head>

<body>
  <h1 class="title web-title">Web Scraping</h1>

  <div class="container">
    <p class="text-1 align-center">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dignissimos tenetur esse
      est
      rerum iure eveniet aut neque saepe hic quos. Incidunt id, unde qui reprehenderit officia adipisci nisi fugit
      porro?</p>
    <p class="text-2 align-center">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Veritatis, culpa.</p>
    <p class="text-3 align-center">Lorem ipsum dolor sit amet.</p>
  </div>
  <h2 class="sub-title web-sub-title">Sub Title</h2>
  <div class="second-group">
    <p class="text-3 with-span">Hi ,<span class="span-in-p text-red-800">Scraping</span></p>
  </div>
</body>

</html>"""

soup = BeautifulSoup(text, 'lxml')
print(soup.find("h2"))
print(soup.find_all("p"))
# <h2 class="sub-title web-sub-title">Sub Title</h2>
# [<p class="text-1 align-center">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dignissimos tenetur esse
#       est
#       rerum iure eveniet aut neque saepe hic quos. Incidunt id, unde qui reprehenderit officia adipisci nisi fugit
#       porro?</p>, <p class="text-2 align-center">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Veritatis, culpa.</p>, <p class="text-3 align-center">Lorem ipsum dolor sit amet.</p>, <p class="text-3 with-span">Hi ,<span class="span-in-p text-red-800">Scraping</span></p>]

first_p_tag = soup.find_all("p")[0]
print(first_p_tag.get("class"))
print(first_p_tag.getText())
# ['text-1', 'align-center']
# Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dignissimos tenetur esse
#       est
#       rerum iure eveniet aut neque saepe hic quos. Incidunt id, unde qui reprehenderit officia adipisci nisi fugit
#       porro?
print(first_p_tag["class"])
# ['text-1', 'align-center']
