from crewai import Task
from tools import tool
from agents import news_researcher, writer

# Research task
research_task = Task(
    description="Scrape the content from the website link provided by the user.",
    expected_output="Extracted content from the provided website link.",
    tools=[tool],
    agent=news_researcher,
)

# Writing task with language model configuration
write_task = Task(
    description=(
        """
        Summarize the content from {link} using the following markdown format:
        '''
        *Title*
        Summarize the AI applications mentioned in 10-15 lines include Advantages and disadvantages.
        *More Details:* {link}
        '''

        Ensure that the sentences that are there in prompts should not be there in the Output
        Ensure the summary follows this structure and does not start with "This article is about..."
        Ensure the summary follows this structure and does not start with "The article discusses..."
        Ensure the summary follows this structure and does not start with "This article..."
        Review the format and example provided by the critic agent before finalizing the output.
        """
    ),
    expected_output="Summary of the content following the specified format.",
    agent=writer,
    async_execution=False,
    output_file="output.md"
)
