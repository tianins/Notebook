# py相关教程

## 1.typing

在 Python 中，`typing` 模块提供了许多工具和类型，用于为变量、函数参数和返回值添加类型注释。以下是一些常见的 `typing` 用法及示例：

### 基本类型

1. **List**: 用于表示一个包含特定类型元素的列表。
2. **Dict**: 用于表示一个键值对的字典，其中键和值都是特定类型。
3. **Tuple**: 用于表示一个固定长度和特定类型的元组。
4. **Set**: 用于表示一个包含特定类型元素的集合。

### 可选和联合类型

1. **Optional**: 用于表示一个值可以是某种类型或 `None`。
2. **Union**: 用于表示一个值可以是多种类型之一。

### 泛型

1. **TypeVar**: 用于定义泛型类型变量。
2. **Generic**: 用于定义一个类的泛型。

### Callable

1. **Callable**: 用于表示一个可调用对象（如函数），并指定其参数类型和返回类型。

### Any

1. **Any**: 用于表示任意类型。这在类型未知或不关心类型的情况下非常有用。

### NewType

1. **NewType**: 用于创建类型的别名，通常用于区分逻辑上不同的相同底层类型。

### TypedDict

1. **TypedDict**: 用于定义具有特定键和值类型的字典。

`typing` 模块在 Python 中提供了丰富的类型提示工具，可以显著提高代码的可读性和可维护性。通过使用这些类型提示，你可以更好地定义函数参数和返回值的类型，减少错误，并利用静态类型检查工具（如 `mypy`）提高代码质量。

```
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

```



## 2.关键字参数解包

```
from pydantic import BaseModel
from typing import List, Dict

class Address(BaseModel):
    street: str
    city: str
    country: str

class User(BaseModel):
    id: int
    name: str
    addresses: List[Address]
    metadata: Dict[str, str]

# 示例数据
data = {
    "id": 1,
    "name": "John Doe",
    "addresses": [
        {"street": "123 Main St", "city": "Anytown", "country": "USA"},
        {"street": "456 Elm St", "city": "Othertown", "country": "USA"}
    ],
    "metadata": {
        "nickname": "johnny",
        "occupation": "developer"
    }
}

# 使用 **data 解包字典并传递给 User 的构造函数
user = User(**data)

print(user)

# 其中 User(**data)作用与挨个传递参数相等
user = User(
    id=1,
    name="John Doe",
    addresses=[
        {"street": "123 Main St", "city": "Anytown", "country": "USA"},
        {"street": "456 Elm St", "city": "Othertown", "country": "USA"}
    ],
    metadata={
        "nickname": "johnny",
        "occupation": "developer"
    }
)
```

`**data` 是 Python 中的一个语法，用于将字典中的键值对作为关键字参数传递给函数或类的构造函数。这种语法被称为“字典解包”或“关键字参数解包”。

### 具体解释

当你有一个字典 `data`，其中的键对应参数名称，值对应参数值时，你可以使用 `**data` 语法将该字典解包，并将其中的键值对作为关键字参数传递给函数或类的构造函数。

### 使用场景

1. **简化代码**：
   - 当你有一个字典，包含了所有需要传递给函数或构造函数的参数时，使用 `**` 语法可以简化代码，避免显式地列出所有参数。
2. **动态参数传递**：
   - 当参数集合是动态生成的（例如，从配置文件读取或通过网络请求获取），使用 `**` 语法可以方便地将这些动态参数传递给函数或构造函数。
3. **提高可读性**：
   - 使用字典解包语法可以提高代码的可读性，使参数传递更加清晰。



## 2.pydantic

`pydantic` 是一个非常有用的库，特别适用于需要进行数据验证、解析和管理的场景。以下是一些常见的使用场景和具体实例，说明什么时候需要用到 `pydantic`：

### 1. **API 数据验证**

在开发API时，需要确保客户端发送的数据符合预期格式和类型。`pydantic` 可以帮助验证请求数据，并自动生成响应数据。

```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.post("/items/")
async def create_item(item: Item):
    return item

# 运行后访问 http://127.0.0.1:8000/docs 可以看到自动生成的API文档

```

### 2. **配置管理**

`pydantic` 可以用来加载和验证配置数据，例如从环境变量、配置文件或其他来源读取配置。

```
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str
    admin_email: str
    items_per_user: int

    class Config:
        env_file = ".env"  # 指定环境变量文件

# 加载配置
settings = Settings()

# 使用配置
print(settings.app_name)
print(settings.admin_email)
print(settings.items_per_user)

```

`.env` 文件是一个简单的文本文件，用于存储环境变量。每行包含一个键值对，格式为 `KEY=VALUE`。这是一个非常常见的方式来管理应用程序的配置，特别是在开发和生产环境中。

创建和设置 `.env` 文件

1. **文件位置**：将 `.env` 文件放在项目的根目录下（通常与 `main.py` 或 `app.py` 文件同一目录）。
2. **键值对格式**：每行一个键值对，使用 `=` 分隔键和值。值可以是字符串、数字、布尔值等。

```
# Application configuration
APP_NAME=MyCoolApp
DEBUG=True

# Database configuration
DATABASE_URL=postgresql://user:password@localhost:5432/mydatabase

# Email configuration
ADMIN_EMAIL=admin@example.com
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
SMTP_USER=smtp_user
SMTP_PASSWORD=smtp_password

# Other settings
ITEMS_PER_USER=10

```

### 3. **数据解析和验证**

在处理外部数据（如JSON、XML等）时，`pydantic` 可以帮助解析这些数据并进行类型验证。

```
from pydantic import BaseModel
import json

class User(BaseModel):
    id: int
    name: str
    email: str

json_data = '{"id": 123, "name": "John Doe", "email": "john.doe@example.com"}'
user = User.parse_raw(json_data)

print(user)
# 输出: id=123 name='John Doe' email='john.doe@example.com'

```

### 4. **数据转换**

`pydantic` 提供了方便的方法来将数据模型转换为其他格式，例如字典、JSON等。这对于数据存储和传输非常有用。

```
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float

product = Product(name="Laptop", price=999.99)
product_dict = product.dict()
product_json = product.json()

print(product_dict)
# 输出: {'name': 'Laptop', 'price': 999.99}

print(product_json)
# 输出: {"name": "Laptop", "price": 999.99}

```

### 5. **复杂数据结构**

`pydantic` 支持嵌套模型、列表、字典等复杂数据结构的定义和验证。这对于处理复杂的数据模型非常有用。

```
from pydantic import BaseModel
from typing import List, Dict

class Address(BaseModel):
    street: str
    city: str
    country: str

class User(BaseModel):
    id: int
    name: str
    addresses: List[Address]

data = {
    "id": 1,
    "name": "John Doe",
    "addresses": [
        {"street": "123 Main St", "city": "Anytown", "country": "USA"},
        {"street": "456 Elm St", "city": "Othertown", "country": "USA"}
    ]
}

user = User(**data)
print(user)
# 输出: id=1 name='John Doe' addresses=[Address(street='123 Main St', city='Anytown', country='USA'), Address(street='456 Elm St', city='Othertown', country='USA')]

```



### 6. Field 的参数

`Field` 函数接受多个参数，这些参数可以用来定义字段的各种属性和校验规则：

- **default**: 字段的默认值。
- **default_factory**: 用于动态生成默认值的工厂函数。
- **alias**: 字段的别名，用于序列化和反序列化。
- **title**: 字段的标题，常用于文档生成。
- **description**: 字段的描述信息，常用于文档生成。
- **gt**: 指定字段值必须大于指定值（greater than）。
- **ge**: 指定字段值必须大于等于指定值（greater than or equal to）。
- **lt**: 指定字段值必须小于指定值（less than）。
- **le**: 指定字段值必须小于等于指定值（less than or equal to）。
- **regex**: 指定字段值必须匹配的正则表达式。
- **min_length**: 字段值的最小长度（适用于字符串、列表等）。
- **max_length**: 字段值的最大长度（适用于字符串、列表等）。



```
from pydantic import BaseModel, Field
from typing import Optional

class Document(BaseModel):
    """Class for storing a piece of text and associated metadata."""
    page_content: str
    metadata: Optional[dict] = Field(default_factory=dict) # 默认为空字典

# 示例用法
doc = Document(page_content="Hello, world!", metadata={"author": "John Doe"})
print(doc)
# 输出: page_content='Hello, world!' metadata={'author': 'John Doe'}

# 验证失败示例
try:
    doc = Document(page_content=123)  # page_content 应该是 str 类型
except ValueError as e:
    print(e)
# 输出: 1 validation error for Document
# page_content
#   str type expected (type=type_error.str)

```

- 

## 3.ABC(抽象基类)

支持多态性是面向对象编程中的一个重要概念，它允许你在代码中使用基类类型来引用具体子类的对象，而无需关心这些对象的具体类型。这使得代码可以处理不同类型的对象，而不需要硬编码具体的实现，从而提高代码的灵活性和扩展性。

### 如何理解多态性

1. **统一接口**：
   - 抽象基类定义了一个统一的接口，所有子类都必须实现这个接口的方法。这样，你可以编写依赖于这个接口的方法，而不需要知道具体的子类实现。
2. **灵活调用**：
   - 通过接受基类类型的参数，方法可以处理任何继承自这个基类的对象。这使得代码可以处理多种不同的子类对象，而不需要为每种子类编写专门的代码。

### 示例

假设我们有一个抽象基类 `BaseDocumentTransformer`，以及几个具体的子类实现：

```python
from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Any
from pydantic import BaseModel

class Document(BaseModel):
    page_content: str
    metadata: dict = {}

class BaseDocumentTransformer(ABC):
    @abstractmethod
    def transform_documents(self, documents: Sequence[Document], **kwargs: Any) -> Sequence[Document]:
        pass

    @abstractmethod
    async def atransform_documents(self, documents: Sequence[Document], **kwargs: Any) -> Sequence[Document]:
        pass

class SimpleTransformer(BaseDocumentTransformer):
    def transform_documents(self, documents: Sequence[Document], **kwargs: Any) -> Sequence[Document]:
        return [Document(page_content=doc.page_content.upper(), metadata=doc.metadata) for doc in documents]

    async def atransform_documents(self, documents: Sequence[Document], **kwargs: Any) -> Sequence[Document]:
        return [Document(page_content=doc.page_content.lower(), metadata=doc.metadata) for doc in documents]

class ComplexTransformer(BaseDocumentTransformer):
    def transform_documents(self, documents: Sequence[Document], **kwargs: Any) -> Sequence[Document]:
        return [Document(page_content=doc.page_content[::-1], metadata=doc.metadata) for doc in documents]

    async def atransform_documents(self, documents: Sequence[Document], **kwargs: Any) -> Sequence[Document]:
        return [Document(page_content="".join(reversed(doc.page_content)), metadata=doc.metadata) for doc in documents]

```

### 编写支持多态性的函数

由于所有的转换器都继承自 `BaseDocumentTransformer` 并实现了其抽象方法，我们可以编写一个函数，它接受 `BaseDocumentTransformer` 类型的参数，从而支持所有的子类：

```python
def process_documents(transformer: BaseDocumentTransformer, documents: Sequence[Document]) -> Sequence[Document]:
    return transformer.transform_documents(documents)

# 示例文档列表
docs = [Document(page_content="Hello World"), Document(page_content="OpenAI GPT")]

# 使用 SimpleTransformer
simple_transformer = SimpleTransformer()
transformed_docs = process_documents(simple_transformer, docs)
for doc in transformed_docs:
    print(doc.page_content)  # 输出: HELLO WORLD, OPENAI GPT

# 使用 ComplexTransformer
complex_transformer = ComplexTransformer()
transformed_docs = process_documents(complex_transformer, docs)
for doc in transformed_docs:
    print(doc.page_content)  # 输出: dlroW olleH, TPG IAOepnO

```

### 何时使用

在开发Python项目时，是否需要定义抽象基类取决于具体的需求和项目的复杂性。抽象基类（ABC）的主要作用是提供一个框架或接口，使得不同的实现方式可以被统一管理和调用。以下是一些典型的场景，说明在什么时候需要使用抽象基类：

#### 1. **定义统一接口**

当你需要为一组相关的类定义一个统一的接口时，抽象基类非常有用。比如，假设你在开发一个文档处理系统，不同的文档处理器有不同的实现，但都应该有相同的方法接口，如 `transform_documents` 和 `atransform_documents`。通过定义抽象基类，你可以确保所有的处理器都遵循相同的接口。

#### 2. **强制子类实现特定方法**

当你希望确保所有子类都实现某些特定的方法时，抽象基类可以强制子类实现这些方法。没有实现这些抽象方法的类将无法实例化，从而避免运行时错误。

#### 3. **提供默认实现**

你可以在抽象基类中提供一些方法的默认实现，而只需要子类实现特定的抽象方法。这可以减少代码重复，并确保某些基础功能的一致性。

#### 4. **提高代码的灵活性和可扩展性**

抽象基类允许你编写与具体实现无关的代码，使代码更具灵活性和可扩展性。例如，假设你有一个函数需要处理各种类型的支付方式（信用卡、PayPal等），你可以定义一个抽象基类 `PaymentProcessor`，然后为每种具体支付方式创建子类实现。这样，你的函数只需要接受 `PaymentProcessor` 类型的参数，而不需要关心具体的支付方式。

#### 5. **适用于框架和库**

当你在开发一个框架或库时，抽象基类可以帮助定义清晰的扩展点和接口，使得用户可以方便地扩展和定制框架的行为。例如，在Web框架中，你可以定义一个抽象基类 `RequestHandler`，用户可以继承这个基类并实现具体的请求处理逻辑。

#### 具体示例

##### 示例1：文件处理系统

假设你有一个文件处理系统，需要处理不同类型的文件（如文本文件、图像文件）。你可以定义一个抽象基类 `FileProcessor`，并强制子类实现 `process` 方法。

```python
from abc import ABC, abstractmethod

class FileProcessor(ABC):
    @abstractmethod
    def process(self, file_path: str) -> None:
        pass

class TextFileProcessor(FileProcessor):
    def process(self, file_path: str) -> None:
        with open(file_path, 'r') as file:
            content = file.read()
            # 处理文本文件内容
            print(f"Processed text file: {content}")

class ImageFileProcessor(FileProcessor):
    def process(self, file_path: str) -> None:
        # 处理图像文件
        print(f"Processed image file: {file_path}")

def process_file(file_processor: FileProcessor, file_path: str) -> None:
    file_processor.process(file_path)

# 使用不同的文件处理器
text_processor = TextFileProcessor()
image_processor = ImageFileProcessor()

process_file(text_processor, 'example.txt')
process_file(image_processor, 'example.png')

```

##### 示例2：支付处理系统

假设你有一个支付处理系统，需要处理不同的支付方式。你可以定义一个抽象基类 `PaymentProcessor`，并强制子类实现 `process_payment` 方法。

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        # 信用卡支付逻辑
        print(f"Processed credit card payment of {amount}")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        # PayPal支付逻辑
        print(f"Processed PayPal payment of {amount}")

def process_payment(processor: PaymentProcessor, amount: float) -> None:
    processor.process_payment(amount)

# 使用不同的支付处理器
cc_processor = CreditCardProcessor()
paypal_processor = PayPalProcessor()

process_payment(cc_processor, 100.0)
process_payment(paypal_processor, 200.0)

```

### 何时不使用抽象基类

- **简单项目**：对于小型、简单的项目，定义抽象基类可能会增加不必要的复杂性。
- **单一实现**：如果你确定某个功能只会有一种实现，抽象基类并没有太大意义。

### 结论

使用抽象基类的关键在于项目的复杂性和需求。如果你需要定义统一的接口、强制子类实现特定方法、提高代码的灵活性和可扩展性，那么抽象基类是一个非常有效的工具。在这些场景下，抽象基类可以帮助你编写更具结构化和可维护性的代码。