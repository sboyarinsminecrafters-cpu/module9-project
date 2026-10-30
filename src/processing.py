
def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтруем список операций по статусу"""
    filtered = []
    for operation in operations:
        if operation.get("state") == state:
            filtered.append(operation)

    return filtered


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """Сортируем список операций по дате"""
    sorted_operations = sorted(operations, key=lambda operation: operation.get("date", ""), reverse=reverse)
    return sorted_operations
