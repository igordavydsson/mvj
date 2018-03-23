from django.contrib.gis import admin

from leasing.models import (
    Comment, Condition, ConditionType, Contact, Contract, ContractChange, ContractType, Decision, DecisionMaker,
    DecisionType, District, Financing, Hitas, IntendedUse, Lease, LeaseArea, LeaseIdentifier, LeaseStateLog, LeaseType,
    Management, MortgageDocument, Municipality, NoticePeriod, PlanUnit, PlanUnitState, PlanUnitType, Plot, Regulation,
    RelatedLease, StatisticalUse, SupportiveHousing, Tenant, TenantContact)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_business', 'is_lessor')
    search_fields = ['first_name', 'last_name', 'business_name']


class MunicipalityAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    readonly_fields = ('id',)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'municipality', 'identifier')
    search_fields = ['name', 'municipality__name', 'identifier']


class TenantContactInline(admin.TabularInline):
    model = TenantContact
    extra = 0


class TenantAdmin(admin.ModelAdmin):
    list_display = ('lease', )
    inlines = [TenantContactInline]


class LeaseAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    list_display = ('lease', 'topic', 'user', 'created_at', 'modified_at')


class ContractChangeInline(admin.StackedInline):
    model = ContractChange
    extra = 0


class MortgageDocumentInline(admin.StackedInline):
    model = MortgageDocument
    extra = 0


class ContractAdmin(admin.ModelAdmin):
    list_display = ('lease', 'type', 'contract_number')
    inlines = [ContractChangeInline, MortgageDocumentInline]


class ConditionInline(admin.StackedInline):
    model = Condition
    extra = 0


class DecisionAdmin(admin.ModelAdmin):
    list_display = ('lease', 'reference_number', 'decision_maker', 'type')
    inlines = [ConditionInline]


class NameAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Financing, NameAdmin)
admin.site.register(Hitas, NameAdmin)
admin.site.register(IntendedUse, NameAdmin)
admin.site.register(Lease, LeaseAdmin)
admin.site.register(LeaseArea)
admin.site.register(LeaseIdentifier)
admin.site.register(LeaseStateLog)
admin.site.register(LeaseType, NameAdmin)
admin.site.register(Management, NameAdmin)
admin.site.register(Municipality, MunicipalityAdmin)
admin.site.register(NoticePeriod)
admin.site.register(Plot)
admin.site.register(PlanUnit)
admin.site.register(PlanUnitState, NameAdmin)
admin.site.register(PlanUnitType, NameAdmin)
admin.site.register(Regulation, NameAdmin)
admin.site.register(RelatedLease)
admin.site.register(StatisticalUse, NameAdmin)
admin.site.register(SupportiveHousing, NameAdmin)
admin.site.register(Tenant, TenantAdmin)
admin.site.register(TenantContact)
admin.site.register(Contract, ContractAdmin)
admin.site.register(ContractType, NameAdmin)
admin.site.register(Decision, DecisionAdmin)
admin.site.register(DecisionType, NameAdmin)
admin.site.register(DecisionMaker, NameAdmin)
admin.site.register(ConditionType, NameAdmin)
