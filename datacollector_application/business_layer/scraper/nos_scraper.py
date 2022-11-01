from datacollector_application.business_layer.model.article import Article
from datacollector_application.business_layer.scraper.scraper_interface import BeautifulParent


class NosScraper(BeautifulParent):
    def __init__(self):
        super().__init__()
        self.url = "https://nos.nl/nieuws/archief/{}-{}-{}"

    def scrape(self, dates, descr=True):

        for date in dates:
            url = self.url.format(date.year, date.strftime('%m'), date.strftime('%d'))
            soup = self.soup(self.req.get(url).content, 'html.parser')
            titles = soup.find_all('div', class_='list-time__title')
            urls = soup.find_all('a', class_='link-block')

            for i in range(len(titles)):
                title = titles[i].contents[0]
                url = "".join(["https://www.nos.nl", urls[i].attrs['href']])

                if descr:
                    description = self.get_description(url)
                else:
                    description = ""

                if self.scrape_complete_text:
                    text = self.get_article_text(url)
                else:
                    text = ""

                article = Article(title, date, url, description, text)
                self.articles.append(article)

        return self.articles

    def get_description(self, url):
        req = self.req.get(url)
        soup = self.soup(req.content, 'html.parser').head
        description = soup.select_one('meta[name="description"]').attrs['content']

        return description

    def get_article_text(self, url):
        req = self.req.get(url)
        soup = self.soup(req.content, 'html.parser')
        list_of_text = soup.find_all('p', attrs={"data-testid": "text"})
        text = ""

        for t in list_of_text:
            if isinstance(t, Tag):
                if isinstance(t.contents[0], str):
                    text += t.contents[0]
                    text += " "
                elif isinstance(t.contents[0].contents[0], str):
                    text += t.contents[0].contents[0]
                    text += " "

        return text

    def check_if_field_is_empty(self):
        pass
