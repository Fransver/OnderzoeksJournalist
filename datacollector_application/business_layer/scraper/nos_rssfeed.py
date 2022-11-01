import datetime
from datacollector_application.business_layer.scraper.scraper_interface import BeautifulParent
from datacollector_application.business_layer.model.article import Article


class NosRssScraper(BeautifulParent):
    def __init__(self):
        super().__init__()
        self.url = "https://feeds.nos.nl/nosnieuwsbinnenland/"

    def scrape(self, dates_scraper, descr=False):
        soup = self.soup(self.req.get(self.url).content, 'lxml')
        urls = soup.find_all('guid')
        titles = soup.find_all('title')

        print(titles)

        for i in range(len(titles)):
            title = titles[i].text
            url = urls[0].text # 1e artikel heeft geen url dus klopt niet in volgorde.
            date = ''
            descriptions = ''
            article = Article(title, date, url, descriptions)
            self.articles.append(article)
            print(f"title: {article.title}\nurl: {article.url}\n"
                  f"description: {article.description}\ndate: {article.date}\n")

        return self.articles


if __name__ == '__main__':
    titles = []
    today = datetime.date.today()
    scraper_rss = NosRssScraper()
    scraper_rss.scrape(today)

