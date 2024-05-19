from typing import Any

class Array:
    def __init__(self, n: int, dtype: Any):
        self.vals = [None] * n
        self.dtype = dtype

    def get(self, i: int) -> Any:
        """
        Возвращает значение как индекс i
        """
        return self.vals[i]

    def put(self, i: int, val: Any) -> None:
        """
        Обновляем массив как индекс i с val. Val должно быть одного типа с self.dtype
        """
        if not isinstance(val, self.dtype):
            raise ValueError(f"val {type(val)}; должно быть {self.dtype}")
        self.vals[i] = val


    def __str__(self) -> str:
        return str(self.vals)


arr = Array(10, str)

arr.get(0)       # None
arr.put(0, 'kot')  # None
arr.get(0)       # 'kot'
arr.put(5, "koshka")
print(arr)

#arr.put(1, 5) -> ValueError: val is <class 'int'>; must be <class 'str'>