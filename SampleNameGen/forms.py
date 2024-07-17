from django import forms
from .models import Sample
from django.forms import DateInput
from .utils import getAllChoices

class SampleForm(forms.ModelForm):
    project_name = forms.ChoiceField(
        label="Project Name",
        widget=forms.Select(attrs={'placeholder': 'Select Project'})
    )
    institution = forms.ChoiceField(
        label="Institution/Department",
        widget=forms.Select(attrs={'placeholder': 'Select Institution/Department'})
    )
    technology = forms.ChoiceField(
        label="Technology",
        widget=forms.Select(attrs={'placeholder': 'Select Technology'})
    )
    storage_type = forms.ChoiceField(
        label="Storage Type",
        widget=forms.Select(attrs={'placeholder': 'Select Storage Type'})
    )
    tissue_type = forms.ChoiceField(
        label="Tissue Type",
        widget=forms.Select(attrs={'placeholder': 'Select Tissue Type'})
    )
    origin = forms.ChoiceField(
        label="Origin",
        widget=forms.Select(attrs={'placeholder': 'Select Origin'})
    )
    condition = forms.ChoiceField(
        label="Condition",
        widget=forms.Select(attrs={'placeholder': 'Select Condition'})
    )
    sample_name = forms.CharField(
        label="Sample Identifier",
        max_length=50,  # Adjust this value as needed
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Sample Identifier String',
            'class': 'form-control'
        })
    )
    replicate = forms.IntegerField(
        label="Replicate Number",
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Replicate Number'})
    )
    date = forms.DateField(
        label="Date",
        widget=DateInput(attrs={'type': 'date', 'placeholder': 'Select Date'})
    )
    description = forms.CharField(
        label="Description",
        widget=forms.Textarea(attrs={'placeholder': 'Enter Description', 'rows': 3})
    )

    class Meta:
        model = Sample
        fields = [
            'project_name', 'institution', 'technology', 'storage_type', 'tissue_type', 
            'sample_name', 'origin', 'condition', 'replicate', 'date', 'description'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Load choices dynamically
        choices = getAllChoices()
        
        # Set choices for each field
        self.fields['project_name'].choices = choices['PROJECT_CHOICES']
        self.fields['institution'].choices = choices['INSTITUTION_CHOICES']
        self.fields['technology'].choices = choices['TECHNOLOGY_CHOICES']
        self.fields['storage_type'].choices = choices['STORAGE_TYPE_CHOICES']
        self.fields['tissue_type'].choices = choices['TISSUE_TYPE_CHOICES']
        self.fields['origin'].choices = choices['ORIGIN_CHOICES']
        self.fields['condition'].choices = choices['CONDITION_CHOICES']

        # Add 'form-control' class to all fields
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

# class ChoicesForm(forms.ModelForm):
#    print('')