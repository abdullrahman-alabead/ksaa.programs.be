from django.db import models
from .utils import validate_image_and_svg_file_extension, validate_video_file_extension
from ckeditor.fields import RichTextField

# Create your models here.
# RichTextField(default='', config_name='awesome_ckeditor')
# models.CharField(max_length=200, default='', blank=True, null=True)
# models.ImageField(upload_to="Website")
# supplier_image = models.FileField(upload_to="image", validators=[validate_image_and_svg_file_extension,])



class Homepage(models.Model):
  english_landing_headline = models.CharField(max_length=200, default="", null= True, blank=True)
  arabic_landing_headline = models.CharField(max_length=200, default="", null= True, blank=True)
  english_landing_subheadline = models.CharField(max_length=200, default="", null= True, blank=True)
  arabic_landing_subheadline = models.CharField(max_length=200, default="", null= True, blank=True)
  english_ready_text = models.CharField(max_length=200, default="", null= True, blank=True)
  arabic_ready_text = models.CharField(max_length=200, default="", null= True, blank=True)
  register_button_url = models.CharField(max_length=200, default="", null= True, blank=True)
  english_register_button_text = models.CharField(max_length=200, default="", null= True, blank=True)
  arabic_register_button_text = models.CharField(max_length=200, default="", null= True, blank=True)
  landing_background = models.FileField(upload_to="images")

  english_target_audience_headline = models.CharField(max_length=200, default="", null= True, blank=True)
  arabic_target_audience_headline = models.CharField(max_length=200, default="", null= True, blank=True)
  english_target_audience_text = RichTextField(default="", config_name="awesome_ckeditor")
  arabic_target_audience_text = RichTextField(default="", config_name="awesome_ckeditor")

  english_goals_headline = models.CharField(max_length=200, default="", null= True, blank=True)
  arabic_goals_headline = models.CharField(max_length=200, default="", null= True, blank=True)

  english_outputs_headline = models.CharField(max_length=200, default="", null= True, blank=True)
  arabic_outputs_headline = models.CharField(max_length=200, default="", null= True, blank=True)
  outputs_image = models.FileField(upload_to="images")

  english_courses_headline = models.CharField(max_length=200, default="", null= True, blank=True)
  arabic_courses_headline = models.CharField(max_length=200, default="", null= True, blank=True)

  english_jobs_headline = models.CharField(max_length=200, default="", null= True, blank=True)
  arabic_jobs_headline = models.CharField(max_length=200, default="", null= True, blank=True)
  english_jobs_text = RichTextField(default="", config_name="awesome_ckeditor")
  arabic_jobs_text = RichTextField(default="", config_name="awesome_ckeditor")
  jobs_image = models.FileField(upload_to="images")
  english_conditions_headline = models.CharField(max_length=200, default="", null= True, blank=True)
  arabic_conditions_headline = models.CharField(max_length=200, default="", null= True, blank=True)

  arabic_faq_headline = models.CharField(max_length=200, default="", null= True, blank=True)
  english_faq_headline = models.CharField(max_length=200, default="", null= True, blank=True)





class ProgramInfo(models.Model):
  icon = models.FileField(upload_to="images")
  arabic_info_label = models.CharField(max_length=200, default="", null= True, blank=True)
  english_info_label = models.CharField(max_length=200, default="", null= True, blank=True)
  arabic_info_text = models.CharField(max_length=200, default="", null= True, blank=True)
  english_info_text = models.CharField(max_length=200, default="", null= True, blank=True)
  homepage = models.ForeignKey(to=Homepage, on_delete=models.CASCADE, related_name="program_info")


class TargetAudiences(models.Model):
  english_name = models.CharField(max_length=200, default="", null= True, blank=True)
  arabic_name = models.CharField(max_length=200, default="", null= True, blank=True)
  homepage = models.ForeignKey(to=Homepage, on_delete=models.CASCADE, related_name="target_audiences")


class Goals(models.Model):
  icon = models.FileField(upload_to="images")
  english_goal_text = RichTextField(default="", config_name="awesome_ckeditor")
  arabic_goal_text = RichTextField(default="", config_name="awesome_ckeditor")
  homepage = models.ForeignKey(to=Homepage, on_delete=models.CASCADE, related_name="goals")


class Outputs(models.Model):
  english_output = models.CharField(max_length=200, default="", null= True, blank=True)
  arabic_output = models.CharField(max_length=200, default="", null= True, blank=True)
  homepage = models.ForeignKey(to=Homepage, on_delete=models.CASCADE, related_name="outputs")


class Courses(models.Model):
  english_title = models.CharField(max_length=200, default="", null= True, blank=True)
  arabic_title = models.CharField(max_length=200, default="", null= True, blank=True)
  homepage = models.ForeignKey(to=Homepage, on_delete=models.CASCADE, related_name="courses")


class Conditions(models.Model):
  icon = models.FileField(upload_to="images")
  english_text = RichTextField(default="", config_name="awesome_ckeditor")
  arabic_text = RichTextField(default="", config_name="awesome_ckeditor")
  homepage = models.ForeignKey(to=Homepage, on_delete=models.CASCADE, related_name="conditions")


class Faqs(models.Model):
  english_question = RichTextField(default="", config_name="awesome_ckeditor")
  arabic_question = RichTextField(default="", config_name="awesome_ckeditor")
  english_answer = RichTextField(default="", config_name="awesome_ckeditor")
  arabic_answer = RichTextField(default="", config_name="awesome_ckeditor")
  homepage = models.ForeignKey(to=Homepage, on_delete=models.CASCADE, related_name="faqs")





# Form Page

class FormPage(models.Model):
  english_landing_headline = models.CharField(max_length=200, default="", null= True, blank=True)
  arabic_landing_subheadline = models.CharField(max_length=200, default="", null= True, blank=True)
  english_landing_subheadline = models.CharField(max_length=200, default="", null= True, blank=True)
  arabic_landing_headline = models.CharField(max_length=200, default="", null= True, blank=True)
  english_intro_text = RichTextField(default="", config_name="awesome_ckeditor")
  arabic_intro_text = RichTextField(default="", config_name="awesome_ckeditor")
  landing_cover_image = models.FileField(upload_to="images")

  english_submit_button = models.CharField(max_length=200, default="", null= True, blank=True)
  arabic_submit_button = models.CharField(max_length=200, default="", null= True, blank=True)
  english_in_progress_text = models.CharField(max_length=200, default="", null= True, blank=True)
  arabic_in_progress_text = models.CharField(max_length=200, default="", null= True, blank=True)
  english_success_text = models.CharField(max_length=200, default="", null= True, blank=True)
  arabic_success_text = models.CharField(max_length=200, default="", null= True, blank=True)
  english_failed_text = models.CharField(max_length=200, default="", null= True, blank=True)
  arabic_failed_text = models.CharField(max_length=200, default="", null= True, blank=True)


class FormSections(models.Model):
  english_headline = models.CharField(max_length=200, default="", null= True, blank=True)
  arabic_headline = models.CharField(max_length=200, default="", null= True, blank=True)


class FormFields(models.Model):
  english_input_label = models.CharField(max_length=200, default="", null= True, blank=True)
  arabic_input_label = models.CharField(max_length=200, default="", null= True, blank=True)
  sanity_name = models.CharField(max_length=200, default="", null= True, blank=True, editable=False)
  input_type = models.CharField(max_length=200, default="", null= True, blank=True)
  choices = models.CharField(max_length=200, default="", null= True, blank=True)
  form_section = models.ForeignKey(to=FormSections, on_delete=models.CASCADE, related_name="form_fields")


class Registered(models.Model):
  training_officer_name = models.CharField(max_length=200, default="", null= True, blank=True)
  training_officer_job = models.CharField(max_length=200, default="", null= True, blank=True)
  training_officer_phone_number = models.CharField(max_length=200, default="", null= True, blank=True)
  candidate_name = models.CharField(max_length=200, default="", null= True, blank=True)
  candidate_sex = models.CharField(max_length=200, default="", null= True, blank=True)
  candidate_civil_registry = models.CharField(max_length=200, default="", null= True, blank=True)
  candidate_birth_date = models.CharField(max_length=200, default="", null= True, blank=True)
  candidate_qualification = models.CharField(max_length=200, default="", null= True, blank=True)
  candidate_qualification_title = models.CharField(max_length=200, default="", null= True, blank=True)
  candidate_graduation_year = models.CharField(max_length=200, default="", null= True, blank=True)
  candidate_job_title = models.CharField(max_length=200, default="", null= True, blank=True)
  candidate_email_address = models.CharField(max_length=200, default="", null= True, blank=True)
  candidate_phone_number = models.CharField(max_length=200, default="", null= True, blank=True)
  candidate_nomination_letter = models.FileField(upload_to="images", null= True, blank=True)
  candidate_bachelor_document = models.FileField(upload_to="images", null= True, blank=True)



class HeaderFooter(models.Model):
  english_footer_license = models.CharField(max_length=200, default="", null= True, blank=True)
  arabic_footer_license = models.CharField(max_length=200, default="", null= True, blank=True)


class HeaderLink(models.Model):
  link = models.CharField(max_length=200, default="", null= True, blank=True)
  arabic_text = models.CharField(max_length=200, default="", null= True, blank=True)
  english_text = models.CharField(max_length=200, default="", null= True, blank=True)
  header_footer = models.ForeignKey(to=HeaderFooter, on_delete=models.CASCADE, related_name="header_links")