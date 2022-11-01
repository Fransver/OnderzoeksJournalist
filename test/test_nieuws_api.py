from datacollector_application.business_layer.api_data_collector.nieuws_api import NewsAPI


class TestNieuwsApi:
    news_api_test = NewsAPI()
    client = news_api_test.client

    def test_if_sources_status_ok(self):
        # =========================== Implementaties
        sources = self.client.get_sources()
        status = sources.get('status')

        assert status == 'ok'

    def test_if_sources_holds_articles(self):
        # ========================== Implementaties
        sources = self.news_api_test.get_sources()
        sources_sources = sources.get('sources')  # Without id tag
        length = len(sources_sources)  # Aantal artikelen
        print(length)
        assert length >= 1

    def test_to_search_by_subject_ukraine(self):
        subject = 'Ukraine'
        result_subject = self.news_api_test.get_subject_news(subject)
        assert result_subject.get('status') == 'ok'
        assert result_subject.get('totalResults') >= 1
