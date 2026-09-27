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

    # ---------------------------------------------------------
    # TASK 1: RESEARCH PLANNING
    # ---------------------------------------------------------

    planning_task = Task(
        description="""
        Create a detailed research plan for the following topic:

        Topic:
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

        Make the plan specific to the research topic.
        """,

        expected_output="""
        A detailed and logically organized research plan containing:

        - Main research question
        - Sub-questions
        - Key concepts
        - Search keywords
        - Evidence requirements
        - Relevant theoretical perspectives
        - Areas requiring recent research
        """,

        agent=planner,
    )

    # ---------------------------------------------------------
    # TASK 2: WEB RESEARCH
    # ---------------------------------------------------------

    research_task = Task(
        description="""
        Conduct comprehensive web research based on the research
        planning information provided in your context.

        Requirements:

        - Use the web search tool.
        - Use web pages when useful.
        - Search multiple queries.
        - Prefer authoritative and recent sources.
        - Look for academic, institutional and industry sources
          where appropriate.
        - Record source titles and URLs when available.
        - Extract useful evidence and findings.
        - Do not fabricate sources.
        - Clearly distinguish evidence from interpretation.
        """,

        expected_output="""
        A detailed research evidence report containing:

        - Important findings
        - Key facts
        - Relevant studies or reports
        - Source titles
        - Source URLs
        - Evidence supporting major findings
        - Conflicting evidence where applicable
        """,

        agent=researcher,
        context=[planning_task],
    )

    # ---------------------------------------------------------
    # TASK 3: ACADEMIC ANALYSIS
    # ---------------------------------------------------------

    academic_task = Task(
        description="""
        Analyze the research evidence provided in your context.

        Conduct a critical academic analysis.

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

        Do not invent studies, findings or citations.

        Base the analysis only on the research evidence available
        in your context.
        """,

        expected_output="""
        A critical academic analysis of the collected research
        evidence including:

        - Major themes
        - Theories
        - Variables
        - Methodologies
        - Major findings
        - Agreements and disagreements
        - Limitations
        - Research gaps
        - Future research directions
        """,

        agent=academic,
        context=[research_task],
    )

    # ---------------------------------------------------------
    # TASK 4: VALIDATION
    # ---------------------------------------------------------

    validation_task = Task(
        description="""
        Critically validate the research evidence and academic
        analysis provided in your context.

        Check for:

        - Unsupported claims
        - Weak evidence
        - Questionable sources
        - Contradictions
        - Overgeneralizations
        - Missing evidence
        - Citation problems
        - Claims that require additional verification

        Create four sections:

        1. Validated findings
        2. Findings requiring caution
        3. Unsupported claims to remove
        4. Additional research or verification needed

        Never create fake citations or sources.
        """,

        expected_output="""
        A research quality-control report containing:

        1. Validated findings
        2. Findings requiring caution
        3. Unsupported claims
        4. Additional verification needed
        5. Source and citation concerns
        """,

        agent=validator,
        context=[research_task, academic_task],
    )

    # ---------------------------------------------------------
    # TASK 5: FINAL WRITING
    # ---------------------------------------------------------

    writing_task = Task(
        description="""
        Write the final research report using the research evidence,
        academic analysis and validation information provided in
        your context.

        Topic:
        {topic}

        Research Type:
        {research_type}

        Requirements:

        - Use clear academic language.
        - Organize the report with useful headings.
        - Maintain logical flow.
        - Do not invent citations.
        - Do not introduce unsupported claims.
        - Preserve important source URLs.
        - Clearly identify research gaps.
        - Distinguish established findings from areas of uncertainty.
        - Base the report strictly on the validated research material.

        Produce a useful report for a researcher.
        """,

        expected_output="""
        A polished and structured academic research report containing:

        - Introduction
        - Major findings/themes
        - Critical analysis
        - Relevant theories and variables
        - Research evidence
        - Limitations
        - Research gaps
        - Future research directions
        - Source URLs where available
        """,

        agent=writer,
        context=[
            research_task,
            academic_task,
            validation_task,
        ],
    )

    # ---------------------------------------------------------
    # CREATE CREW
    # ---------------------------------------------------------

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
