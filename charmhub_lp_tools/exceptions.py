#
# Copyright (C) 2023 Canonical Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Charmhub LP Tools error classes."""


class CharmcraftError504(Exception):
    """charmcraft failed with a error 504 from charmhub."""


class InvalidRiskLevel(Exception):
    """Invalid risk level."""


class BranchNotFound(Exception):
    """Branch not found."""


class CharmNameNotFound(Exception):
    """Charm name not found declared in osci.yaml."""
