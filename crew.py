from crewai import Crew,Process
from tasks import research_task,write_task
from agents import news_researcher,writer


## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[news_researcher,writer],
    tasks=[research_task,write_task, ],
    process=Process.sequential,
    

)


link = input("Enter the link\n:")
result=crew.kickoff(inputs={'link':link})
print(result)

