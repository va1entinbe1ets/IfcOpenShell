# BlenderBIM Add-on - OpenBIM Blender Add-on
# Copyright (C) 2021 Dion Moult <dion@thinkmoult.com>
#
# This file is part of BlenderBIM Add-on.
#
# BlenderBIM Add-on is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BlenderBIM Add-on is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BlenderBIM Add-on.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import annotations
import bpy
import ifcopenshell.api
import ifcopenshell.util.classification
import blenderbim.core.tool
import blenderbim.tool as tool
import blenderbim.bim
from typing import Any, Optional, Union, Literal, Iterable, Callable
from typing_extensions import assert_never


class Classification(blenderbim.core.tool.Classification):
    @classmethod
    def get_location(cls, classification: ifcopenshell.entity_instance) -> Union[str, None]:
        schema = classification.file.schema
        if schema in ("IFC4", "IFC4X3"):
            return classification[5]
        elif schema == "IFC2X3":
            return None
        assert_never(schema)

    @classmethod
    def set_location(cls, classification: ifcopenshell.entity_instance, location: Union[str, None]) -> None:
        schema = classification.file.schema
        if schema in ("IFC4", "IFC4X3"):
            classification[5] = location
            return
        elif schema == "IFC2X3":
            return
        assert_never(schema)
