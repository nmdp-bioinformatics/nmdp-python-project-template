# SPDX-FileCopyrightText: 2026 (NMDP) National Marrow Donor Program. All Rights Reserved.
#
# SPDX-License-Identifier: LGPL-3.0-or-later


"""Tests for `my_project_template` package."""

import pytest
from my_project_template.algorithm.match import slug_match
from my_project_template.model.slug import SLUG
from my_project_template.model.allele import Allele


@pytest.fixture
def supported_genes():
    """Sample pytest fixture.

    See more at: https://doc.pytest.org/en/latest/fixture.html
    """
    return ["HLA-A", "HLA-B", "HLA-C"]


def test_content(supported_genes):
    """Sample pytest test function with the pytest fixture as an argument."""
    assert "HLA-A" in supported_genes


def test_slug_match_identical_slugs():
    """Test that identical SLUGs match."""
    allele1 = Allele("HLA-A", "HLA-A*01:01")
    allele2 = Allele("HLA-A", "HLA-A*02:01")
    slug1 = SLUG(allele1, allele2)
    slug2 = SLUG(allele1, allele2)

    assert slug_match(slug1, slug2) is True


def test_slug_match_different_slugs():
    """Test that different SLUGs do not match."""
    allele1 = Allele("HLA-A", "HLA-A*01:01")
    allele2 = Allele("HLA-A", "HLA-A*02:01")
    allele3 = Allele("HLA-A", "HLA-A*03:01")

    slug1 = SLUG(allele1, allele2)
    slug2 = SLUG(allele1, allele3)

    assert slug_match(slug1, slug2) is False
