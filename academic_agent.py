from crewai import Agent

from llm import get_llm


def create_academic_agent():

    return Agent(
        role="Academic Research Analyst",

        goal=(
            "Analyze collected research evidence, identify major themes, "
            "theories, variables, methodologies, findings, limitations "
            "and research gaps."
        ),

        backstory=(
            "You are a senior academic researcher experienced in "
            "literature reviews, theoretical frameworks, empirical "
            "research and research methodology. You critically compare "
            "studies instead of simply summarizing them."
        ),

        llm=get_llm(),

        allow_delegation=False,

        verbose=True,
    )
