
class TestSort:
    
    def __init__(self, sec = []):
        self._sec = sec

    def sort(self):
        t = len(self._sec)
        temp = 0

        for i in range(0,t):
            f_val = self._sec[i]
            f_ind = i
            for j in range(i, t):
                if self._sec[j] < f_val:
                    f_val = self._sec[j]
                    f_ind = j
            temp = self._sec[i]
            self._sec[i] = f_val
            self._sec[f_ind] = temp
        return self._sec


a = TestSort([2,5,6,7,1,4,3])
print(a.sort())