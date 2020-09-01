import csv, io, datetime
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import Dataset, Column

import lib.datastats as datastats
# Create your views here.
@login_required()
def summary(request):
    if request.method == 'POST':
        #DEBUG
        messages.info(request, 'in upload_csv')
        try:
            csv_file = request.FILES['csv_file']
            dfData = datastats.process_csv(csv_file)
            #DEBUG
            messages.info(request, 'after csv file try'+str(csv_file.name))
            
            #Drop the index so the Column Name field is populated
            dfData = dfData.reset_index()
            dfData = dfData.rename(columns={
                'Col_Name':'column_name',
                'Type':'column_type',
                'Num_Blank':'num_blank',
                'Num_Unique':'num_unique',
                'Variability':'variability',
                'count':'num_count',
                'mean':'num_mean',
                'std':'num_std',
                'min':'num_min',
                '25%':'pct_25',
                '50%':'pct_50',
                '75%':'pct_75',
                'max':'num_max'})
            
            #DEBUG
            messages.info(request, 'after data rename')
            
            #Get the description entered by th user in the form
            description = str(request.POST.get('file_description'))
            
            #DEBUG
            messages.info(request, 'set description ='+description)
            
            #Create the new dataset row in the database
            new_dataset = Dataset(file_name=str(csv_file), description=description, load_date=datetime.datetime.now())
            new_dataset.save()
            
            #Get the current dataset id as the foreign key to insert inot the Column table
            dataset_id = new_dataset.id
            #Include that dataset id as the dataset id field value for all rows
            dfData['dataset_id'] = dataset_id
            
            #DEBUG
            #dfData.to_csv('out.csv')
            #DEBUG
            messages.info(request, 'after save dataset')
            
            #Convert the df to a dict so it can be inserted into the database
            dictColumns = dfData.apply(lambda x : x.dropna().to_dict(),axis=1)
            #Loop through the dictionary and insert each row
            for item in dictColumns:
                col_to_add = Column(**item)
                col_to_add.save()
                
            #DEBUG
            messages.info(request, 'after save')
        except Exception as e:
            messages.error(request, "Unable to upload file. "+repr(e))
            
    latest_dataset_list = Dataset.objects.order_by('-load_date')[:5]
    context = {'latest_dataset_list':latest_dataset_list}
    return render(request, 'datastats/index.html', context)
    
def dataset(request, dataset_id):
    dataset = get_object_or_404(Dataset, pk=dataset_id)
    return render(request, 'datastats/dataset.html', {'dataset': dataset})