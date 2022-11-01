import requests

from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

# INTERFACE om abstractie aan te brengen voor eventuele uitbreiden aantal/soorten scrapers
# ========================================================================================


class Scraper(ABC):  # Hier de blauwdruk van de scraper maken waarin variabel datum-lijst nog optioneel is.
    @abstractmethod
    def scrape(self, *args):
        pass


class BeautifulParent(Scraper):  # De Beutiful Soup scrapers gebruiken allemaal de soup en requests. Dus meegegeven.
    def __init__(self):
        super().__init__()
        self.articles = []
        self.soup = BeautifulSoup
        self.req = requests

    def scrape(self, dates_scraper):  # Hier al aangeven dat een Beuautiful Soup scraper een lijst data moet hebben.
        pass
