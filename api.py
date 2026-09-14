# -*- coding: utf-8 -*-

#
#    my_project_template My Project Template.
#    Copyright (c) 2021 Be The Match operated by National Marrow Donor Program. All Rights Reserved.
#
#    This library is free software; you can redistribute it and/or modify it
#    under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation; either version 3 of the License, or (at
#    your option) any later version.
#
#    This library is distributed in the hope that it will be useful, but WITHOUT
#    ANY WARRANTY; with out even the implied warranty of MERCHANTABILITY or
#    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
#    License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this library;  if not, write to the Free Software Foundation,
#    Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307  USA.
#
#    > http://www.fsf.org/licensing/licenses/lgpl.html
#    > http://www.opensource.org/licenses/lgpl-license.php
from flask import request

from my_project_template.model.allele import InvalidAllele
from my_project_template.my_project_template import match


def slug_match_controller():
    if request.json:
        # Check the request
        try:
            patient_slug_glstring = request.json["patient_slug"]
            donor_slug_glstring = request.json["donor_slug"]
        except KeyError:
            return {"message": "Invalid data in patient_slug/donor_slug"}, 400
        # Perform match
        try:
            donor_slug, matched, patient_slug = match(
                patient_slug_glstring, donor_slug_glstring
            )
            matched_result = "Match" if matched else "No Match"
            return {
                "matched": matched_result,
                "patient_slug": str(patient_slug),
                "donor_slug": str(donor_slug),
            }, 200
        except InvalidAllele as e:
            return {"message": e.message}, 400

    # if no data is sent
    return {"message": "No input provided"}, 404
