import rdflib
from litellm import completion
import re
import tqdm

graph = rdflib.Graph().parse("/home/nicolas/projects/musicbo-knowledge-graph/data/knowledge_graphs_releases/projected_only_wikidata.nt")

MBO = rdflib.Namespace("https://w3id.org/polifonia/ontology/musicbo/")

properties = list(graph.triples((None, rdflib.RDFS.subPropertyOf, MBO["frameBinaryProjection"])))
for prop, _, _ in tqdm.tqdm(properties):
  prop_str = str(prop).split("/")[-1]

  response = completion(
      model="ollama/mistral", 
      api_base="http://localhost:11434",
      max_tokens=5,
      messages=[
        { "content": 
            f"""Write only one natural language label for the frame "{prop_str}" in maximum 5 words that describes the relationship between the two entities.
            Examples:
            takes_sharer_role_in_frame_share_1_with_other_role_shared_with -> shared with
            takes_visitor_role_in_frame_visit_1_with_other_role_visited -> visited
            takes_source_or_from_where_role_in_frame_trip_1_with_other_role_destination -> trip source of
            takes_source_or_from_where_role_in_frame_trip_1_with_other_role_destination -> trip source of
            takes_name_itself_role_in_frame_call_1_with_other_role_item_being_labelled -> is named
            takes_office_holder_role_in_frame_have-org-role_2_with_other_role_title_of_office_held -> helds office
            Do not add anything else besides the label. Only write one label without any additional note or clarification or text.""",
          "role": "user"}], 
  )

  response = response.choices[0]["message"]["content"]
  label = re.search('(.*)[.\n]?', response).group(0).strip().lower().replace(".", "")

  graph.add((prop, rdflib.RDFS.label, rdflib.Literal(label)))

graph.serialize("data/knowledge_graphs_releases/projected_only_wikidata_described.nt")
