from enum import Enum
from typing import Union

class GenderTypes(Enum):

    MALE = ('male', 'Male')
    FEMALE = ('female', 'Female')

    val = lambda x : x.value[0]
    label = lambda x : x.value[1]
    selection = lambda x : (x.value[0],x.value[1])

    @classmethod
    def get_selection_gender_type(cls):
        _selection = []
        for gender_type in cls:
            _selection.append(gender_type.selection())
        return _selection

    @classmethod
    def get_label_for_type(cls, find_value:str) -> Union[str, None]:
        return next((label for value, label in cls.get_selection_gender_type() if value==find_value), None)

class MartialStatus(Enum):

    SINGLE = ('single','Single')
    MARRIED = ('married','Married')

    val = lambda x : x.value[0]
    label = lambda x : x.value[1]
    selection = lambda x : (x.value[0],x.value[1])

    @classmethod
    def get_martial_status(cls):
        _selection = []
        for martial_type in cls:
            _selection.append(martial_type.selection())
        return _selection

    @classmethod
    def get_label_for_type(cls, find_value:str) -> Union[str, None]:
        return next((label for value, label in cls.get_martial_status() if value==find_value), None)
