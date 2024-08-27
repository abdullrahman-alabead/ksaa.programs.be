from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
from django.core.validators import (
  get_available_image_extensions,
  FileExtensionValidator  
)



# @deconstructible
# class VideoValidator:
#     error_messages = {
#         'invalid_video': _("The uploaded file is not a video."),
#     }

#     def __call__(self, value):
#         # Check if the file has a video MIME type
#         mime_type = magic.from_buffer(value.read(), mime=True)
#         if not mime_type.startswith('video/'):
#             raise ValidationError(self.error_messages['invalid_video'])

#     def __eq__(self, other):
#         return isinstance(other, self.__class__)

#     def __hash__(self):
#         return hash(self.__class__)



def validate_image_and_svg_file_extension(value) :
  allowed_extensions = get_available_image_extensions() + ["svg"]
  return FileExtensionValidator(allowed_extensions=allowed_extensions)(value)


def validate_video_file_extension(value) :
  allowed_extensions = allowed_extensions=['MOV','avi','mp4','webm','mkv']
  return FileExtensionValidator(allowed_extensions=allowed_extensions)(value)
