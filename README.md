# buho-tags
Código base para agregar tags a cualquier entidad de Buho.

## Uso
```python
from buho.tags.models import Tag
from django.db import models


class Product(models.Model):
    ...


class ProductTag(Tag):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='tags')
```
