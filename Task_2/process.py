def sheep_jumps_to_next_stone(A, D):
    total_distance = len(A)
    if D >= total_distance:
        return 0

    max_time = max(time + i for i, time in enumerate(A))  # Calculate the maximum time when a stone will be out of the water.
    stones_out_of_water = set()
    stones_out_of_water.add(0)  # The first stone is always available

    for time in range(1, max_time + 1):
        max_jump = min(D, total_distance)  # Calculate the maximum jump the sheep can make
        reachable_stones = set()

        for stone in stones_out_of_water:
            for jump in range(1, max_jump + 1):
                next_position = stone + jump

                if next_position == total_distance - 1:
                    return time

                if next_position < total_distance and A[next_position] <= time: # Check if the stone at next_position is out of the water at the current time
                    reachable_stones.add(next_position) # if we add next pos. to the reachable_stone set, sheep can jump to it on the next iteration

        stones_out_of_water = reachable_stones # update stones_out_of_water to include new reachable stones

    return -1