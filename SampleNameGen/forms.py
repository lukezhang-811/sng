from django import forms
from .models import Sample

# Define choices for the dropdown fields
PROJECT_CHOICES = [
    ('', 'Select Project'),
    ('TOUCHSTONE', 'Touchstone'),
    # Add more as needed
]

INSTITUTION_CHOICES = [
    ('', 'Select Institution/Department'),
    ('STJ', 'STJ - St Jude'),
    ('UOA', 'UOA - Universitiy of Adelaide'),
    ('WCM', 'WCM - Weill Cornell Medicine'),
    ('DNB', 'DNB - St Jude Developmental Neurobiology'),
    # Add more institutions as needed
]

TECHNOLOGY_CHOICES = [
    ('', 'Select Technology'),
    ('XR', 'Xenium'),
    ('CR', 'CosMx RNA'),
    # Add more technologies as needed
]

STORAGE_TYPE_CHOICES = [
    ('', 'Select Storage Type'),
    ('FFPE', 'FFPE'),
    ('FF', 'FF'),
    # Add more storage types as needed
]

TISSUE_TYPE_CHOICES = [
    ('', 'Select Tissue Type'),
    ('BR', 'Breast'),
    ('AP', 'Appendix'),
    ('CO', 'Colon'),
    ('BA', 'Brain'),
    ('PA', 'Pancreas'),
    ('PR', 'Prostate'),
    # Add more tissue types as needed
]

ORIGIN_CHOICES = [
    ('', 'Select Institution'),
    ('STJ', 'STJ - St Jude'),
    ('UOA', 'UOA - Universitiy of Adelaide'),
    ('WCM', 'WCM - Weill Cornell Medicine'),
    # Add more origins as needed
]

CONDITION_CHOICES = [
    ('', 'Select Condition'),
    ('N', 'Normal'),
    ('C', 'Cancer'),
    ('D', 'Non-cancer Disease'),
    # Add more conditions as needed
]

class SampleForm(forms.ModelForm):
    project_name = forms.ChoiceField(
        choices=PROJECT_CHOICES,
        label="Project Name",
        widget=forms.Select(attrs={'placeholder': 'Select Project'})
    )
    institution = forms.ChoiceField(
        choices=INSTITUTION_CHOICES,
        label="Institution/Department",
        widget=forms.Select(attrs={'placeholder': 'Select Institution/Department'})
    )
    technology = forms.ChoiceField(
        choices=TECHNOLOGY_CHOICES,
        label="Technology",
        widget=forms.Select(attrs={'placeholder': 'Select Technology'})
    )
    storage_type = forms.ChoiceField(
        choices=STORAGE_TYPE_CHOICES,
        label="Storage Type",
        widget=forms.Select(attrs={'placeholder': 'Select Storage Type'})
    )
    tissue_type = forms.ChoiceField(
        choices=TISSUE_TYPE_CHOICES,
        label="Tissue Type",
        widget=forms.Select(attrs={'placeholder': 'Select Tissue Type'})
    )
    origin = forms.ChoiceField(
        choices=ORIGIN_CHOICES,
        label="Origin",
        widget=forms.Select(attrs={'placeholder': 'Select Origin'})
    )
    condition = forms.ChoiceField(
        choices=CONDITION_CHOICES,
        label="Condition",
        widget=forms.Select(attrs={'placeholder': 'Select Condition'})
    )
    sample_name = forms.IntegerField(
        label="Sample Number",
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Sample Number'})
    )
    replicate = forms.IntegerField(
        label="Replicate Number",
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Replicate Number'})
    )

    class Meta:
        model = Sample
        fields = [
            'project_name', 'institution', 'technology', 'storage_type', 'tissue_type', 
            'sample_name', 'origin', 'condition', 'replicate'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})