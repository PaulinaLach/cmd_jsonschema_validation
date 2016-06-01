# -*- coding: utf-8 -*-
#
# This file is part of DoMapping.
# Copyright (C) 2015, 2016 CERN.
#
# DoMapping is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# DoMapping is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with DoMapping; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""CLI commands."""

import json
import click
import doschema.validation as dv

@click.group()
def cli():
    """CLI group."""
    pass  # pragma: no cover


@cli.command()
@click.argument('paths_list', nargs=-1)
#@click.option('--ignore_index', default=True, help='Foo', type=click.BOOL)
              
def validate(paths_list):
    schema_validator = dv.JSONSchemaValidator()
    print('starting')
    for path in paths_list:
        print(path)
        with open(path, 'r', encoding='utf-8') as infile:
            print('parsing json')
            schema = json.load(infile)
            schema_validator.validate(schema, path)