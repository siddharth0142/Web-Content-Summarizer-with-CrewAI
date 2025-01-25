from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os


# call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           max_tokens=None,
                           temperature=0.5,
                           timeout=None,
                           google_api_key=os.getenv("GOOGLE_API_KEY")
)


# Creating a senior researcher agent with memory and verbose mode

news_researcher=Agent(
    role="Senior Scraper",
    goal='Scrape the content from the given url {link}',
    verbose=True,
    memory=True,
    backstory=(
        """use the WebsiteSearchTool to then scrape the content, and provide the full content to the writer agent so it can then be summarized
        """

    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

## creating a write agent with custom tools responsible in writing news blog
writer = Agent(
  role='Content summarizer',
  goal='write a summary for the content passed to you',
  verbose=True,
  memory=True,
  backstory=(
    """You are a renowned Content Creator, known for your insightful and engaging articles.
      You transform complex concepts into compelling narratives.
      
      """
  ),
  llm=llm,
  allow_delegation=False
)
