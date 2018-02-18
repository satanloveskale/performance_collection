import datetime
from haystack import indexes
from .models import Score, Name, Subject


class ScoreIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    author = indexes.CharField(model_attr='author')
    score_title = indexes.CharField(model_attr='score_title')
    model = Score
    
    def get_model(self):
        return Score

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return Score.objects.all().select_related()
