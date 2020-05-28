from ..gossip import gossip


def test_gossips_never_spread_when_there_is_only_one_route():
    bus_routes = [
        [1, 2, 3, 4]
    ]
    assert gossip(bus_routes) is None


def test_all_gossip_is_spread_when_all_routes_start_in_the_same_stop():
    bus_routes = [
        [1, 2, 3, 4],
        [1, 5, 7, 8]
    ]
    assert gossip(bus_routes) is 0


def test_all_gossip_is_spread_in_one_minute_if_all_routes_share_the_second_stop():
    bus_routes = [
        [1, 5, 3, 4],
        [2, 5, 7, 8]
    ]
    assert gossip(bus_routes) is 1
