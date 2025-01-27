from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

from numpy import float64

from nomad.config import config
from nomad.datamodel.data import Schema
from nomad.metainfo import Quantity, SchemaPackage, MSection, SubSection

configuration = config.get_plugin_entry_point(
    'nomad_sxdm_parser.schema_packages:mypackage'
)

m_package = SchemaPackage()

class Data(MSection):
    energy = Quantity(type=str)
    sxdm_scan_type = Quantity(type=str)
    dim_x = Quantity(type=int)
    dim_y = Quantity(type=int)
    sample_x = Quantity(type=float64, shape=['dim_x'])
    sample_y = Quantity(type=float64, shape=['dim_y'])
    dataset = Quantity(type=float64, shape=[9, 'dim_x', 'dim_y'])


###############################################################################
class Monochromator(MSection):
    energy = Quantity(
        type=str
    )

class Source(MSection):
    type = Quantity(type=str)
    probe = Quantity(type=str)
    name = Quantity(type=str)

class Instrument(MSection):
    monochromator = SubSection(sub_section=Monochromator.m_def, repeats=False)
    source = SubSection(sub_section=Source.m_def, repeats=False)


###############################################################################
class Sample(MSection):
    rotation_angle = Quantity(
        type=float64,
        description="The rotation angle used during the acquisition."
    )


###############################################################################
###############################################################################
class SXDMData(Schema):
    definition = Quantity(
        type=str,
        description="Name of the potential NeXus application definition."
    )
    start_time = Quantity(
        type=str,
        description="Date at the start of the acquisition."
    )
    end_time = Quantity(
        type=str,
        description="Date at the end of the acquisition."
    )
    title = Quantity(
        type=str,
        description="Name of the file."
    )
    data = SubSection(sub_section=Data.m_def, repeats=False)
    instrument = SubSection(sub_section=Instrument.m_def, repeats=False)
    sample = SubSection(sub_section=Sample.m_def, repeats=False)

m_package.__init_metainfo__()
