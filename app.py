import streamlit as st

from crew import create_research_crew


# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="ResearchAI",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    /* ---------- GLOBAL ---------- */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(99, 102, 241, 0.12),
                transparent 28%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(6, 182, 212, 0.10),
                transparent 25%
            ),
            #080b14;
        color: #f8fafc;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* ---------- HEADER ---------- */

    .hero {
        padding: 2.5rem 2.5rem 2.2rem 2.5rem;
        border-radius: 28px;
        background:
            linear-gradient(
                135deg,
                rgba(99, 102, 241, 0.18),
                rgba(14, 165, 233, 0.10)
            );
        border: 1px solid rgba(255,255,255,0.08);
        margin-bottom: 1.5rem;
        box-shadow: 0 20px 70px rgba(0,0,0,0.25);
    }

    .hero-badge {
        display: inline-block;
        padding: 0.35rem 0.8rem;
        border-radius: 999px;
        background: rgba(99,102,241,0.15);
        border: 1px solid rgba(129,140,248,0.25);
        color: #c7d2fe;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }

    .hero h1 {
        font-size: 3.2rem;
        line-height: 1.05;
        margin: 1rem 0 0.8rem 0;
        font-weight: 800;
        letter-spacing: -0.04em;
    }

    .hero p {
        color: #a5b4fc;
        font-size: 1.05rem;
        max-width: 750px;
        line-height: 1.7;
    }

    /* ---------- CARDS ---------- */

    .glass-card {
        background: rgba(15, 23, 42, 0.68);
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: 22px;
        padding: 1.25rem;
        box-shadow: 0 15px 50px rgba(0,0,0,0.18);
        backdrop-filter: blur(16px);
    }

    .metric-card {
        background: rgba(15,23,42,0.75);
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: 18px;
        padding: 1rem;
        text-align: center;
    }

    .metric-number {
        font-size: 1.8rem;
        font-weight: 800;
    }

    .metric-label {
        color: #94a3b8;
        font-size: 0.8rem;
    }

    /* ---------- AGENTS ---------- */

    .agent-card {
        display: flex;
        align-items: center;
        gap: 14px;
        padding: 13px 15px;
        margin-bottom: 10px;
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.06);
        background: rgba(15,23,42,0.55);
    }

    .agent-card.active {
        border: 1px solid rgba(99,102,241,0.5);
        background: rgba(79,70,229,0.12);
        box-shadow: 0 0 25px rgba(99,102,241,0.12);
    }

    .agent-card.done {
        border: 1px solid rgba(34,197,94,0.25);
        background: rgba(34,197,94,0.06);
    }

    .agent-icon {
        width: 38px;
        height: 38px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(255,255,255,0.06);
        font-size: 1.1rem;
    }

    .agent-name {
        font-weight: 700;
        font-size: 0.92rem;
    }

    .agent-status {
        color: #94a3b8;
        font-size: 0.76rem;
        margin-top: 2px;
    }

    /* ---------- OUTPUT ---------- */

    .result-header {
        padding: 1rem 1.2rem;
        border-radius: 16px;
        background: rgba(99,102,241,0.10);
        border: 1px solid rgba(99,102,241,0.15);
        margin-bottom: 1rem;
    }

    /* ---------- BUTTON ---------- */

    .stButton > button {
        width: 100%;
        border-radius: 14px;
        min-height: 3.1rem;
        font-weight: 750;
        border: 1px solid rgba(255,255,255,0.1);
    }

    /* ---------- SIDEBAR ---------- */

    section[data-testid="stSidebar"] {
        background: #090d18;
        border-right: 1px solid rgba(255,255,255,0.06);
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# HERO
# ---------------------------------------------------------

st.markdown(
    """
    <div class="hero">

        <span class="hero-badge">AI Research Workspace</span>

        <h1>ResearchAI 🔬</h1>

        <p>
            A multi-agent research team powered by CrewAI and Groq.
            Plan research, discover evidence, analyze academic findings,
            validate sources, and generate a structured research report.
        </p>

    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.markdown("## ⚙️ Research Settings")

    research_type = st.selectbox(
        "Research type",
        [
            "Literature Review",
            "Research Proposal",
            "Research Gap Analysis",
            "Research Paper",
            "Theoretical Framework",
            "General Research Report",
        ],
    )

    depth = st.selectbox(
        "Research depth",
        [
            "Quick",
            "Standard",
            "Deep",
        ],
        index=1,
    )

    st.markdown("---")

    st.markdown("### 🤖 Research Team")

    st.markdown(
        """
        **5 specialized agents**

        🧭 Research Planner  
        🔎 Web Researcher  
        📚 Academic Analyst  
        🛡️ Citation Validator  
        ✍️ Research Writer
        """
    )

    st.markdown("---")

    st.caption(
        "Powered by CrewAI + Groq GPT-OSS 120B"
    )


# ---------------------------------------------------------
# MAIN INPUT
# ---------------------------------------------------------

st.markdown("### What do you want to research?")

topic = st.text_area(
    "Research topic",
    placeholder=(
        "Example: Impact of Artificial Intelligence on "
        "Project Cost Management"
    ),
    height=130,
    label_visibility="collapsed",
)


col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-number">05</div>
            <div class="metric-label">Specialized Agents</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-number">02</div>
            <div class="metric-label">Research Tools</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-number">01</div>
            <div class="metric-label">Unified Report</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown("")


# ---------------------------------------------------------
# AGENT UI
# ---------------------------------------------------------

agents = [
    ("🧭", "Research Planner"),
    ("🔎", "Web Researcher"),
    ("📚", "Academic Analyst"),
    ("🛡️", "Citation Validator"),
    ("✍️", "Research Writer"),
]


def render_agents(active_index=-1, completed_index=-1):

    html = ""

    for i, (icon, name) in enumerate(agents):

        if i == active_index:
            css_class = "agent-card active"
            status = "● Working now"

        elif i <= completed_index:
            css_class = "agent-card done"
            status = "✓ Completed"

        else:
            css_class = "agent-card"
            status = "○ Waiting"

        html += f"""
        <div class="{css_class}">
            <div class="agent-icon">{icon}</div>

            <div>
                <div class="agent-name">{name}</div>
                <div class="agent-status">{status}</div>
            </div>
        </div>
        """

    return html


st.markdown("### 🤖 Agent Activity")

agent_placeholder = st.empty()

agent_placeholder.markdown(
    render_agents(),
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# START BUTTON
# ---------------------------------------------------------

start = st.button(
    "🚀 Start Research",
    type="primary",
)


# ---------------------------------------------------------
# RUN CREW
# ---------------------------------------------------------

if start:

    if not topic.strip():

        st.warning(
            "Please enter a research topic first."
        )

        st.stop()

    progress = st.progress(0)

    status_box = st.empty()

    try:

        # -----------------------------
        # Agent 1
        # -----------------------------

        agent_placeholder.markdown(
            render_agents(
                active_index=0,
                completed_index=-1,
            ),
            unsafe_allow_html=True,
        )

        status_box.info(
            "🧭 Research Planner is creating the research strategy..."
        )

        progress.progress(10)

        crew = create_research_crew()

        # -----------------------------
        # Agent 2
        # -----------------------------

        agent_placeholder.markdown(
            render_agents(
                active_index=1,
                completed_index=0,
            ),
            unsafe_allow_html=True,
        )

        status_box.info(
            "🔎 Web Researcher is searching for evidence..."
        )

        progress.progress(25)

        # -----------------------------
        # Agent 3
        # -----------------------------

        agent_placeholder.markdown(
            render_agents(
                active_index=2,
                completed_index=1,
            ),
            unsafe_allow_html=True,
        )

        status_box.info(
            "📚 Academic Analyst is analyzing the research..."
        )

        progress.progress(45)

        # -----------------------------
        # Agent 4
        # -----------------------------

        agent_placeholder.markdown(
            render_agents(
                active_index=3,
                completed_index=2,
            ),
            unsafe_allow_html=True,
        )

        status_box.info(
            "🛡️ Citation Validator is checking research quality..."
        )

        progress.progress(70)

        # -----------------------------
        # Run Crew
        # -----------------------------

        try:
    result = crew.kickoff(
        inputs={
            "topic": topic,
            "research_type": research_type,
            "depth": depth,
        }
    )

    # Mark all agents as completed
    for agent_name in agent_names:
        agent_status[agent_name] = "completed"

    progress_bar.progress(100)

    st.success("Research completed successfully!")

    # ---------------------------------------------------------
    # FINAL REPORT
    # ---------------------------------------------------------

    st.markdown(
        """
        <div class="section-title">
            📄 Final Research Report
        </div>
        """,
        unsafe_allow_html=True,
    )

    final_output = result.raw if hasattr(result, "raw") else str(result)

    st.markdown(
        f"""
        <div class="report-container">
            {final_output}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.download_button(
        label="⬇️ Download Research Report",
        data=final_output,
        file_name="research_report.txt",
        mime="text/plain",
    )

except Exception as e:
    st.error("Something went wrong while running the research team.")

    with st.expander("🔧 Technical details"):
        st.code(str(e))

        # -----------------------------
        # Agent 5
        # -----------------------------

        agent_placeholder.markdown(
            render_agents(
                active_index=4,
                completed_index=3,
            ),
            unsafe_allow_html=True,
        )

        status_box.info(
            "✍️ Research Writer is preparing the final report..."
        )

        progress.progress(90)

        # -----------------------------
        # Complete
        # -----------------------------

        agent_placeholder.markdown(
            render_agents(
                active_index=-1,
                completed_index=4,
            ),
            unsafe_allow_html=True,
        )

        progress.progress(100)

        status_box.success(
            "Research completed successfully."
        )

        st.markdown("---")

        st.markdown(
            """
            <div class="result-header">
                <strong>📄 Final Research Report</strong><br>
                <span style="color:#94a3b8;">
                Generated by the ResearchAI multi-agent team
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(str(result))

        st.download_button(
            label="⬇️ Download Research Report",
            data=str(result),
            file_name="research_report.md",
            mime="text/markdown",
        )

   except Exception as e:
    st.error("Something went wrong while running the research team.")

    with st.expander("🔧 Technical details"):
        st.code(str(e))

        st.info(
            "Check your GROQ_API_KEY and SERPER_API_KEY in "
            "Streamlit Secrets, then redeploy."
        )
