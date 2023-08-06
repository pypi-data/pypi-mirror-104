import re
from dataclasses import dataclass, field
from typing import List, Union
from enum import Enum

__all__ = ["ObjectType", "EnumType", "ReferenceType", "File", "TypeAttribute", "Communication", "Constant", "Request",
           "Response", "Type", "Typedef", "PrimitiveType", "Primitive", "WSEvent", "WSEvents"]


class Primitive(Enum):
    Str = 0
    Int = 1
    Float = 2
    Bool = 3
    Any = 4


@dataclass
class PrimitiveType:
    primitive: Primitive
    constants: List["Constant"] = field(default_factory=list)

    def constants_dicts(self):
        return {c.name: c.value for c in self.constants}


@dataclass
class ObjectType:
    name: str
    values: List["Constant"]
    attributes: List["TypeAttribute"]


@dataclass
class EnumType:
    name: str
    values: List[str]


@dataclass
class ReferenceType:
    name: str
    reference: 'Type' = None


Type = Union[PrimitiveType, ObjectType, EnumType, ReferenceType]


@dataclass
class Typedef:
    name: str
    type: Type


@dataclass
class TypeAttribute:
    name: str
    type: Type
    is_optional: bool = False
    is_array: bool = False
    is_wildcard: bool = False


@dataclass
class Response:
    code: int
    attributes: List[TypeAttribute]


@dataclass
class Request:
    method: str
    parameters: List[TypeAttribute]
    responses: List[Response]


@dataclass
class Communication:
    name: str
    values: List["Constant"]
    requests: List[Request]


@dataclass
class Constant:
    name: str
    value: str  # For now only string constants


@dataclass
class File:
    communications: List[Communication]
    global_types: List[Typedef]
    constants: List[Constant]
    ws_events: 'WSEvents'


@dataclass
class WSEvents:
    client: List['WSEvent']
    server: List['WSEvent']


@dataclass
class WSEvent:
    name: str
    data: Union[List[TypeAttribute], ReferenceType]


def url_params_from_uri(uri: str) -> List[str]:
    return re.findall("<([^>]+)>", uri)
