class BadVersion:
    @staticmethod
    def is_bad_version(n):
        first = 16
        if n >= first:
            return True
        return False

    @staticmethod
    def first_bad_version(first):
        beg, last = 1, first
        pos = 1
        while beg <= last:
            mid = beg + (last - beg) // 2
            x = BadVersion.is_bad_version(mid)
            if x:
                pos = mid
                last = mid - 1
            else:
                beg = mid + 1
        return pos

if __name__ == "__main__":
    print(BadVersion.first_bad_version(19))
    