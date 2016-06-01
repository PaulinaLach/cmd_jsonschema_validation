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


"""Minimal Flask application example for development.
Run this example:
.. code-block:: console
    $ cd examples
    $ python app.py
The same result could be created with the cli:
.. code-block:: console
    $ cd examples
    $ mkdir generated
    $ domapping schema_to_mapping schema.json --config config.json | \
        domapping mapping_to_jinja > generated/generated_schema.json
    $ domapping jinja_to_mapping template.json --context_path generated
"""

import json

import doschema.validation as dv


paths_list = ['file1.json', 'file2.json']

schema_validator = dv.JSONSchemaValidator()
for path in paths_list:
    with open(path, 'r', encoding='utf-8') as infile:
        schema = json.load(infile)
        schema_validator.validate(schema, path)
