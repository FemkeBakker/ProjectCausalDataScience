import pandas as pd
import networkx as nx

def load_graph():
    df = pd.read_stata("data/close_college.dta")
    variables = df.columns.values
    
    G = nx.DiGraph()

    for variable in variables:
        G.add_node(variable)

    G.add_edge('black', 'married')
    G.add_edge('black', 'educ')
    G.add_edge('black', 'lwage')
    G.add_edge('south', 'black')
    G.add_edge('smsa', 'south')
    G.add_edge('smsa', 'black')
    G.add_edge('smsa', 'lwage')
    G.add_edge('smsa', 'nearc4')
    G.add_edge('nearc4', 'educ')
    G.add_edge('educ', 'smsa')
    G.add_edge('educ', 'exper')
    G.add_edge('educ', 'lwage')
    G.add_edge('exper', 'lwage')
    return G