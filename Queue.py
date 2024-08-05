from RestockDetail import RestockDetail

class RestockingQ:
    def __init__(self) -> None:
        self.items: list[RestockDetail] = []

    def __len__(self) -> int:
        return len(self.items)

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def enqueue(self, item: RestockDetail) -> None:
        self.items.append(item)

    def dequeue(self) -> RestockDetail:
        return self.items.pop(0)