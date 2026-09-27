import os

try:
    import crewai.llms.cache as crew_cache

    crew_cache.mark_cache_breakpoint = lambda msg: msg

except Exception:
    pass

from crewai import LLM


MODEL_NAME = "groq/openai/gpt-oss-120b"


def get_llm():

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. Add it to Streamlit Secrets."
        )

    return LLM(
        model=MODEL_NAME,
        api_key=api_key,
        temperature=0.1,
        max_tokens=1200,
    )
