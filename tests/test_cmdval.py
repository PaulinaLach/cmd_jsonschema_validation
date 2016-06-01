# -*- coding: utf-8 -*-
#
# This file is part of DoSchema.
# Copyright (C) 2016 CERN.
#
# DoSchema is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# DoSchema is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with DoSchema; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

import os

from click.testing import CliRunner
from doschema.cmdval import validate


def test_cli():
    """Test add action role in access CLI."""
    runner = CliRunner()
    files = ['jsonschema_f1.json', 'jsonschema_f2.json']
    current_dir = os.getcwd()
    print('1')

    def data_path(filename):
        return os.path.join(current_dir, 'tests', 'data_files', filename)

    print('2')
    print([data_path(filename) for filename in files])
    result = runner.invoke(
        validate, [data_path(filename) for filename in files])
    print('3')
    print(result.exit_code)
    assert result.exit_code != 0
    print('4')


def test_cli_exception():
    """Test add action role in access CLI."""
    runner = CliRunner()
    files = ['jsonschema_f2.json', 'jsonschema_f3.json']
    current_dir = os.getcwd()

    def data_path(filename):
        return os.path.join(current_dir, 'tests', 'data_files', filename)

    print([data_path(filename) for filename in files])
    result = runner.invoke(
        validate, [data_path(filename) for filename in files])
    print(result.exit_code)
    assert result.exit_code == 0
