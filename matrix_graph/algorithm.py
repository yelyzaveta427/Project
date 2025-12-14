def hasHamiltonianCycle(graph) -> bool:
    n = len(graph)
    start_vertex = 0
    max_states = 2 ** n

    dp = []
    for i in range(max_states):
        row = []
        for j in range(n):
            row.append(False)
        dp.append(row)
    dp[1][0] = True

    dp[2 ** start_vertex][start_vertex] = True

    for mask in range(1, max_states):
        for v in range(n):

            if mask & (2 ** v):
                prev_mask = mask ^ (2 ** v)
                if prev_mask == 0:
                    continue
                for u in graph.get(v, []):
                    if (prev_mask & (2 ** u)) and dp[prev_mask][u]:
                        dp[mask][v] = True
                        break

    full_mask = max_states - 1

    for v in range(n):
        if dp[full_mask][v]:
            if start_vertex in graph.get(v, []):
                return True
    return False