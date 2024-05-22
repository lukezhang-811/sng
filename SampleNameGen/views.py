from django.shortcuts import render, redirect
from .forms import SampleForm
from .models import Sample

def home(request):
    if request.method == "POST":
        form = SampleForm(request.POST)
        if form.is_valid():
            project_name = form.cleaned_data['project_name']
            institution = form.cleaned_data['institution']
            technology = form.cleaned_data['technology']
            storage_type = form.cleaned_data['storage_type']
            tissue_type = form.cleaned_data['tissue_type']
            sample_name = form.cleaned_data['sample_name']
            origin = form.cleaned_data['origin']
            condition = form.cleaned_data['condition']
            replicate = form.cleaned_data['replicate']

            sample_id = '_'.join([project_name, institution, technology, storage_type,
                                  tissue_type, str(sample_name), origin, condition, replicate])

            # Check for duplicates
            if Sample.objects.filter(
                sample_id=sample_id
            ).exists():
                duplicate_message = "A sample with the same ID already exists."
                return render(request, 'submit_form.html', {'form': form, 'duplicate_message': duplicate_message})

            # Save the form and generate the name
            sample = form.save(commit=False)
            sample.sample_id = sample_id
            sample.save()

            return render(request, 'submit_form.html', {'form': form, 'generated_name': sample_id})
    else:
        form = SampleForm()
    
    return render(request, 'submit_form.html', {'form': form})

def sample_ids(request):
    submissions = Sample.objects.values_list('sample_id', flat=True)
    context = {
        'submissions': submissions,
    }
    return render(request, 'sample_id_list.html', context)

def data(request):
    samples = Sample.objects.all()  # Fetch all data from the Submission model
    print(samples)
    return render(request, 'data_table.html', {'samples': samples})