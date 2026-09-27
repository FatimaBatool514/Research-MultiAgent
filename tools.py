import os

from crewai_tools import SerperDevTool, ScrapeWebsiteTool


def get_search_tool():
    if not os.getenv("SERPER_API_KEY"):
        raise ValueError(
            "SERPER_API_KEY is missing. Add it to Streamlit Secrets."
        )

    return SerperDevTool()


def get_scraper_tool():
    return ScrapeWebsiteTool()
