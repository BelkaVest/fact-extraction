from django import forms

#форма для ввода анализируемого текста
class UserForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(), label="Результат анализа:")
    ner = forms.BooleanField(label="Разметка распознанных сущностей")
    morph = forms.BooleanField(label="Морфологический анализ")
    syntax = forms.BooleanField(label="Синтаксический анализ")
    seman = forms.IntegerField(label="Номер предложения для семантического анализа")
#форма для вывода результата
class ResultForm(forms.Form):
    result = forms.CharField()