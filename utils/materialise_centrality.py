import rdflib
from rdflib.extras.external_graph_libs import rdflib_to_networkx_graph
import networkx as nx
import tqdm

graph = rdflib.Graph().parse("data/knowledge_graphs_releases/projected_only_wikidata_described.ttl")

MBO = rdflib.Namespace("https://w3id.org/polifonia/ontology/musicbo/")

nx_graph = rdflib_to_networkx_graph(graph, calc_weights=False)

c = nx.communicability_exp(nx_graph)

for node, others in tqdm.tqdm(c.items()):
  if "wikidata" in str(node):
    for other, weight in others.items():
      if "wikidata" in str(other) and weight > 0:
        communicates_bnode = rdflib.BNode()
        graph.add((communicates_bnode, rdflib.RDF.type, MBO["LinkStrength"]))
        graph.add((communicates_bnode, MBO["hasSource"], node))
        graph.add((communicates_bnode, MBO["hasTarget"], other))
        graph.add((communicates_bnode, MBO["hasStrength"], rdflib.Literal(weight)))


graph.serialize("data/knowledge_graphs_releases/projected_only_wikidata_described_strength.ttl")