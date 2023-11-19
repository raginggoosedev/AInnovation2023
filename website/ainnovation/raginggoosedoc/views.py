from django.shortcuts import render
from .forms import UserInputForm
from .models import RagingGooseDoc  # Import your model


def user_input_view(request):
    page = RagingGooseDoc.objects.first()  # Fetch the specific page, you might need to adjust the logic here
    initial_data = {'name': page.name, 'problem': page.problem}
    form = UserInputForm(initial=initial_data)  # Use the UserInputForm with initial data

    return render(request, 'raging_goose_doc.html', {'page': page, 'form': form})
