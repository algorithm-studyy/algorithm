def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[1])
    camera = routes[0][1]
    for route in routes:
        if route[0] > camera:
            camera = route[1]
            answer += 1

    return answer