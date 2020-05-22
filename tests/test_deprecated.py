"""
SPDX-FileCopyrightText: 2019 oemof developer group <contact@oemof.org>
SPDX-License-Identifier: MIT
"""

import warnings

import pytest

from windpowerlib.data import load_turbine_data_from_oedb
from windpowerlib.wind_turbine import get_turbine_types


def test_old_import():
    msg = "Use >>from windpowerlib import get_turbine_types"
    with pytest.raises(ImportError, match=msg):
        get_turbine_types()


def test_old_name_load_data_from_oedb():
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        msg = "store_turbine_data_from_oedb"
        with pytest.raises(FutureWarning, match=msg):
            load_turbine_data_from_oedb()
