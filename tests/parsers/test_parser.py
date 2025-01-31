import logging

from nomad.datamodel import EntryArchive

from nomad_sxdm_parser.parsers.myparser import MyParser


def test_parse_file():
    parser = MyParser()
    archive = EntryArchive()
    parser.parse('tests/data/SXDM_test_output_NX.h5', archive, logging.getLogger())

    assert archive.data.definition == 'NXsxdm'
