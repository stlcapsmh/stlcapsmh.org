# The contents of this file are subject to the Common Public Attribution
# License Version 1.0 (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
#
#     https://opensource.org/licenses/CPAL-1.0
#
# The License is based on the Mozilla Public License Version 1.1 but Sections
# 14 and 15 have been added to cover use of software over a computer network
# and provide for limited attribution for the Original Developer. In addition,
# Exhibit A has been modified to be consistent with Exhibit B.
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for
# the specific language governing rights and limitations under the License.
#
# The Original Code is stlcapsmh.org. The Original Developer is the Initial
# Developer and are volunteers of the St. Louis Centers for Advanced
# Professional Studies Medical and Healthcare program. All portions of the code
# written by volunteers of the St. Louis Centers for Advanced Professional
# Studies are
#
# Copyright (c) 2018 St. Louis Centers for Advanced Professional Studies
# Medical and Healthcare Program. All Rights Reserved.

import flask
import pytest


from stlcapsmh import stlcapsmh

@pytest.fixture
def client():
    stlcapsmh.APP.config['TESTING'] = True
    client = stlcapsmh.APP.test_client()

    yield client

def test_get_index(client):
    """Test the rendered home page template for declared data"""
    response = client.get('/')

    # Verify rendered template contains core content
    for core_metadata in stlcapsmh.CORE.values():
        assert core_metadata.encode() in response.data

    # Verify rendered template contains page content
    page = stlcapsmh.PAGES[0]
    assert page['name'].encode() in response.data
    assert page['title'].encode() in response.data

def test_get_about(client):
    """Test the rendered about page template for declared data"""
    response = client.get('/about')

    # Verify rendered template contains core content
    for core_metadata in stlcapsmh.CORE.values():
        assert core_metadata.encode() in response.data

    # Verify rendered template contains page content
    page = stlcapsmh.PAGES[1]
    assert page['name'].encode() in response.data
    assert page['title'].encode() in response.data

def test_get_apply(client):
    """Test the rendered apply page template for declared data"""
    response = client.get('/apply')

    # Verify rendered template contains core content
    for core_metadata in stlcapsmh.CORE.values():
        assert core_metadata.encode() in response.data

    # Verify rendered template contains page content
    page = stlcapsmh.PAGES[2]
    assert page['name'].encode() in response.data
    assert page['title'].encode() in response.data

