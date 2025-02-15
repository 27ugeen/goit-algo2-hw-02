from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int

@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int

def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    """
    Оптимізує чергу 3D-друку згідно з пріоритетами та обмеженнями принтера

    Args:
        print_jobs: Список завдань на друк
        constraints: Обмеження принтера

    Returns:
        Dict з порядком друку та загальним часом
    """
    # Перетворюємо вхідні дані у список об'єктів PrintJob
    jobs = [PrintJob(**job) for job in print_jobs]

    # Сортуємо завдання за пріоритетом (найвищий 1 → 2 → 3)
    jobs.sort(key=lambda job: job.priority)

    max_volume = constraints["max_volume"]
    max_items = constraints["max_items"]

    print_order = []
    total_time = 0

    i = 0
    while i < len(jobs):
        current_batch = []
        current_volume = 0

        # Додаємо завдання у поточну групу поки не перевищені обмеження
        while i < len(jobs) and len(current_batch) < max_items and current_volume + jobs[i].volume <= max_volume:
            current_batch.append(jobs[i])
            current_volume += jobs[i].volume
            i += 1

        # Додаємо ідентифікатори в загальний порядок
        print_order.extend(job.id for job in current_batch)

        # Час друку групи = найдовше завдання у групі
        batch_time = max(job.print_time for job in current_batch)
        total_time += batch_time

    return {
        "print_order": print_order,
        "total_time": total_time
    }