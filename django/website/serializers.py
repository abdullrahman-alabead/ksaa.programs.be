from cgitb import lookup
from dataclasses import field, fields
from multiprocessing import context
from pyexpat import model
from rest_framework import serializers
from .models import *

class ProgramInfoSerializer(serializers.ModelSerializer):
  info_label = serializers.SerializerMethodField()
  info_text = serializers.SerializerMethodField()
  
  class Meta:
    model= ProgramInfo
    fields = "__all__"
  
  def get_info_label(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_info_label
    return obj.english_info_label

  def get_info_text(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_info_text
    return obj.english_info_text


class TargetAudiencesSerializer(serializers.ModelSerializer):
  name = serializers.SerializerMethodField()
  
  class Meta:
    model= TargetAudiences
    fields = "__all__"
  
  def get_name(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_name
    return obj.english_name


class GoalsSerializer(serializers.ModelSerializer):
  goal_text = serializers.SerializerMethodField()
  
  class Meta:
    model= Goals
    fields = "__all__"
  
  def get_goal_text(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_goal_text
    return obj.english_goal_text


class OutputsSerializer(serializers.ModelSerializer):
  output = serializers.SerializerMethodField()
  
  
  class Meta:
    model= Outputs
    fields = "__all__"
  
  def get_output(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_output
    return obj.english_output


class CoursesSerializer(serializers.ModelSerializer):
  title = serializers.SerializerMethodField()
  
  class Meta:
    model= Courses
    fields = "__all__"
  
  def get_title(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_title
    return obj.english_title


class ConditionsSerializer(serializers.ModelSerializer):
  text = serializers.SerializerMethodField()
  
  class Meta:
    model= Conditions
    fields = "__all__"
  
  def get_text(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_text
    return obj.english_text


class FaqsSerializer(serializers.ModelSerializer):
  question = serializers.SerializerMethodField()
  answer = serializers.SerializerMethodField()
  
  class Meta:
    model= Faqs
    fields = "__all__"
  
  def get_question(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_question
    return obj.english_question

  def get_answer(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_answer
    return obj.english_answer



class HomepageSerializer(serializers.ModelSerializer):
  landing_headline = serializers.SerializerMethodField()
  landing_subheadline = serializers.SerializerMethodField()
  ready_text = serializers.SerializerMethodField()
  register_button_text = serializers.SerializerMethodField()
  target_audience_headline = serializers.SerializerMethodField()
  target_audience_text = serializers.SerializerMethodField()
  goals_headline = serializers.SerializerMethodField()
  outputs_headline = serializers.SerializerMethodField()
  courses_headline = serializers.SerializerMethodField()
  jobs_headline = serializers.SerializerMethodField()
  jobs_text = serializers.SerializerMethodField()
  conditions_headline = serializers.SerializerMethodField()
  faq_headline = serializers.SerializerMethodField()
  program_info = ProgramInfoSerializer(many=True)
  target_audiences = TargetAudiencesSerializer(many=True)
  goals = GoalsSerializer(many=True)
  outputs = OutputsSerializer(many=True)
  courses = CoursesSerializer(many=True)
  conditions = ConditionsSerializer(many=True)
  faqs = FaqsSerializer(many=True)
  
  
  
  class Meta:
    model= Homepage
    fields = "__all__"
  
  def get_landing_headline(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_landing_headline
    return obj.english_landing_headline

  def get_landing_subheadline(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_landing_subheadline
    return obj.english_landing_subheadline

  def get_ready_text(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_ready_text
    return obj.english_ready_text

  def get_register_button_text(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_register_button_text
    return obj.english_register_button_text

  def get_target_audience_headline(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_target_audience_headline
    return obj.english_target_audience_headline

  def get_target_audience_text(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_target_audience_text
    return obj.english_target_audience_text

  def get_goals_headline(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_goals_headline
    return obj.english_goals_headline

  def get_outputs_headline(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_outputs_headline
    return obj.english_outputs_headline

  def get_courses_headline(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_courses_headline
    return obj.english_courses_headline

  def get_jobs_headline(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_jobs_headline
    return obj.english_jobs_headline

  def get_jobs_text(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_jobs_text
    return obj.english_jobs_text

  def get_conditions_headline(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_conditions_headline
    return obj.english_conditions_headline

  def get_faq_headline(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_faq_headline
    return obj.english_faq_headline

















class FormPageSerializer(serializers.ModelSerializer):
  landing_headline = serializers.SerializerMethodField()
  landing_subheadline = serializers.SerializerMethodField()
  intro_text = serializers.SerializerMethodField()
  submit_button = serializers.SerializerMethodField()
  in_progress_text = serializers.SerializerMethodField()
  success_text = serializers.SerializerMethodField()
  failed_text = serializers.SerializerMethodField()

  
  class Meta:
    model= FormPage
    fields = "__all__"
  
  def get_landing_headline(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_landing_headline
    return obj.english_landing_headline

  def get_landing_subheadline(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_landing_subheadline
    return obj.english_landing_subheadline

  def get_intro_text(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_intro_text
    return obj.english_intro_text

  def get_submit_button(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_submit_button
    return obj.english_submit_button

  def get_in_progress_text(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_in_progress_text
    return obj.english_in_progress_text

  def get_success_text(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_success_text
    return obj.english_success_text

  def get_failed_text(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_failed_text
    return obj.english_failed_text



class FormFieldsSerializer(serializers.ModelSerializer):
  input_label = serializers.SerializerMethodField()
  
  class Meta:
    model= FormFields
    fields = "__all__"
  
  def get_input_label(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_input_label
    return obj.english_input_label


class FormSectionsSerializer(serializers.ModelSerializer):
  headline = serializers.SerializerMethodField()
  note = serializers.SerializerMethodField()
  form_fields = FormFieldsSerializer(many=True)
  
  class Meta:
    model= FormSections
    fields = "__all__"
  
  def get_headline(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_headline
    return obj.english_headline
  def get_note(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_note
    return obj.english_note




class RegisteredSerializer(serializers.ModelSerializer):
  
  class Meta:
    model= Registered
    fields = "__all__"
  



class HeaderLinkSerializer(serializers.ModelSerializer):
  text = serializers.SerializerMethodField()
  
  
  
  class Meta:
    model= HeaderLink
    fields = "__all__"
    
  def get_text(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_text
    return obj.english_text


class HeaderFooterSerializer(serializers.ModelSerializer):
  footer_license = serializers.SerializerMethodField()
  header_links = HeaderLinkSerializer(many=True)
  
  
  class Meta:
    model= HeaderFooter
    fields = "__all__"
    
  def get_footer_license(self, obj):
    if self.context['request'].headers.get('Accept-Language') == 'ar':
      return obj.arabic_footer_license
    return obj.english_footer_license