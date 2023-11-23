
class Group:

    _count_st = 0

    def __init__(self, name):
        self._name = name
        self._count_st = 0

    def group_inc(self):
        self._count_st += 1


class Student:

    _spec = ''
    _faculty = ''


    def __init__(self, name):
        self._name = name
        self._group = None

    def set_spec(self,val):
        self._spec = val

    def set_group(self, group):
        if isinstance(group, Group):
            self._group = group._name
            group.group_inc()
        else:
            print(f'Объект не является группой!')

    def set_faculty(self,val):
        self._faculty = val