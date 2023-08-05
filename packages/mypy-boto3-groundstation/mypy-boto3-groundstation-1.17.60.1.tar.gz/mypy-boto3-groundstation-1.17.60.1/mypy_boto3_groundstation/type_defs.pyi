"""
Main interface for groundstation service type definitions.

Usage::

    ```python
    from mypy_boto3_groundstation.type_defs import AntennaDemodDecodeDetailsTypeDef

    data: AntennaDemodDecodeDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_groundstation.literals import (
    AngleUnits,
    BandwidthUnits,
    ConfigCapabilityType,
    ContactStatus,
    Criticality,
    EirpUnits,
    EndpointStatus,
    FrequencyUnits,
    Polarization,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AntennaDemodDecodeDetailsTypeDef",
    "AntennaDownlinkConfigTypeDef",
    "AntennaDownlinkDemodDecodeConfigTypeDef",
    "AntennaUplinkConfigTypeDef",
    "ConfigDetailsTypeDef",
    "ConfigListItemTypeDef",
    "ConfigTypeDataTypeDef",
    "ContactDataTypeDef",
    "DataflowDetailTypeDef",
    "DataflowEndpointConfigTypeDef",
    "DataflowEndpointListItemTypeDef",
    "DataflowEndpointTypeDef",
    "DecodeConfigTypeDef",
    "DemodulationConfigTypeDef",
    "DestinationTypeDef",
    "EirpTypeDef",
    "ElevationTypeDef",
    "EndpointDetailsTypeDef",
    "FrequencyBandwidthTypeDef",
    "FrequencyTypeDef",
    "GroundStationDataTypeDef",
    "MissionProfileListItemTypeDef",
    "S3RecordingConfigTypeDef",
    "S3RecordingDetailsTypeDef",
    "SatelliteListItemTypeDef",
    "SecurityDetailsTypeDef",
    "SocketAddressTypeDef",
    "SourceTypeDef",
    "SpectrumConfigTypeDef",
    "TrackingConfigTypeDef",
    "UplinkEchoConfigTypeDef",
    "UplinkSpectrumConfigTypeDef",
    "ConfigIdResponseTypeDef",
    "ContactIdResponseTypeDef",
    "DataflowEndpointGroupIdResponseTypeDef",
    "DescribeContactResponseTypeDef",
    "GetConfigResponseTypeDef",
    "GetDataflowEndpointGroupResponseTypeDef",
    "GetMinuteUsageResponseTypeDef",
    "GetMissionProfileResponseTypeDef",
    "GetSatelliteResponseTypeDef",
    "ListConfigsResponseTypeDef",
    "ListContactsResponseTypeDef",
    "ListDataflowEndpointGroupsResponseTypeDef",
    "ListGroundStationsResponseTypeDef",
    "ListMissionProfilesResponseTypeDef",
    "ListSatellitesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MissionProfileIdResponseTypeDef",
    "PaginatorConfigTypeDef",
)

AntennaDemodDecodeDetailsTypeDef = TypedDict(
    "AntennaDemodDecodeDetailsTypeDef", {"outputNode": str}, total=False
)

AntennaDownlinkConfigTypeDef = TypedDict(
    "AntennaDownlinkConfigTypeDef", {"spectrumConfig": "SpectrumConfigTypeDef"}
)

AntennaDownlinkDemodDecodeConfigTypeDef = TypedDict(
    "AntennaDownlinkDemodDecodeConfigTypeDef",
    {
        "decodeConfig": "DecodeConfigTypeDef",
        "demodulationConfig": "DemodulationConfigTypeDef",
        "spectrumConfig": "SpectrumConfigTypeDef",
    },
)

_RequiredAntennaUplinkConfigTypeDef = TypedDict(
    "_RequiredAntennaUplinkConfigTypeDef",
    {"spectrumConfig": "UplinkSpectrumConfigTypeDef", "targetEirp": "EirpTypeDef"},
)
_OptionalAntennaUplinkConfigTypeDef = TypedDict(
    "_OptionalAntennaUplinkConfigTypeDef", {"transmitDisabled": bool}, total=False
)

class AntennaUplinkConfigTypeDef(
    _RequiredAntennaUplinkConfigTypeDef, _OptionalAntennaUplinkConfigTypeDef
):
    pass

ConfigDetailsTypeDef = TypedDict(
    "ConfigDetailsTypeDef",
    {
        "antennaDemodDecodeDetails": "AntennaDemodDecodeDetailsTypeDef",
        "endpointDetails": "EndpointDetailsTypeDef",
        "s3RecordingDetails": "S3RecordingDetailsTypeDef",
    },
    total=False,
)

ConfigListItemTypeDef = TypedDict(
    "ConfigListItemTypeDef",
    {"configArn": str, "configId": str, "configType": ConfigCapabilityType, "name": str},
    total=False,
)

ConfigTypeDataTypeDef = TypedDict(
    "ConfigTypeDataTypeDef",
    {
        "antennaDownlinkConfig": "AntennaDownlinkConfigTypeDef",
        "antennaDownlinkDemodDecodeConfig": "AntennaDownlinkDemodDecodeConfigTypeDef",
        "antennaUplinkConfig": "AntennaUplinkConfigTypeDef",
        "dataflowEndpointConfig": "DataflowEndpointConfigTypeDef",
        "s3RecordingConfig": "S3RecordingConfigTypeDef",
        "trackingConfig": "TrackingConfigTypeDef",
        "uplinkEchoConfig": "UplinkEchoConfigTypeDef",
    },
    total=False,
)

ContactDataTypeDef = TypedDict(
    "ContactDataTypeDef",
    {
        "contactId": str,
        "contactStatus": ContactStatus,
        "endTime": datetime,
        "errorMessage": str,
        "groundStation": str,
        "maximumElevation": "ElevationTypeDef",
        "missionProfileArn": str,
        "postPassEndTime": datetime,
        "prePassStartTime": datetime,
        "region": str,
        "satelliteArn": str,
        "startTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

DataflowDetailTypeDef = TypedDict(
    "DataflowDetailTypeDef",
    {"destination": "DestinationTypeDef", "errorMessage": str, "source": "SourceTypeDef"},
    total=False,
)

_RequiredDataflowEndpointConfigTypeDef = TypedDict(
    "_RequiredDataflowEndpointConfigTypeDef", {"dataflowEndpointName": str}
)
_OptionalDataflowEndpointConfigTypeDef = TypedDict(
    "_OptionalDataflowEndpointConfigTypeDef", {"dataflowEndpointRegion": str}, total=False
)

class DataflowEndpointConfigTypeDef(
    _RequiredDataflowEndpointConfigTypeDef, _OptionalDataflowEndpointConfigTypeDef
):
    pass

DataflowEndpointListItemTypeDef = TypedDict(
    "DataflowEndpointListItemTypeDef",
    {"dataflowEndpointGroupArn": str, "dataflowEndpointGroupId": str},
    total=False,
)

DataflowEndpointTypeDef = TypedDict(
    "DataflowEndpointTypeDef",
    {"address": "SocketAddressTypeDef", "mtu": int, "name": str, "status": EndpointStatus},
    total=False,
)

DecodeConfigTypeDef = TypedDict("DecodeConfigTypeDef", {"unvalidatedJSON": str})

DemodulationConfigTypeDef = TypedDict("DemodulationConfigTypeDef", {"unvalidatedJSON": str})

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "configDetails": "ConfigDetailsTypeDef",
        "configId": str,
        "configType": ConfigCapabilityType,
        "dataflowDestinationRegion": str,
    },
    total=False,
)

EirpTypeDef = TypedDict("EirpTypeDef", {"units": EirpUnits, "value": float})

ElevationTypeDef = TypedDict("ElevationTypeDef", {"unit": AngleUnits, "value": float})

EndpointDetailsTypeDef = TypedDict(
    "EndpointDetailsTypeDef",
    {"endpoint": "DataflowEndpointTypeDef", "securityDetails": "SecurityDetailsTypeDef"},
    total=False,
)

FrequencyBandwidthTypeDef = TypedDict(
    "FrequencyBandwidthTypeDef", {"units": BandwidthUnits, "value": float}
)

FrequencyTypeDef = TypedDict("FrequencyTypeDef", {"units": FrequencyUnits, "value": float})

GroundStationDataTypeDef = TypedDict(
    "GroundStationDataTypeDef",
    {"groundStationId": str, "groundStationName": str, "region": str},
    total=False,
)

MissionProfileListItemTypeDef = TypedDict(
    "MissionProfileListItemTypeDef",
    {"missionProfileArn": str, "missionProfileId": str, "name": str, "region": str},
    total=False,
)

_RequiredS3RecordingConfigTypeDef = TypedDict(
    "_RequiredS3RecordingConfigTypeDef", {"bucketArn": str, "roleArn": str}
)
_OptionalS3RecordingConfigTypeDef = TypedDict(
    "_OptionalS3RecordingConfigTypeDef", {"prefix": str}, total=False
)

class S3RecordingConfigTypeDef(
    _RequiredS3RecordingConfigTypeDef, _OptionalS3RecordingConfigTypeDef
):
    pass

S3RecordingDetailsTypeDef = TypedDict(
    "S3RecordingDetailsTypeDef", {"bucketArn": str, "keyTemplate": str}, total=False
)

SatelliteListItemTypeDef = TypedDict(
    "SatelliteListItemTypeDef",
    {"groundStations": List[str], "noradSatelliteID": int, "satelliteArn": str, "satelliteId": str},
    total=False,
)

SecurityDetailsTypeDef = TypedDict(
    "SecurityDetailsTypeDef",
    {"roleArn": str, "securityGroupIds": List[str], "subnetIds": List[str]},
)

SocketAddressTypeDef = TypedDict("SocketAddressTypeDef", {"name": str, "port": int})

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "configDetails": "ConfigDetailsTypeDef",
        "configId": str,
        "configType": ConfigCapabilityType,
        "dataflowSourceRegion": str,
    },
    total=False,
)

_RequiredSpectrumConfigTypeDef = TypedDict(
    "_RequiredSpectrumConfigTypeDef",
    {"bandwidth": "FrequencyBandwidthTypeDef", "centerFrequency": "FrequencyTypeDef"},
)
_OptionalSpectrumConfigTypeDef = TypedDict(
    "_OptionalSpectrumConfigTypeDef", {"polarization": Polarization}, total=False
)

class SpectrumConfigTypeDef(_RequiredSpectrumConfigTypeDef, _OptionalSpectrumConfigTypeDef):
    pass

TrackingConfigTypeDef = TypedDict("TrackingConfigTypeDef", {"autotrack": Criticality})

UplinkEchoConfigTypeDef = TypedDict(
    "UplinkEchoConfigTypeDef", {"antennaUplinkConfigArn": str, "enabled": bool}
)

_RequiredUplinkSpectrumConfigTypeDef = TypedDict(
    "_RequiredUplinkSpectrumConfigTypeDef", {"centerFrequency": "FrequencyTypeDef"}
)
_OptionalUplinkSpectrumConfigTypeDef = TypedDict(
    "_OptionalUplinkSpectrumConfigTypeDef", {"polarization": Polarization}, total=False
)

class UplinkSpectrumConfigTypeDef(
    _RequiredUplinkSpectrumConfigTypeDef, _OptionalUplinkSpectrumConfigTypeDef
):
    pass

ConfigIdResponseTypeDef = TypedDict(
    "ConfigIdResponseTypeDef",
    {"configArn": str, "configId": str, "configType": ConfigCapabilityType},
    total=False,
)

ContactIdResponseTypeDef = TypedDict("ContactIdResponseTypeDef", {"contactId": str}, total=False)

DataflowEndpointGroupIdResponseTypeDef = TypedDict(
    "DataflowEndpointGroupIdResponseTypeDef", {"dataflowEndpointGroupId": str}, total=False
)

DescribeContactResponseTypeDef = TypedDict(
    "DescribeContactResponseTypeDef",
    {
        "contactId": str,
        "contactStatus": ContactStatus,
        "dataflowList": List["DataflowDetailTypeDef"],
        "endTime": datetime,
        "errorMessage": str,
        "groundStation": str,
        "maximumElevation": "ElevationTypeDef",
        "missionProfileArn": str,
        "postPassEndTime": datetime,
        "prePassStartTime": datetime,
        "region": str,
        "satelliteArn": str,
        "startTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

_RequiredGetConfigResponseTypeDef = TypedDict(
    "_RequiredGetConfigResponseTypeDef",
    {"configArn": str, "configData": "ConfigTypeDataTypeDef", "configId": str, "name": str},
)
_OptionalGetConfigResponseTypeDef = TypedDict(
    "_OptionalGetConfigResponseTypeDef",
    {"configType": ConfigCapabilityType, "tags": Dict[str, str]},
    total=False,
)

class GetConfigResponseTypeDef(
    _RequiredGetConfigResponseTypeDef, _OptionalGetConfigResponseTypeDef
):
    pass

GetDataflowEndpointGroupResponseTypeDef = TypedDict(
    "GetDataflowEndpointGroupResponseTypeDef",
    {
        "dataflowEndpointGroupArn": str,
        "dataflowEndpointGroupId": str,
        "endpointsDetails": List["EndpointDetailsTypeDef"],
        "tags": Dict[str, str],
    },
    total=False,
)

GetMinuteUsageResponseTypeDef = TypedDict(
    "GetMinuteUsageResponseTypeDef",
    {
        "estimatedMinutesRemaining": int,
        "isReservedMinutesCustomer": bool,
        "totalReservedMinuteAllocation": int,
        "totalScheduledMinutes": int,
        "upcomingMinutesScheduled": int,
    },
    total=False,
)

GetMissionProfileResponseTypeDef = TypedDict(
    "GetMissionProfileResponseTypeDef",
    {
        "contactPostPassDurationSeconds": int,
        "contactPrePassDurationSeconds": int,
        "dataflowEdges": List[List[str]],
        "minimumViableContactDurationSeconds": int,
        "missionProfileArn": str,
        "missionProfileId": str,
        "name": str,
        "region": str,
        "tags": Dict[str, str],
        "trackingConfigArn": str,
    },
    total=False,
)

GetSatelliteResponseTypeDef = TypedDict(
    "GetSatelliteResponseTypeDef",
    {"groundStations": List[str], "noradSatelliteID": int, "satelliteArn": str, "satelliteId": str},
    total=False,
)

ListConfigsResponseTypeDef = TypedDict(
    "ListConfigsResponseTypeDef",
    {"configList": List["ConfigListItemTypeDef"], "nextToken": str},
    total=False,
)

ListContactsResponseTypeDef = TypedDict(
    "ListContactsResponseTypeDef",
    {"contactList": List["ContactDataTypeDef"], "nextToken": str},
    total=False,
)

ListDataflowEndpointGroupsResponseTypeDef = TypedDict(
    "ListDataflowEndpointGroupsResponseTypeDef",
    {"dataflowEndpointGroupList": List["DataflowEndpointListItemTypeDef"], "nextToken": str},
    total=False,
)

ListGroundStationsResponseTypeDef = TypedDict(
    "ListGroundStationsResponseTypeDef",
    {"groundStationList": List["GroundStationDataTypeDef"], "nextToken": str},
    total=False,
)

ListMissionProfilesResponseTypeDef = TypedDict(
    "ListMissionProfilesResponseTypeDef",
    {"missionProfileList": List["MissionProfileListItemTypeDef"], "nextToken": str},
    total=False,
)

ListSatellitesResponseTypeDef = TypedDict(
    "ListSatellitesResponseTypeDef",
    {"nextToken": str, "satellites": List["SatelliteListItemTypeDef"]},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

MissionProfileIdResponseTypeDef = TypedDict(
    "MissionProfileIdResponseTypeDef", {"missionProfileId": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
