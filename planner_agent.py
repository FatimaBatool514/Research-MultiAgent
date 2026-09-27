from crewai import Agent

from llm import get_llm


def create_planner_agent():

    return Agent(
        role="Senior Research Planning Specialist",

        goal=(
            "Transform a research topic into a clear, rigorous and "
            "well-structured research plan."
        ),

        backstory=(
            "You are an experienced research strategist with expertise "
            "in academic research, literature reviews, research design, "
            "and research question formulation. You carefully break "
            "complex topics into manageable research questions."
        ),

        llm=get_llm(),

        allow_delegation=False,

        verbose=True,
    )
