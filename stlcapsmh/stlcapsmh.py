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

"""Displays website pages."""

import flask

APP = flask.Flask(__name__)

# Core attributes for each page
CORE = {
    'copyright': '© 2018 STL Centers for Advanced Professional Studies '
                 'Medical and Healthcare Program',
    'subtitle': 'Medical and Healthcare Program',
    'title': 'St. Louis Centers for Advanced Professional Studies',
    'twitter_button_txt': 'Follow @STLCAPSMed',
    'twitter_link': 'https://twitter.com/STLCAPSMed'
}

# Website pages
PAGES = [
    {
        'name': 'HOME',
        'title': 'HOME - STL CAPS Medical and Healthcare Program',
        'description': 'This is the official website of the Affton School '
                       'District\'s Biomedical Healthcare Program, a '
                       'division of the St. Louis Center for Advanced '
                       'Professional Studies.',
        'path': '/'
    },
    {
        'name': 'ABOUT',
        'title': 'ABOUT - STL CAPS Medical and Healthcare Program',
        'description': 'This is the official website of the Affton School '
                       'District\'s Biomedical Healthcare Program, a '
                       'division of the St. Louis Center for Advanced '
                       'Professional Studies.',
        'path': '/about',
        'about_content': 'The St. Louis Centers for Advanced Professional '
                         'Studies is a division of the Affton School '
                         'District, and provides junior and senior high '
                         'school students the opportunity to test-drive '
                         'their future in high-skill, high-demand careers '
                         'while embedded in a professional workplace for a '
                         'year-long experience. The Medical and '
                         'Healthcare division of the STL CAPS program '
                         'implements students in the hospital setting, '
                         'providing real world experiences in the field of '
                         'healthcare and medicine in and out of the '
                         'classroom. In the classroom students build a '
                         'vocabulary in anatomical language, investigate '
                         'each human body system, learn proper physical '
                         'assessment skills, develop treatment plans, and '
                         'practice proper patient care.  The activities have '
                         'been designed to improve student analysis and '
                         'problem solving skills.  Students also learn from '
                         'a diverse group of healthcare providers who visit '
                         'the classroom as guest lecturers.  Outside the '
                         'classroom numerous site visits to medical, '
                         'healthcare, and biomedical facilities exposing '
                         'students to a variety of professions and '
                         'advancements.'
    }
]


@APP.route('/')
def get_index():
    """Display the homepage."""
    page = PAGES[0]
    return flask.render_template('core/index.html', core=CORE, pages=PAGES,
                                 page=page)


@APP.route('/about')
def get_about():
    """Display the about page."""
    page = PAGES[1]
    return flask.render_template('pages/about.html', core=CORE, pages=PAGES,
                                 page=page)
