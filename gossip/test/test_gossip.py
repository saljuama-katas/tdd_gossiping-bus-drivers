from ..gossip import GossipCalculator


def test_gossips_never_spread_when_there_is_only_one_route():
    calculator = GossipCalculator([[1, 2, 3, 4]])
    assert calculator.gossip_spread_time() is None


def test_gossips_never_spread_with_multiple_routes_that_never_share_a_stop():
    calculator = GossipCalculator([[1, 2, 3], [4, 5, 6]])
    assert calculator.gossip_spread_time() is None


def test_all_gossip_is_spread_in_n_minutes_if_all_routes_share_the_n_plus_one_stop():
    calculator = GossipCalculator([[1, 2, 3], [1, 4, 5]])
    assert calculator.gossip_spread_time() == 0

    calculator = GossipCalculator([[1, 2, 3], [4, 2, 5]])
    assert calculator.gossip_spread_time() == 1

    calculator = GossipCalculator([[1, 2, 3], [4, 5, 3]])
    assert calculator.gossip_spread_time() == 2


def test_drivers_repeat_the_route_once_they_finish():
    calculator = GossipCalculator([[1, 2], [3, 4, 5, 6, 7, 8, 1]])
    assert calculator.gossip_spread_time() == 6


def test_drivers_drive_a_maximum_of_480_stops():
    calculator = GossipCalculator([[1000, 480], list(range(1, 481))])
    assert calculator.gossip_spread_time() == 479

    calculator = GossipCalculator([[481, 1000], list(range(1, 482))])
    assert calculator.gossip_spread_time() is None
