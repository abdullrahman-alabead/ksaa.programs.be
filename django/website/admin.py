from django.contrib import admin
from .models import *




class ProgramInfoInline(admin.TabularInline):
    model= ProgramInfo

class TargetAudiencesInline(admin.TabularInline):
    model= TargetAudiences

class GoalsInline(admin.TabularInline):
    model= Goals

class OutputsInline(admin.TabularInline):
    model= Outputs

class CoursesInline(admin.TabularInline):
    model= Courses

class ConditionsInline(admin.TabularInline):
    model= Conditions

class FaqsInline(admin.TabularInline):
    model= Faqs
    

class FormFieldsInline(admin.TabularInline):
    model= FormFields
    
class HeaderLinkInline(admin.TabularInline):
    model= HeaderLink




@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):
  list_display = ['english_landing_headline']
  inlines= [
    ProgramInfoInline,
    TargetAudiencesInline,
    GoalsInline,
    OutputsInline,
    CoursesInline,
    ConditionsInline,
    FaqsInline,
  ]


@admin.register(FormPage)
class FormPageAdmin(admin.ModelAdmin):
  list_display = ['english_landing_headline']


@admin.register(HeaderFooter)
class HeaderFooterAdmin(admin.ModelAdmin):
  list_display = ['arabic_footer_license']
  inlines= [HeaderLinkInline]



@admin.register(FormSections)
class FormSectionsAdmin(admin.ModelAdmin):
  list_display = ['english_headline']
  inlines= [
      FormFieldsInline
  ]


@admin.register(Registered)
class RegisteredAdmin(admin.ModelAdmin):
  list_display = ['training_officer_name']
