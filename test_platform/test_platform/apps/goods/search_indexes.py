# -*- coding: utf-8 -*-
# 开发者:Annona
# 开发时间:2023/12/5 21:09
from haystack import indexes

from goods.models import SKU


class SKUIndex(indexes.SearchIndex, indexes.indexable):
    """SKU索引数据模型类"""
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        """返回建立索引的模型类"""
        return SKU

    def index_queryset(self, using=None):
        """返回要建立索引的数据查询集"""
        return self.get_model().objects.filter(is_launched=True)