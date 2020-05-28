from ..gossip import gossip


def test_gossips_never_spread_when_there_is_only_one_route():
    bus_routes = [
        [1, 2, 3, 4]
    ]
    assert gossip(bus_routes) is None


def test_all_gossip_is_spread_in_n_minutes_if_all_routes_share_the_n_plus_one_stop():
    bus_routes = [[1, 2, 3], [1, 4, 5]]
    assert gossip(bus_routes) is 0

    bus_routes = [[1, 2, 3], [4, 2, 5]]
    assert gossip(bus_routes) is 1

    bus_routes = [[1, 2, 3], [4, 5, 3]]
    assert gossip(bus_routes) is 2
