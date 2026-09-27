from crewai import Agent

from llm import get_llm
from tools import get_search_tool, get_scraper_tool


def create_researcher_agent():

    return Agent(
        role="Senior Web Research Specialist",

        goal=(
            "Find high-quality, relevant and recent information from "
            "reliable online sources and provide evidence-backed findings."
        ),

        backstory=(
            "You are an expert online researcher. You know how to "
            "formulate effective search queries, identify authoritative "
            "sources, extract relevant information, compare sources, "
            "and distinguish reliable evidence from weak sources."
        ),

        tools=[
            get_search_tool(),
            get_scraper_tool(),
        ],

        llm=get_llm(),

        allow_delegation=False,

        verbose=True,
    )
