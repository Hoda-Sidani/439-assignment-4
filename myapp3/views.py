from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

# CREATE
def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'myapp3/contact_form.html', {'form': form})


# READ (list all contacts)
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'myapp3/contact_list.html', {'contacts': contacts})


# UPDATE
def update_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'myapp3/contact_form.html', {'form': form})


# DELETE
def delete_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'myapp3/contact_confirm_delete.html', {'contact': contact})


from django.db.models import Q

from django.shortcuts import render

def recommend_doctors(request):
    query = request.GET.get('query', '').lower().strip()  # Get the query from the GET request
    filtered_doctors = Contact.objects.all()  # Start with all doctors
    # Gender filter
    if 'female' in query:
        filtered_doctors = filtered_doctors.filter(gender__iexact='Female')
    elif 'male' in query:
        filtered_doctors = filtered_doctors.filter(gender__iexact='Male')
    #Specialty filter
    specialties = [
        'oncologic', 'neurosurgeon', 'orthopedic', 'urologic',
        'pediatric', 'general', 'cardiothoracic', 'vascular',
        'plastic'
    ]
    # Hospital filter
    hospitals = [
        'aley medical center', 'notre dame de secours', 'hammoud hospital', 
        'dar el amal', 'general hospital', 'najjar', 'aubmc', 'mount lebanon',
        'al najda', 'saint georges', 'al zahraa', 'rafic hariri', 'cmc'
    ]
    for hospital in hospitals:
        if hospital in query:
            filtered_doctors = filtered_doctors.filter(hospital__icontains=hospital)
            break
    for specialty in specialties:
        if specialty in query:
            filtered_doctors = filtered_doctors.filter(speciality__icontains=specialty)
            break
   # Address filter
    addresses = [
        'aley', 'byblos', 'baalbek', 'tripoli', 'sidon', 'beirut', 
        'jounieh', 'nabatieh', 'zahle', 'tyre'
    ]
    for address in addresses:
        if address in query:
            filtered_doctors = filtered_doctors.filter(address__icontains=address)
            break

    def parse_condition(condition):
        """
        Parses a single condition and returns a Q object.
        """
        condition = condition.strip()
        try:
                        
            # Recommendation Condition
            if 'recommendation' in condition:
                if 'above' in condition:
                    value = int(condition.split('above')[1].strip().split()[0])
                    return Q(recommendation__gt=value)
                elif 'at least' in condition:
                    value = int(condition.split('at least')[1].strip().split()[0])
                    return Q(recommendation__gte=value)
                elif 'below' in condition:
                    value = int(condition.split('below')[1].strip().split()[0])
                    return Q(recommendation__lt=value)
                else:
                    value = int(condition.split('recommendation')[1].strip().split()[0])
                    return Q(recommendation=value)

            # Experience Condition
            elif 'experience' in condition:
                if 'above' in condition:
                    value = int(condition.split('above')[1].strip().split()[0])
                    return Q(experience__gt=value)
                elif 'at least' in condition:
                    value = int(condition.split('at least')[1].strip().split()[0])
                    return Q(experience__gte=value)
                elif 'below' in condition:
                    value = int(condition.split('below')[1].strip().split()[0])
                    return Q(experience__lt=value)
                else:
                    value = int(condition.split('experience')[1].strip().split()[0])
                    return Q(experience=value)

            # Fees Condition
            elif 'fees' in condition:
                if 'above' in condition:
                    value = int(condition.split('above')[1].strip().split()[0])
                    return Q(fees__gt=value)
                elif 'at least' in condition:
                    value = int(condition.split('at least')[1].strip().split()[0])
                    return Q(fees__gte=value)
                elif 'below' in condition:
                    value = int(condition.split('below')[1].strip().split()[0])
                    return Q(fees__lt=value)
                else:
                    value = int(condition.split('fees')[1].strip().split()[0])
                    return Q(fees=value)

            # Speciality Condition
            elif 'speciality' in condition:
                speciality_value = condition.split('speciality')[1].strip()
                return Q(speciality__icontains=speciality_value)

            # Hospital Condition
            elif 'hospital' in condition:
                hospital_value = condition.split('hospital')[1].strip()
                return Q(hospital__icontains=hospital_value)

        except (ValueError, IndexError):
            return Q()  # Return an empty filter if the condition is invalid

        # Add other conditions as necessary
        return Q()

    # Handle the complex logic explicitly
    overall_filter = Q()  # Initialize the overall Q object
    and_parts = query.split(' and ')
    for part in and_parts:
        if ' or ' in part:
            # Handle OR conditions within the AND part
            or_conditions = part.split(' or ')
            or_filter = Q()  # Initialize Q for OR conditions
            for or_condition in or_conditions:
                or_filter |= parse_condition(or_condition)
            overall_filter &= or_filter
        else:
            # Handle simple AND condition
            overall_filter &= parse_condition(part)

    # Apply the final filter
    filtered_doctors = filtered_doctors.filter(overall_filter)

    return render(request, 'myapp3/contact_list.html', {'contacts': filtered_doctors})