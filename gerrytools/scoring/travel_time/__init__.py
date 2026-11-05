"""District travel-time scores from a precomputed statewide table.

``pairwise_travel_time`` averages travel time across unordered pairs of units in each district.
``centroid_travel_time`` selects the district unit minimizing travel time to all district units,
then averages trips from that unit. Population-weighted modes retain their weights in the score's
units and divide by the number of trips.
"""

from .api import centroid_travel_time, pairwise_travel_time, travel_time_scores
from .builder import (
    DEFAULT_FALLBACK_SPEED_KPH,
    DEFAULT_FERRY_SPEED_KPH,
    FerryBuildSummary,
    SpeedRepairSummary,
    TravelTimeBuildReport,
    TravelTimeBuildResult,
    build_osm_drive_graph,
    build_travel_time_table,
    build_travel_time_table_from_pbf,
    census_representative_points,
    repair_nonpositive_edge_speeds,
    snap_units_to_graph,
)
from .od_table import TravelTimeTable
from .provenance import (
    SnappingArtifact,
    UnitSnap,
    default_snapping_path,
    load_snapping_artifact,
    save_snapping_artifact,
)
from .table_io import (
    TimeUnit,
    TravelTimeArtifact,
    load_travel_time_table,
    save_travel_time_table,
)
from .weights import CentroidWeightMode, PairwiseWeightMode

__all__ = [
    "DEFAULT_FALLBACK_SPEED_KPH",
    "DEFAULT_FERRY_SPEED_KPH",
    "CentroidWeightMode",
    "FerryBuildSummary",
    "PairwiseWeightMode",
    "SnappingArtifact",
    "TimeUnit",
    "TravelTimeArtifact",
    "TravelTimeBuildReport",
    "TravelTimeBuildResult",
    "TravelTimeTable",
    "UnitSnap",
    "SpeedRepairSummary",
    "build_osm_drive_graph",
    "build_travel_time_table",
    "build_travel_time_table_from_pbf",
    "census_representative_points",
    "centroid_travel_time",
    "default_snapping_path",
    "load_snapping_artifact",
    "load_travel_time_table",
    "pairwise_travel_time",
    "repair_nonpositive_edge_speeds",
    "save_snapping_artifact",
    "save_travel_time_table",
    "snap_units_to_graph",
    "travel_time_scores",
]
