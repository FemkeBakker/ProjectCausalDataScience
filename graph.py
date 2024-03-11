import pandas as pd
import networkx as nx
import os

"""
Version of the graph corresponds to the version on draw.io.
"""
def load_graph(version):


    df = pd.read_stata("data/close_college.dta")
    variables = df.columns.values
    G = nx.DiGraph()

    for variable in variables:
        G.add_node(variable)

    # version 0
    if version==0:
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

    
        nx.write_gml(G, f"graph_files/graph_version{version}.gml")

        return G
    
    # version 1
    elif version==1:
        G.add_edge('black', 'married')
        G.add_edge('black', 'educ')
        G.add_edge('black', 'lwage')
        G.add_edge('south', 'black')
        G.add_edge('smsa', 'south')
        G.add_edge('smsa', 'black')
        G.add_edge('smsa', 'lwage')
        G.add_edge('smsa', 'nearc4')
        G.add_edge('nearc4', 'educ')

        #remove
        # G.add_edge('educ', 'smsa')
        G.add_edge('educ', 'exper')
        G.add_edge('educ', 'lwage')
        G.add_edge('exper', 'lwage')

        nx.write_gml(G, f"graph_files/graph_version{version}.gml")
        return G
    
    # version 2
    elif version==2:
        G.add_edge('black', 'married')
        G.add_edge('black', 'educ')
        G.add_edge('black', 'lwage')
        G.add_edge('south', 'black')
        # G.add_edge('smsa', 'south')
        G.add_edge('smsa', 'black')
        G.add_edge('smsa', 'lwage')
        G.add_edge('smsa', 'nearc4')
        G.add_edge('nearc4', 'educ')

        #remove
        G.add_edge('smsa', 'educ')
        G.add_edge('educ', 'exper')
        G.add_edge('educ', 'lwage')
        G.add_edge('exper', 'lwage')

        nx.write_gml(G, f"graph_files/graph_version{version}.gml")
        return G
