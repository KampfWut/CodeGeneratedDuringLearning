from bs4 import BeautifulSoup

soup = BeautifulSoup(open("12_UseHtml.html"), "lxml")

print("> All html:\n")
print(soup.prettify)

print("\n> 1. First ul:\n")
print(soup.ul)
print(soup.find('ul'))

print("\n> 2. All ul:\n")
print(soup.find_all('ul'))
print("\n>   a. in this , fisrt ul is \n")
print(soup.find_all('ul')[0])
print("\n>   b. in this , second ul is \n")
print(soup.find_all('ul')[1])

print("\n> 3. Find 3 li:\n")
print(soup.find('li', attrs={'nu':'3'}))

print("\n> 4. Find \"mo shan\" price:\n")
Tag = soup.find_all('a', attrs={'class':'price'})
print(Tag[1])

print("\n> 5. Get 4 message:\n")
Tag = soup.find('li', attrs={'nu':'4'})
print(Tag.get('nu'))
print(Tag.find('a').get_text())