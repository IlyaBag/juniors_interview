def appearance(intervals: dict[str, list[int]]) -> int:
    indices_map = {
        0: len(intervals['lesson']) - 1,
        1: len(intervals['pupil']) - 1,
        2: len(intervals['tutor']) - 1,
    }

    common_education_time = 0

    while indices_map[0] > 0 and indices_map[1] > 0 and indices_map[2] > 0:
        end_time = min(
            intervals['lesson'][indices_map[0]],
            intervals['pupil'][indices_map[1]],
            intervals['tutor'][indices_map[2]],
        )
        starts = (
            intervals['lesson'][indices_map[0] - 1],
            intervals['pupil'][indices_map[1] - 1],
            intervals['tutor'][indices_map[2] - 1],
        )
        start_time = max(starts)
        index_to_change = starts.index(start_time)
        indices_map[index_to_change] -= 2

        if start_time < end_time:
            common_education_time += (end_time - start_time)

    return common_education_time
