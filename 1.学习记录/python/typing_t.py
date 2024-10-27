from typing import List, Dict, Tuple, Set
#### 基本类型

"""
List: 用于表示一个包含特定类型元素的列表。
Dict: 用于表示一个键值对的字典，其中键和值都是特定类型。
Tuple: 用于表示一个固定长度和特定类型的元组。
Set: 用于表示一个包含特定类型元素的集合。
"""
def process_numbers(numbers: List[int]) -> List[int]:
    return [n * 2 for n in numbers]

def map_strings_to_integers(mapping: Dict[str, int]) -> Dict[str, int]:
    return {k: v + 1 for k, v in mapping.items()}

def get_coordinates() -> Tuple[float, float]:
    return (45.0, 90.0)

def unique_elements(elements: Set[str]) -> Set[str]:
    return set(elements)

# 使用示例
print(process_numbers([1, 2, 3]))
print(map_strings_to_integers({'a': 1, 'b': 2}))
print(get_coordinates())
print(unique_elements({'apple', 'banana', 'apple'}))


####可选和联合类型
"""
Optional: 用于表示一个值可以是某种类型或 None。
Union: 用于表示一个值可以是多种类型之一。
"""
from typing import Optional, Union
def get_user_id(user: Optional[str]) -> Optional[int]:
    if user:
        return len(user)
    return None

def process_input(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return f"Processed integer: {value}"
    else:
        return f"Processed string: {value}"

# 使用示例
print(get_user_id("Alice"))
print(get_user_id(None))
print(process_input(42))
print(process_input("Hello"))

#### 泛型
"""
TypeVar: 用于定义泛型类型变量。
Generic: 用于定义一个类的泛型。
"""

from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

# 使用示例
stack = Stack[int]()
stack.push(1)
stack.push(2)
print(stack.pop())
print(stack.pop())


####Callable
"""
Callable: 用于表示一个可调用对象（如函数），并指定其参数类型和返回类型。
"""
from typing import Callable

def apply_function(x: int, func: Callable[[int], int]) -> int:
    return func(x)

def square(n: int) -> int:
    return n * n

# 使用示例
print(apply_function(4, square))

####Any

"""
Any: 用于表示任意类型。这在类型未知或不关心类型的情况下非常有用。
"""
from typing import Any

def print_value(value: Any) -> None:
    print(f"The value is {value}")

# 使用示例
print_value(42)
print_value("Hello")
print_value([1, 2, 3])


"""
NewType: 用于创建类型的别名，通常用于区分逻辑上不同的相同底层类型。
"""
from typing import NewType

UserId = NewType('UserId', int)

def get_user_name(user_id: UserId) -> str:
    return f"User_{user_id}"

# 使用示例
user_id = UserId(123)
print(get_user_name(user_id))


"""
TypedDict: 用于定义具有特定键和值类型的字典。
"""

from typing import TypedDict

class User(TypedDict):
    name: str
    age: int

def get_user_info(user: User) -> str:
    return f"{user['name']} is {user['age']} years old."

# 使用示例
user_info = User(name="Alice", age=30)
print(get_user_info(user_info))




