from pydantic import BaseModel, Field
from typing import Optional, Dict

class Document(BaseModel):
    page_content: str
    metadata: Optional[Dict[str, str]] = Field(default_factory=dict)

# 示例用法
doc1 = Document(page_content="Hello, world!")
doc2 = Document(page_content="Another document")

print(doc1)
# 输出: page_content='Hello, world!' metadata={}
print(doc2)
# 输出: page_content='Another document' metadata={'author': 'John Doe'}


