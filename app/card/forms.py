from django import forms
from app.models import Player

class CardForm(forms.Form):
    name = forms.CharField(max_length=32, label="名字", help_text="點數卡的名子", required=False)
    value = forms.IntegerField(label="值", help_text="點數卡的數值", initial="64", max_value=2560, min_value=-2560)
    long_desc = forms.CharField(max_length=200, widget=forms.Textarea(), label="說明", required=False)
    active = forms.BooleanField(label="開通", help_text="該點數卡是否可用", required=False, initial=True)

class FeedForm(forms.Form):
    player = forms.ModelChoiceField(Player.objects.all(), label="玩家")
