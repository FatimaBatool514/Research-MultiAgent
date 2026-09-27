from crewai import Agent

from llm import get_llm


def create_validator_agent():

    return Agent(
        role="Research Quality and Citation Validator",

        goal=(
            "Critically examine research findings and identify "
            "unsupported claims, weak evidence, inconsistencies, "
            "questionable sources and citation problems."
        ),

        backstory=(
            "You are a meticulous academic reviewer. You inspect "
            "research outputs for unsupported claims, logical gaps, "
            "overstatements and poor source quality. You never invent "
            "citations and clearly identify information that requires "
            "additional verification."
        ),

        llm=get_llm(),

        allow_delegation=False,

        verbose=True,
    )
