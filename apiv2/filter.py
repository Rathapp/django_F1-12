import django_filters 
from patients.models import patients
class PatientFilter( django_filters.FilterSet ):
    # min_age = django_filters.NumberFilter(field_name='age',   	lookup_expr='gte' )
    # max_age = django_filters.NumberFilter(field_name='age',  	lookup_expr='lte'    )
    firstname_contain = django_filters.CharFilter(field_name='firstName', 	lookup_expr='icontains' )
    lastname_contain = django_filters.CharFilter(field_name='lastName', 	lookup_expr='icontains' )
    class Meta: 
        model = patients
        fields = [  
            'firstName',
            'lastName',
            'Sex',
            'Phone' 
            ]
