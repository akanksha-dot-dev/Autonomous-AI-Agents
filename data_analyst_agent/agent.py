from google.adk.agents import Agent
from google.adk.tools import google_search, AgentTool
from .tools import analyze_csv, calculate_metrics

# Sub-agent for web research
search_agent = Agent(
    name="search_agent",
    model="gemini-2.5-flash",
    instruction="Search the web for data and trends. Cite sources.",
    tools=[google_search],
)

# Root agent — the data analyst
root_agent = Agent(
    model="gemini-2.5-flash",
    name="data_analyst_agent",
    instruction=(
        "You are an expert data analyst. Use search "
        "for market trends. Use analyze_csv for local "
        "data files. Always cite your sources."
    ),
    tools=[
        AgentTool(search_agent),
        analyze_csv,
        calculate_metrics,
    ],
)