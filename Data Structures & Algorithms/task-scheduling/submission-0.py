from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 统计每个任务的出现次数
        freq = Counter(tasks)

        # 找出最多任务数
        max_freq = max(freq.values())

        # 统计有多少任务出现了 max_freq 次
        max_count = sum(1 for task in freq.values() if task == max_freq)

        # 计算框架长度
        part_count = max_freq - 1
        part_length = n - (max_count - 1)
        empty_slots = part_count * part_length
        available_tasks = len(tasks) - max_freq * max_count
        idles = max(0, empty_slots - available_tasks)

        return len(tasks) + idles
