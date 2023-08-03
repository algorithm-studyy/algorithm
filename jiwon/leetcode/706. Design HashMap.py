class MyHashMap:

    def __init__(self):
        self.val = dict()

    def put(self, key: int, value: int) -> None:
        self.val[key] = value

    def get(self, key: int) -> int:
        return self.val.get(key, -1)

    def remove(self, key: int) -> None:
        if key in self.val:
            del self.val[key]
