class MergeIntervals:
    def __init__(self, intervals, threshold):
        self.intervals = sorted(intervals, key=lambda x: x[0])
        self.threshold = threshold

    def merge(self):
        merged_intervals = []
        for current_interval in self.intervals:
            if (
                not merged_intervals
                or current_interval[0] > merged_intervals[-1][1] + self.threshold
            ):
                merged_intervals.append(current_interval)
            else:
                merged_intervals[-1][1] = max(
                    merged_intervals[-1][1], current_interval[1]
                )
        return merged_intervals


if __name__ == "__main__":
    merger = MergeIntervals([[0, 300], [600, 1200], [3500, 6000]], 400)
    result = merger.merge()
    print(result)
