from pathlib import Path

import pytest
from py_mmut_rdf import MMUT
from rdflib import URIRef, Graph, RDF, Literal, Namespace
from rdflib.namespace import RDFS


EX = Namespace("http://example.org#")
SHAPES_FILE = Path(__file__).resolve().parents[1] / "py_mmut_rdf" / "mmut-shapes.ttl"
FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"


def _build_valid_workflow_graph():
    g = Graph()
    g.bind("mmut", MMUT._NS)

    g.add((EX.model_in, RDF.type, MMUT.RDFMicroModel))
    g.add((EX.model_in, RDFS.label, Literal("Input Model")))

    g.add((EX.model_out, RDF.type, MMUT.RDFMicroModel))
    g.add((EX.model_out, RDFS.label, Literal("Output Model")))

    g.add((EX.transform, RDF.type, MMUT.PythonScriptTransformation))
    g.add((EX.transform, RDFS.label, Literal("Transform Step")))
    g.add((EX.model_in, MMUT.isInputModelOf, EX.transform))
    g.add((EX.transform, MMUT.hasOutputModel, EX.model_out))
    g.add((EX.transform, MMUT.hasTaskDefinition, EX.taskdef))

    g.add((EX.taskdef, RDF.type, MMUT.TaskDefinition))
    g.add((EX.taskdef, RDFS.label, Literal("Transform Task")))
    g.add((EX.taskdef, MMUT.hasContainerProperties, EX.container))

    g.add((EX.container, RDF.type, MMUT.ContainerProperties))
    g.add((EX.container, MMUT.image, Literal("python:3.11")))
    g.add((EX.container, MMUT.hasCommandSequence, Literal("python run.py")))

    return g


def test_namespace_exists():
    """Test that the MMUT namespace is properly defined."""
    assert MMUT._NS is not None
    assert str(MMUT._NS).startswith("http://")


def test_classes_exist():
    """Test that all expected classes are defined."""
    assert isinstance(MMUT.RDFMicroModel, URIRef)
    assert isinstance(MMUT.PythonScriptTransformation, URIRef)


def test_object_properties_exist():
    """Test that all expected object properties are defined."""
    assert isinstance(MMUT.isInputModelOf, URIRef)
    assert isinstance(MMUT.hasOutputModel, URIRef)


def test_workflow():
    g = Graph()
    g.bind("mmut", MMUT._NS)
    g.add((URIRef("http://example.org#model_x"), RDF.type, MMUT.RDFMicroModel))

    assert (URIRef("http://example.org#model_x"), RDF.type, MMUT.RDFMicroModel) in g


def test_shacl_validation_positive():
    pyshacl = pytest.importorskip("pyshacl")

    g = _build_valid_workflow_graph()
    conforms, _, report_text = pyshacl.validate(
        data_graph=g,
        shacl_graph=str(SHAPES_FILE),
    )

    assert conforms is True
    assert "Conforms: True" in report_text


def test_shacl_validation_negative_loop():
    pyshacl = pytest.importorskip("pyshacl")

    g = _build_valid_workflow_graph()
    # Introduce an explicit loop: transform -> model_out -> transform
    g.add((EX.model_out, MMUT.isInputModelOf, EX.transform))

    conforms, _, report_text = pyshacl.validate(
        data_graph=g,
        shacl_graph=str(SHAPES_FILE),
    )

    assert conforms is False
    assert "Loop detected" in report_text


def test_shacl_validation_positive_from_ttl_fixture():
    pyshacl = pytest.importorskip("pyshacl")

    g = Graph()
    g.parse(FIXTURES_DIR / "workflow-valid.ttl", format="turtle")

    conforms, _, report_text = pyshacl.validate(
        data_graph=g,
        shacl_graph=str(SHAPES_FILE),
    )

    assert conforms is True
    assert "Conforms: True" in report_text


def test_shacl_validation_negative_from_ttl_fixture():
    pyshacl = pytest.importorskip("pyshacl")

    g = Graph()
    g.parse(FIXTURES_DIR / "workflow-loop.ttl", format="turtle")

    conforms, _, report_text = pyshacl.validate(
        data_graph=g,
        shacl_graph=str(SHAPES_FILE),
    )

    assert conforms is False
    assert "Loop detected" in report_text
