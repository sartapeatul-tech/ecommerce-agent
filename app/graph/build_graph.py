from langgraph.graph import StateGraph, END
from app.graph.state import AgentState

from app.agents.search_agent import search_agent
from app.agents.filter_agent import filter_agent
from app.agents.review_agent import review_agent
from app.agents.ranking_agent import ranking_agent
from app.agents.aggregator_agent import aggregator_agent

from langsmith import traceable

@traceable(name="search_node")
def search_node(state):
    products, constraints = search_agent(state["query"])
    state["products"] = products
    state["constraints"] = constraints
    return state

@traceable(name="filter_node")
def filter_node(state):
    state["filtered_products"] = filter_agent(
        state["products"], state["query"]
    )
    return state

@traceable(name="review_node")
def review_node(state):
    state["review_analysis"] = review_agent(
        state["filtered_products"], state["query"]
    )
    return state

@traceable(name="ranking_node")
def ranking_node(state):
    state["ranked_products"] = ranking_agent(
        state["filtered_products"],
        state["review_analysis"],
        state["constraints"]
    )
    return state

@traceable(name="aggregator_node")
def aggregator_node(state):
    state["final_output"] = aggregator_agent(
        state["ranked_products"], state["query"]
    )
    return state


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("search", search_node)
    graph.add_node("filter", filter_node)
    graph.add_node("review", review_node)
    graph.add_node("ranking", ranking_node)
    graph.add_node("aggregator", aggregator_node)

    graph.set_entry_point("search")
    graph.add_edge("search", "filter")
    graph.add_edge("filter", "review")
    graph.add_edge("review", "ranking")
    graph.add_edge("ranking", "aggregator")
    graph.add_edge("aggregator", END)

    return graph.compile()

    graph.add_node("search", search_node)
    graph.add_node("filter", filter_node)
    graph.add_node("review", review_node)
    graph.add_node("ranking", ranking_node)
    graph.add_node("aggregator", aggregator_node)

    graph.set_entry_point("search")

    graph.add_edge("search", "filter")
    graph.add_edge("filter", "review")
    graph.add_edge("review", "ranking")
    graph.add_edge("ranking", "aggregator")
    graph.add_edge("aggregator", END)

    return graph.compile()