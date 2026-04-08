class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.bucket = [[] for _ in range(self.size)]

    def get_bucket(self,key):
        index = key % self.size
        return self.bucket[index]

    def add(self, key: int) -> None:
        bucket = self.get_bucket(key)
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.get_bucket(key)
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        bucket = self.get_bucket(key)
        return key in bucket

        
# Your Myget_bucketSet object will be instantiated and called as such:
# obj = Myget_bucketSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)