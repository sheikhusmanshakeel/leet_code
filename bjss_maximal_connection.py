def calculate_new_rank(total_connections):
    dict_seen = {}
    max_rank = 1
    for i in range(total_connections):
        if not dict_seen.keys().__contains__(total_connections[i]):
            max_rank += 1
    return max_rank


def return_connected_cities_rank(rank_network, a, b, city1, max_rank_so_far):
    collected_cities = []
    max_rank_so_far = 0
    for i in range(len(b)):
        if b[i] == city1:
            connected_city1 = a[i]
            if rank_network.keys().__contains__(connected_city1):
                x = rank_network[connected_city1]
                new_max_rank = calculate_new_rank(collected_cities.append(x))
                if new_max_rank > max_rank_so_far:
                    max_rank_so_far = new_max_rank

    return max_rank_so_far


def solution(a, b, number_of_cities):
    # write your code in Python 3.6
    rank_network = {}
    max_rank_so_far = 0
    for c in range(number_of_cities):
        city1 = a[c]
        city2 = b[c]
        connected_max_rank = return_connected_cities_rank(rank_network,a,b,city1,max_rank_so_far)
        if connected_max_rank > max_rank_so_far:
            max_rank_so_far = connected_max_rank
        else:
            max_rank_so_far += 1

        if not rank_network.keys().__contains__(city1):
            rank_network[city1]

        if rank_network.keys().__contains__(city1):
            # check if any other cities are connected in the rank_network
            new_max_rank = return_connected_cities_rank(rank_network, a, b, city1, max_rank_so_far)
            rank_network[city1] = [city2]
            new_max_rank += 1
            if new_max_rank > max_rank_so_far:
                max_rank_so_far = new_max_rank
        else:
            if max_rank_so_far == 0:
                max_rank_so_far = 1
    return max_rank_so_far


a = [1, 2, 3, 4]
b = [2, 3, 1, 4]
number_of_cities = 4
number_of_roads = len(a)
solution(a,b,number_of_cities)