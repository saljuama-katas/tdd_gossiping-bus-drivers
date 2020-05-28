def gossip(routes):
    if len(routes) < 2:
        return None

    for x in range(3):
        if routes[0][x] == routes[1][x]:
            return x

    return None
