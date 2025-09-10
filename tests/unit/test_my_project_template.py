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
#


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
