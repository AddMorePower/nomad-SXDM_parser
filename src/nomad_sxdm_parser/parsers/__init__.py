from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field


class MyParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_sxdm_parser.parsers.myparser import MyParser

        return MyParser(**self.dict())


myparser = MyParserEntryPoint(
    name='SXDM parser',
    description='Parser for experimental data files coming from SXDM at ESRF.',
    mainfile_name_re='.*SXDM.*\.h5',
)
