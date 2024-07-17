import json
import os
from django.conf import settings

def loadChoices(filename):
    app_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(app_dir, 'choices', f'{filename}.json')
    with open(file_path, 'r') as f:
        return json.load(f)
    
def getAllChoices():
    return {
        'PROJECT_CHOICES': loadChoices('project_choices'),
        'INSTITUTION_CHOICES': loadChoices('institution_choices'),
        'TECHNOLOGY_CHOICES': loadChoices('technology_choices'),
        'STORAGE_TYPE_CHOICES': loadChoices('storage_type_choices'),
        'TISSUE_TYPE_CHOICES': loadChoices('tissue_type_choices'),
        'ORIGIN_CHOICES': loadChoices('origin_choices'),
        'CONDITION_CHOICES': loadChoices('condition_choices')
    }