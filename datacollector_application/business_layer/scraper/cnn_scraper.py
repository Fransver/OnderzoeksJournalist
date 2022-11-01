import datetime

from datacollector_application.business_layer.helpers.date_collector import DateCollector
from datacollector_application.business_layer.model.article import Article
from datacollector_application.business_layer.scraper.scraper_interface import BeautifulParent

dates = DateCollector().get_range_of_dates(starting_date=datetime.date(2022, 10, 5))
list_of_lists = []


class CnnScraper(BeautifulParent):
    def __init__(self):
        super().__init__()
        self.url = "https://edition.cnn.com/articles/"

    def scrape(self, dates_cnn, descr=True):

        for date in dates_cnn:
            soup = self.soup(self.req.get(self.url).content, 'html.parser')
            titles = soup.find_all('h3', class_='cd__headline')

            for i in range(len(titles)):
                title = titles[i].text
                url = "".join(["https://edition.cnn.com/", titles[i].a['href']])  # a class geselecteerd

                if descr:
                    description = self.get_description(url)
                else:
                    description = ""

                article_cnn = Article(title, date, url, description)
                self.articles.append(article_cnn)

        return self.articles

    def get_description(self, url):
        req = self.req.get(url)
        soup = self.soup(req.content, 'html.parser').head
        description = soup.select_one('meta[name="description"]').attrs['content']

        return description

    def check_if_field_is_empty(self):
        pass


scraper_cnn = CnnScraper()

if __name__ == '__main__':
    articles = scraper_cnn.scrape(dates, descr=False)

    for article in articles:
        list_of_attribute_values = [article.title, article.description, article.date, article.url]
        list_of_lists.append(list_of_attribute_values)
        print(f"title: {article.title}\ndate: {article.date}\ndescription: {article.description}\nurl: {article.url}\n")
