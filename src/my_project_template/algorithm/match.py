# SPDX-FileCopyrightText: 2026 (NMDP) National Marrow Donor Program. All Rights Reserved.
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from my_project_template.model.slug import SLUG


def slug_match(patient_slug: SLUG, donor_slug: SLUG) -> bool:
    """
    SLUGs are matched if they are equal to each other

    @param patient_slug: Patient SLUG
    @param donor_slug: Donor SLUG
    @return: bool indicating whether they match or not
    """
    return patient_slug == donor_slug
