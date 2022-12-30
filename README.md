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

MusicBO Knowledge Graph is automatically extracted from natural language texts by applying a custom text-to-Knowledge Graph (text2KG) process to the MusicBO corpus documents. The MusicBO corpus is part of the **[Polifonia Corpus](https://github.com/polifonia-project/Polifonia-Corpus)**. The text2KG process leverages two modules: the **[Polifonia Knowledge Extractor](https://github.com/polifonia-project/Polifonia-Knowledge-Extractor)** pipeline and the **[AMR2Fred](https://github.com/infovillasimius/amr2Fred)** tool. The two modules are orchestrated by the **[Machine Reading](https://github.com/anuzzolese/machine-reading)** suite, which queries both modules and generates RDF named graphs from natural language text.
