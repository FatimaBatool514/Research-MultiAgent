from crewai import Agent

from llm import get_llm


def create_writer_agent():

    return Agent(
        role="Senior Academic Research Writer",

        goal=(
            "Produce a clear, rigorous, well-structured research report "
            "using only the validated research evidence provided."
        ),

        backstory=(
            "You are an experienced academic writer specializing in "
            "research papers, literature reviews, research proposals "
            "and scholarly reports. You write logically, avoid "
            "unsupported claims and maintain academic clarity."
        ),

        llm=get_llm(),

        allow_delegation=False,

        verbose=True,
    )
