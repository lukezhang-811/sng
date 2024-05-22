from django import forms
from .models import Sample

class SampleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.populate_choices()

    def populate_choices(self):
        for field_name, field in self.fields.items():
            if field_name != 'sample_id':
                print(f"Field Name: {field_name}, Field Type: {type(field)}")
                if isinstance(field, forms.ChoiceField):
                    choices = Sample.objects.order_by(field_name).values_list(field_name, flat=True).distinct()
                    choices = [(choice, choice) for choice in choices]
                    choices.insert(0, ('', 'Custom'))
                    field.choices = choices

    class Meta:
        model = Sample
        fields = [
            'project_name', 'institution', 'technology', 'storage_type', 
            'tissue_type', 'sample_name', 'origin', 'condition', 'replicate'
        ]
