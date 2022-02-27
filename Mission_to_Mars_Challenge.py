
# import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


executable_path = {'executable_path' : ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless = False)


# visit the mars NASA news site
url = 'https://redplanetscience.com'
browser.visit(url)

# optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time = 1)



html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


slide_elem.find('div', class_='content_title')


# use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title



# use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images


# visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)




# find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[9]:


# parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[10]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[11]:


# use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[12]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns = ['description', 'Mars', 'Earth']
df.set_index('description', inplace = True)
df



df.to_html()


# ## D1 : Hemispheres



# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range(4):
    hemispheres = {}
    click_link = browser.find_by_tag('h3')[i].click()

    html = browser.html
    img_soup = soup(html, 'html.parser')

    title = img_soup.find('h2', class_= 'title').text

    html_element = browser.find_by_text('Sample').first
    get_link = html_element['href']
    
    hemispheres['img_url'] = get_link
    hemispheres['title'] = title
    hemisphere_image_urls.append(hemispheres)
    
    browser.back()
    


# In[58]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[59]:


# 5. Quit the browser
browser.quit()


# In[ ]:




