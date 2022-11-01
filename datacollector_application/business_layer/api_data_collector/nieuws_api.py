import json
import time
import pandas as pd

from newsapi import NewsApiClient  # Api direct vanaf documentatie


class NewsAPI:
    def __init__(self):
        self.client = NewsApiClient(api_key='43136ce0aa7047fd83aa71a25633260f')

    def get_sources(self):
        sources_newsapi = self.client.get_sources()
        return sources_newsapi

    def get_top_headlines(self):
        headlines_newsapi = self.client.get_top_headlines()
        return headlines_newsapi

    def get_subject_news(self, subject):
        subject_newsapi = self.client.get_everything(qintitle=f"{subject}")
        return subject_newsapi


# ================= Dataframes
# df_bitcoin = pd.DataFrame(data=bitcoin)  # Naar panda Data
# df_topus = pd.DataFrame(data=top_us)

# ================== Json dumps


if __name__ == '__main__':
    news_api = NewsAPI()

    sources = news_api.get_sources()
    headlines = news_api.get_top_headlines()
    subject_news = news_api.get_subject_news("Ukraine")

    start_time = time.time()
    print(sources)
    end_time = time.time()
    duration = end_time - start_time
    print(duration)
