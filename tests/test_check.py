from ..maigret.sites import SitesInformation
from ..maigret.maigret import sherlock
from ..maigret.notify import QueryNotify, QueryStatus


def test_site(site):
    sites = SitesInformation().sites
    site_data = sites[site].information
    site_data_all = {site: site_data}

    test_cases = [
        {
            'text': 'claimed',
            'status': QueryStatus.CLAIMED,
            'username': site_data['username_claimed'],
        },
        {
            'text': 'available',
            'status': QueryStatus.AVAILABLE,
            'username': site_data['username_unclaimed'],
        },
    ]

    for test_case in test_cases:
        query_notify = QueryNotify()
        results = sherlock(username=test_case['username'],
                                   site_data=site_data_all,
                                   query_notify=query_notify)

        assert results[site]['status'].status == test_case['status']
