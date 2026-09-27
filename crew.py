from crewai import Crew, Process, Task

from planner_agent import create_planner_agent
from researcher_agent import create_researcher_agent
from academic_agent import create_academic_agent
from validator_agent import create_validator_agent
from writer_agent import create_writer_agent


def create_research_crew():

    planner = create_planner_agent()
    researcher = create_researcher_agent()
    academic = create_academic_agent()
    validator = create_validator_agent()
    writer = create_writer_agent()

    planning_task = Task(
        description="""
        Create a detailed research plan for the following topic:

        {topic}

        Research type:
        {research_type}

        Research depth:
        {depth}

        Provide:
        1. Main research question
        2. Important sub-questions
        3. Key concepts
        4. Important keywords
        5. Evidence that should be collected
        6. Potential theoretical perspectives
        7. Areas requiring recent research
        """,

        expected_output=(
            "A detailed and logically organized research plan "
            "containing research questions, keywords, concepts "
            "and evidence requirements."
        ),

        agent=planner,
    )

    research_task = Task(
        description="""
        Using the research plan below, conduct comprehensive web research.

        Research Plan:
        {planning_task}

        Find reliable and relevant information.

        Requirements:
        - Use the search tool.
        - Use web pages when useful.
        - Prefer authoritative and recent sources.
        - Search multiple queries.
        - Record source titles and URLs when available.
        - Do not fabricate sources.
        - Clearly distinguish evidence from interpretation.
        """,

        expected_output=(
            "A detailed research evidence report containing source "
            "information, findings, important facts and URLs."
        ),

        agent=researcher,

        context=[planning_task],
    )

    academic_task = Task(
        description="""
        Analyze the research evidence below.

        Research Evidence:
        {research_task}

        Identify:

        1. Major themes
        2. Important theories
        3. Variables and relationships
        4. Research methodologies
        5. Major findings
        6. Areas of agreement
        7. Areas of disagreement
        8. Limitations
        9. Research gaps
        10. Potential future research directions

        Do not invent studies or findings.
        """,

        expected_output=(
            "A critical academic analysis of the collected evidence "
            "including themes, theories, findings and research gaps."
        ),

        agent=academic,

        context=[planning_task, research_task],
    )

    validation_task = Task(
        description="""
        Critically validate the research materials.

        Research Evidence:
        {research_task}

        Academic Analysis:
        {academic_task}

        Check:

        - Unsupported claims
        - Weak evidence
        - Questionable sources
        - Contradictions
        - Overgeneralizations
        - Missing evidence
        - Citation/source problems

        Create a list of:
        1. Validated findings
        2. Findings requiring caution
        3. Unsupported claims to remove
        4. Additional research needed

        Never create fake citations.
        """,

        expected_output=(
            "A research quality-control report clearly identifying "
            "validated evidence, limitations and claims requiring "
            "additional verification."
        ),

        agent=validator,

        context=[research_task, academic_task],
    )

    writing_task = Task(
        description="""
        Write the final research report using the validated material.

        Topic:
        {topic}

        Research Type:
        {research_type}

        Academic Analysis:
        {academic_task}

        Validation Report:
        {validation_task}

        Research Evidence:
        {research_task}

        Requirements:

        - Use clear academic language.
        - Organize the report with useful headings.
        - Maintain logical flow.
        - Do not invent citations.
        - Do not introduce unsupported claims.
        - Preserve important source URLs.
        - Clearly identify research gaps.
        - Make the report useful for a researcher.
        """,

        expected_output=(
            "A polished, structured research report based strictly "
            "on the validated evidence."
        ),

        agent=writer,

        context=[
            planning_task,
            research_task,
            academic_task,
            validation_task,
        ],
    )

    crew = Crew(
        agents=[
            planner,
            researcher,
            academic,
            validator,
            writer,
        ],

        tasks=[
            planning_task,
            research_task,
            academic_task,
            validation_task,
            writing_task,
        ],

        process=Process.sequential,

        verbose=True,
    )

    return crew
