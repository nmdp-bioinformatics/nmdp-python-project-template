# SPDX-FileCopyrightText: 2026 (NMDP) National Marrow Donor Program. All Rights Reserved.
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from .algorithm.match import slug_match
from .model.slug import SLUG


def match(patient_slug_glstring, donor_slug_glstring):
    """
    Perform match on GL String versions of SLUGs

    @param patient_slug_glstring: Patient's SLUG in GL String format
    @param donor_slug_glstring: Donor's SLUG in GL String format
    @return: bool indicating Match or No Match
    """
    patient_slug = SLUG.from_glstring(patient_slug_glstring)
    donor_slug = SLUG.from_glstring(donor_slug_glstring)
    matched = slug_match(patient_slug, donor_slug)
    return donor_slug, matched, patient_slug
