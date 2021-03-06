from django_filters.rest_framework import FilterSet, filters

from leasing.models import CollectionCourtDecision, CollectionLetter, CollectionNote
from leasing.models.invoice import InvoiceRow, InvoiceSet

from .models import Comment, Contact, Decision, District, Index, Invoice, Lease


class CollectionCourtDecisionFilter(FilterSet):
    lease = filters.NumberFilter()

    class Meta:
        model = CollectionCourtDecision
        fields = ['lease']


class CollectionLetterFilter(FilterSet):
    lease = filters.NumberFilter()

    class Meta:
        model = CollectionLetter
        fields = ['lease']


class CollectionNoteFilter(FilterSet):
    lease = filters.NumberFilter()

    class Meta:
        model = CollectionNote
        fields = ['lease', 'user']


class CommentFilter(FilterSet):
    lease = filters.NumberFilter()

    class Meta:
        model = Comment
        fields = ['lease', 'user', 'topic']


class ContactFilter(FilterSet):
    class Meta:
        model = Contact
        fields = ['type', 'first_name', 'last_name', 'name', 'business_id', 'national_identification_number',
                  'customer_number', 'sap_customer_number', 'partner_code', 'is_lessor']


class DecisionFilter(FilterSet):
    lease = filters.NumberFilter()

    class Meta:
        model = Decision
        fields = ['lease', 'reference_number', 'decision_maker', 'decision_date', 'type']


class DistrictFilter(FilterSet):
    class Meta:
        model = District
        fields = ['municipality', 'identifier']


class IndexFilter(FilterSet):
    class Meta:
        model = Index
        fields = ['year', 'month']


class InvoiceFilter(FilterSet):
    lease = filters.NumberFilter()

    class Meta:
        model = Invoice
        fields = ['lease', 'state', 'type']


class InvoiceSetFilter(FilterSet):
    lease = filters.NumberFilter()

    class Meta:
        model = InvoiceSet
        fields = ['lease']


class InvoiceRowFilter(FilterSet):
    invoice = filters.NumberFilter()

    class Meta:
        model = InvoiceRow
        fields = ['invoice']


class LeaseFilter(FilterSet):
    class Meta:
        model = Lease
        fields = ['type', 'municipality', 'district']
