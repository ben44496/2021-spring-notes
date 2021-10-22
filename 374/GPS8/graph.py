import networkx as nx

class DiGraphWithEdgeChecker(nx.DiGraph):
    """
    In NetworkX's implementation of add_edge, the nodes u and v will be
    automatically added if they are not already in the graph.

    This subclass will fail-fast if you try to do that, which may help you catch mistakes more easily.
    We also want you to practice defining your vertex set explicitly instead of implicitly creating vertices
    when you add edges.
    """
    def add_edge(self, u_of_edge, v_of_edge, **attr):
        if not (u_of_edge in self.nodes and v_of_edge in self.nodes):
            raise Exception("Endpoints of edge are not in the graph's vertex set")
        super().add_edge(u_of_edge, v_of_edge, **attr)

def reach(G, s):
    return {n for n in nx.dfs_postorder_nodes(G,source=s)}