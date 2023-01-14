---
component-id: musicbo-knowledge-graph
name: MusicBO Knowledge Graph
description: The Knowledge Graph about the role of Bologna in the European musical landscape.
type: Repository
release-date: 30/12/2022
release-number: v0.1
work-package: 
- WP4
licence: CC BY
links:
- https://github.com/polifonia-project/musicbo-knowledge-graph
credits:
- https://github.com/valecarriero
- https://github.com/FiorelaCiroku
- https://github.com/roccotrip
- https://github.com/arianna-graciotti
- https://github.com/EleonoraMarzi
---

# musicbo-knowledge-graph
MusicBO Knowledge Graph stores information about the role of music in the city of Bologna from a historical and social perspective. It aims to satisfy the requirements of MusicBO pilot use case, namely conveying knowledge about music performances in Bologna and encounters between musicians, composers, critics and historians who passed through Bologna.

MusicBO Knowledge Graph is available via the **[MusicBO SPARQL endpoint](https://polifonia.disi.unibo.it/musicbo/sparql)**.

MusicBO Knowledge Graph is automatically extracted from natural language texts by applying a custom text-to-Knowledge Graph (text2KG) process to the MusicBO corpus documents. The MusicBO corpus is part of the **[Polifonia Corpus](https://github.com/polifonia-project/Polifonia-Corpus)**. 

The process leverages two modules: the **[Polifonia Knowledge Extractor](https://github.com/polifonia-project/Polifonia-Knowledge-Extractor)** pipeline and the **[AMR2Fred](https://github.com/infovillasimius/amr2Fred)** tool. The first one uses **[AMR](https://github.com/amrisi/amr-guidelines/blob/master/amr.md)** (Abstract Meaning Representation) to parse sentences into semantic graphs. The second one transforms AMR graphs into RDF/OWL KGs based on **[FRED](http://wit.istc.cnr.it/stlab-tools/fred/demo/)** logic form by exploiting the similarities between AMR graphs and FRED's output representation, such as being both graph-based and event-centric. The Polifonia Knowledge Extractor pipeline provides input to the **[AMR2Fred](https://github.com/infovillasimius/amr2Fred)** tool. The two modules are orchestrated by the **[Machine Reading suite](https://github.com/anuzzolese/machine-reading)**, which queries both components through the **[Text-to-AMR-to-FRED API](http://framester.istc.cnr.it/txt-amr-fred/api/docs)** and generates RDF named graphs from natural language text.

The Text2KG process for the automatic creation of the MusicBO KG can be broken down into its main steps as follows:

1. **[Input.]** For the scope of this Deliverable, we applied our text2KG process to the English and Italian language documents of MusicBO corpus. We took as input 47 documents in English and 51 documents in Italian from the MusicBO corpus.
2. **[Pre-processing.]** The MusicBO corpus documents that we chose as input were originally in .PDF, image or .docx formats. Therefore, we needed to extrapolate the plain text from them, leveraging ad hoc Optical Character Recognition (OCR) technologies from **[textual-corpus-population](https://github.com/polifonia-project/textual-corpus-population)** when necessary. We then performed co-reference resolution: for English language documents, we implemented a co-reference resolution pipeline based on Spacy's **[neuralcoref](https://spacy.io/universe/project/neuralcoref)**. We have not yet implemented any co-reference resolution procedure for the Italian language documents, as we are still evaluating the performances of state-of-the-art Italian language co-reference resolution tools. We also performed rule-based minimal post-OCR corrections and sentence splitting on the extrapolated plain texts. 
3. **[Text2AMR Parsing.]** The sentences resulting from the pre-processing steps described at point 2 above are submitted to state-of-the-art neural text-to-AMR parsers. MR has gained significant attention in recent years as a meaning representation formalism, given its ability to abstract away from syntactic variability and its potential to act as an interlingua in scenarios that encompass multilingual textual sources. For sentences in English we used **[SPRING](http://nlp.uniroma1.it/spring/)**. For sentences in Italian, we used **[USeA](https://github.com/SapienzaNLP/usea)**.
4. **[Filtering.]** This step is a preliminary tentative to tackle AMR graphs evaluation. Given that we are concentrating on non-standard texts (historical documents), the results of the state-of-the-art AMR parsers may be inaccurate. Human validation is time-consuming, and there are no standard benchmarks for the semantic parsing of historic and OCRed text. For this reason, we decided to use a back-translation approach that converts the generated AMR graphs back to sentences (AMR2text) to compute similarity scores between the original sentence and the generated one. For English, we used **[SPRING](http://nlp.uniroma1.it/spring/)** for AMR2Text generation and computed **[BLEURT](https://github.com/google-research/bleurt)** as a similarity score. For Italian, we used **[m-AMR2Text](https://github.com/UKPLab/m-AMR2Text)** for AMR2Text generation. Then, we computed the cosine similarity between the embedding of the original and the generated sentences. We generated the embeddings by leveraging **[LASER embeddings](https://github.com/yannvgn/laserembeddings)**, an off-the-shelf multilingual sentence embedding toolkit. We hypothesise that generated sentences with high BLEURT or cosine similarity scores correspond to high-quality graphs. We decided to discard all the graphs in our English AMR graphs bank corresponding to AMR2Text-generated sentences with a negative BLEURT score. With regard to our Italian AMR graphs bank, we decided to discard the graphs associated with AMR2Text-generated sentences having a cosine similarity <0,90. In fact, according to our sample-based qualitative error analysis, negative BLEURT scores and cosine similarity <0,90 corresponded to low-quality generated sentences and, consequentially, to low-quality AMR graphs. The quality issues observed in the AMR graphs correlated with input sentences affected, for example, by severe OCR errors.
5. **[AMR2Fred translation.]** Finally, we transformed the graphs filtered at step above into OWL/RDF Knowledge Graphs that follow **[FRED](http://wit.istc.cnr.it/stlab-tools/fred/demo/)** knowledge representation patterns. This transformation is done by querying the AMR2Fred tool via the **[Machine Reading](https://github.com/anuzzolese/machine-reading)** suite. The output is named graphs produced by using the **[N-Quad](https://www.w3.org/TR/n-quads/)** syntax. Named graphs allow for extending the standard RDF triple model with a "context" element which, among the other features, allows the association of each triple with information about their provenance. In our case, the context element of MusicBO Knowledge Graph triples indicates which sentence's graph the triple is part of. At this step, we enrich the resulting FRED-like RDF/OWL KGs using **[Framester](http://etna.istc.cnr.it/framester_web/)** semantic hub. In fact, thanks to Framester, the information implicitly enclosed in the text could be unveiled by integrating knowledge from different knowledge bases such as [FrameNet](https://framenet.icsi.berkeley.edu/fndrupal/), [WordNet](https://wordnet.princeton.edu/), [VerbNet](https://verbs.colorado.edu/verbnet/), [BabelNet](https://babelnet.org/), [DBPedia](https://www.dbpedia.org/), [Yago](https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/yago-naga/yago/), [DOLCE-Zero](http://www.ontologydesignpatterns.org/ont/d0.owl) and other resources. In particular, we enrich the FRED-like RDF/OWL KGs with Word Sense Disambiguation (WSD) information. The WSD process currently implemented applies to those elements of the FRED-like RDF/OWL KGs which correspond to nodes of the AMR graphs that are not linked to any lexical resources or knowledge bases, namely all the AMR graphs nodes that are not treated as **[PropBank](http://propbank.github.io/)** predicates or named entities. The implemented WSD process consists of submitting the sentence associated with the FRED-like RDF/OWL KG to **[EWISER](https://github.com/SapienzaNLP/ewiser)**, a WSD system, and of associating the resulting WSD information with the AMR2Fred nodes whose corresponding labels in the AMR graph matches the lemmas of the processed sentence (if the  graph's node is among those that need to be enriched with WSD information). We leverage [WordNet](https://wordnet.princeton.edu/) as the lexical resource from which we take the word senses information.

 We provide in folder input_csv\ of this repository the input CSV that contains the pre-processed and filtered EN sentences of the MusicBO corpus (steps 1-4 of the process described above). The CSV is ready to be sent as input to the **[Machine Reading](https://github.com/anuzzolese/machine-reading)** suite, to enable the creation of named graphs as per step 5 of the Text2KG process.

MusicBO Knowledge Graph is described in a dedicated **[MELODY data story](https://projects.dharc.unibo.it/melody/musicbo/music_in_bologna_textual_corpus_overview)**.
