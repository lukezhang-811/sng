from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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
                                  tissue_type, str(sample_name), origin, condition, ('R'+str(replicate))])

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

def data(request):
    samples = Sample.objects.all()  # Fetch all data from the Submission model
    print(samples)
    return render(request, 'data_table.html', {'samples': samples})

def delete(request):
    if request.method == 'POST':
        sample_id = request.POST.get('sample_id')
        try:
            sample = get_object_or_404(Sample, sample_id=sample_id)
            sample.delete()
            messages.success(request, f'Sample with ID {sample_id} has been deleted successfully.')
        except Sample.DoesNotExist:
            messages.error(request, f'Sample with ID {sample_id} does not exist.')
        return redirect('delete')  # Make sure this matches your URL name
    return render(request, 'delete_sample.html')