import bs4
import requests
from bs4 import BeautifulSoup as soup

class works():
    def __init__(self, id=None):
        #If the user specified a work id
        if id != None:
            self.has_found_page = False
            self.warning_level = 0
            while self.has_found_page != True:
                self.id = str(id)
                self.page = requests.get("https://batmanwonderwoman.com/fanfiction/viewstory.php?sid=" + self.id + '&warning=' + str(self.warning_level)).text
                self.page_for_url = requests.get("https://batmanwonderwoman.com/fanfiction/viewstory.php?sid=" + self.id + '&warning=' + str(self.warning_level))
                self.soup = soup(self.page, "html.parser")
                try:
                    self.url = self.page_for_url.url
                    self.title = self.soup.find(id='pagetitle').a.string
                    try:
                        self.story_notes = self.soup.find(class_='noteinfo').p.string
                    except:
                        self.story_notes = 'This story has no story notes'
                    else:
                        pass
                except AttributeError:
                    self.warning_level += 1
                    if self.warning_level >= 10:
                        print('There are no works with the id given.')
                        break
                else:
                    if self.title != None:
                        self.url = self.page_for_url.url
                        self.title = self.soup.find(id='pagetitle').a.string
                        self.has_found_page = True
                        self.author = self.soup.select('#pagetitle a')[-1].text
                        self.summary = self.soup.select('.content p')[-1].text
                        self.chapters = self.soup.select('.label')[8].next_element.next_element
                        self.completed = self.soup.select('.label')[9].next_element.next_element
                        self.words = self.soup.select('.label')[10].next_element.next_element
                        self.read = self.soup.select('.label')[11].next_element.next_element
                        self.published = self.soup.select('.label')[12].next_element.next_element
                        self.updated = self.soup.select('.label')[13].next_element.next_element
                        self.reviews = self.soup.select('#sort a')[1].text
                        self.complete_info = self.soup.select('.content')[-1].text
                        break
        else:
            self.page_for_random_story = requests.get('https://batmanwonderwoman.com/fanfiction/').text
            self.soup_random = soup(self.page_for_random_story, 'html.parser')
            self.random_story = self.soup_random.select('.content ul')[1].text
            self.random_story_href = self.soup_random.select('.content ul li a')[3]
            self.url_list = str(self.random_story_href).split()
            try:
                for item in self.url_list:
                    if 'sid=' in item:
                        self.rand_id = item.split('"')[1].split('=')[1]
                self.random_story_url = f'https://batmanwonderwoman.com/fanfiction/viewstory.php?sid={self.rand_id}'
            except:
                print(f"Couldn't get this stories url, getting the href: {self.random_story_href}")
                self.random_story_url = ''
                self.rand_id = ''
