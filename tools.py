from crewai_tools import ScrapeWebsiteTool

from dotenv import load_dotenv
load_dotenv()
import os

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

# To enable scrapping any website it finds during it's execution
tool = ScrapeWebsiteTool()