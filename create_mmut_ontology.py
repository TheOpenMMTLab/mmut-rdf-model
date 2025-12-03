from rdflib import Graph, Namespace, RDF, RDFS, OWL, URIRef, DCTERMS, Literal, XSD


VERSION = "0.0.2"
KEY = "mmut"

# Definition des NameNSraums
NS = Namespace(f"http://frittenburger.de/ontology/{KEY}#")

# Erstellung des Graphen
g = Graph()
g.namespace_manager.bind(KEY, NS)

# Ontology
ontology = URIRef(f"https://gitlab.hpi.de/dfriedenberger/{KEY}")
g.add((ontology, RDF.type, OWL.Ontology))
g.add((ontology, DCTERMS.title, Literal("Micro Model and Transformation Ontology")))
g.add((ontology, DCTERMS.description, Literal("A rdf Ontology for model Micro Models and Transformation.", lang='en')))

g.add((ontology, OWL.versionInfo, Literal(VERSION)))
g.add((ontology, DCTERMS.creator, Literal("Dirk Friedenberger")))
g.add((ontology, DCTERMS.creator, URIRef("https://www.researchgate.net/profile/Dirk_Friedenberger")))
g.add((ontology, DCTERMS.identifier, Literal(NS)))

# concepts

# Model Taxonomy
g.add((NS.MicroModel, RDF.type, OWL.Class))
g.add((NS.MicroModel, RDFS.label, Literal("An abstract micro model.", lang='en')))

g.add((NS.RDFMicroModel, RDF.type, OWL.Class))
g.add((NS.RDFMicroModel, RDFS.label, Literal("An RDF micro model.", lang='en')))
g.add((NS.RDFMicroModel, RDFS.subClassOf, NS.MicroModel))

g.add((NS.BinaryMicroModel, RDF.type, OWL.Class))
g.add((NS.BinaryMicroModel, RDFS.label, Literal("A Binary micro model.", lang='en')))
g.add((NS.BinaryMicroModel, RDFS.subClassOf, NS.MicroModel))

g.add((NS.SysMLMicroModel, RDF.type, OWL.Class))
g.add((NS.SysMLMicroModel, RDFS.label, Literal("A SysML micro model.", lang='en')))
g.add((NS.SysMLMicroModel, RDFS.subClassOf, NS.MicroModel))

g.add((NS.EcoreMicroModel, RDF.type, OWL.Class))
g.add((NS.EcoreMicroModel, RDFS.label, Literal("An Ecore micro model.", lang='en')))
g.add((NS.EcoreMicroModel, RDFS.subClassOf, NS.MicroModel))

# Transformation Taxonomy
g.add((NS.Transformation, RDF.type, OWL.Class))
g.add((NS.Transformation, RDFS.label, Literal("An abstract transformation.", lang='en')))

g.add((NS.PythonScriptTransformation, RDF.type, OWL.Class))
g.add((NS.PythonScriptTransformation, RDFS.subClassOf, NS.Transformation))
g.add((NS.PythonScriptTransformation, RDFS.label, Literal("A Python-based transformation.", lang='en')))

# Extension: TaskDefinition
g.add((NS.TaskDefinition, RDF.type, OWL.Class))
g.add((NS.TaskDefinition, RDFS.label, Literal("A task definition for implementing processes.", lang='en')))


g.add((NS.ContainerProperties, RDF.type, OWL.Class))
g.add((NS.ContainerProperties, RDFS.label, Literal("Properties of a container.", lang='en')))

g.add((NS.Environment, RDF.type, OWL.Class))
g.add((NS.Environment, RDFS.label, Literal("An environment for executing containers.", lang='en')))

g.add((NS.KeyValuePair, RDF.type, OWL.Class))
g.add((NS.KeyValuePair, RDFS.label, Literal("A key-value pair.", lang='en')))

# properties
g.add((NS.key, RDF.type, OWL.DatatypeProperty))
g.add((NS.key, RDFS.domain, NS.KeyValuePair))
g.add((NS.key, RDFS.range, XSD.string))
g.add((NS.key, RDFS.label, Literal("key of the key-value pair", lang='en')))

g.add((NS.value, RDF.type, OWL.DatatypeProperty))
g.add((NS.value, RDFS.domain, NS.KeyValuePair))
g.add((NS.value, RDFS.range, XSD.string))
g.add((NS.value, RDFS.label, Literal("value of the key-value pair", lang='en')))

g.add((NS.image, RDF.type, OWL.DatatypeProperty))
g.add((NS.image, RDFS.domain, NS.ContainerProperties))
g.add((NS.image, RDFS.range, XSD.string))
g.add((NS.image, RDFS.label, Literal("image of the container", lang='en')))


# relations
g.add((NS.isInputModelOf, RDF.type, OWL.ObjectProperty))
g.add((NS.isInputModelOf, RDFS.domain, NS.MicroModel))
g.add((NS.isInputModelOf, RDFS.range, NS.Transformation))
g.add((NS.isInputModelOf, RDFS.label, Literal("model used for transformation", lang='en')))

g.add((NS.hasOutputModel, RDF.type, OWL.ObjectProperty))
g.add((NS.hasOutputModel, RDFS.domain, NS.Transformation))
g.add((NS.hasOutputModel, RDFS.range, NS.MicroModel))
g.add((NS.hasOutputModel, RDFS.label, Literal("transforms to model", lang='en')))

g.add((NS.hasLooseCoupling, RDF.type, OWL.ObjectProperty))
g.add((NS.hasLooseCoupling, RDFS.domain, NS.MicroModel))
g.add((NS.hasLooseCoupling, RDFS.range, NS.MicroModel))
g.add((NS.hasLooseCoupling, RDFS.label, Literal("couples loose to", lang='en')))

g.add((NS.extendsModel, RDF.type, OWL.ObjectProperty))
g.add((NS.extendsModel, RDFS.domain, NS.MicroModel))
g.add((NS.extendsModel, RDFS.range, NS.MicroModel))
g.add((NS.extendsModel, RDFS.label, Literal("extends model", lang='en')))


g.add((NS.hasTaskDefinition, RDF.type, OWL.ObjectProperty))
g.add((NS.hasTaskDefinition, RDFS.domain, OWL.Thing))
g.add((NS.hasTaskDefinition, RDFS.range, NS.TaskDefinition))
g.add((NS.hasTaskDefinition, RDFS.label, Literal("task definition for processing", lang='en')))

g.add((NS.hasContainerProperties, RDF.type, OWL.ObjectProperty))
g.add((NS.hasContainerProperties, RDFS.domain, NS.TaskDefinition))
g.add((NS.hasContainerProperties, RDFS.range, NS.ContainerProperties))
g.add((NS.hasContainerProperties, RDFS.label, Literal("container properties for processing", lang='en')))

g.add((NS.hasCommandSequence, RDF.type, OWL.ObjectProperty))
g.add((NS.hasCommandSequence, RDFS.domain, NS.ContainerProperties))
g.add((NS.hasCommandSequence, RDFS.range, RDF.Seq))
g.add((NS.hasCommandSequence, RDFS.label, Literal("command to run the container", lang='en')))

g.add((NS.hasEnvironment, RDF.type, OWL.ObjectProperty))
g.add((NS.hasEnvironment, RDFS.domain, NS.ContainerProperties))
g.add((NS.hasEnvironment, RDFS.range, NS.Environment))
g.add((NS.hasEnvironment, RDFS.label, Literal("environment for processing", lang='en')))

g.add((NS.hasKeyValuePair, RDF.type, OWL.ObjectProperty))
g.add((NS.hasKeyValuePair, RDFS.domain, NS.Environment))
g.add((NS.hasKeyValuePair, RDFS.range, NS.KeyValuePair))
g.add((NS.hasKeyValuePair, RDFS.label, Literal("key-value pairs for container properties", lang='en')))


# Serialisierung der Ontologie in RDF/XML-Syntax
g.serialize(destination=f"py_mmut_rdf/{KEY}.ttl", format='turtle')
