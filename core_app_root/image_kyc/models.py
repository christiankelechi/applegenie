from django.db import models

from django.db import models

class UserImageKyc(models.Model):
    user_default_image = models.FileField(upload_to="kyc_images", null=True, blank=True)
    user_real_time_capture = models.FileField(upload_to="kyc_images", null=True, blank=True)

    def save(self, *args, **kwargs):
        # Prevent saving the uploaded files
        self.user_default_image = None
        self.user_real_time_capture = None
        super().save(*args, **kwargs)
    
    def clean(self):
        super().clean()
        max_size = 10 * 1024 * 1024  # 10 MB in bytes

        if self.user_default_image and self.user_default_image.size > max_size:
            raise ValidationError("The file size for user_default_image must be 10 MB or less.")

        if self.user_real_time_capture and self.user_real_time_capture.size > max_size:
            raise ValidationError("The file size for user_real_time_capture must be 10 MB or less.")
    
    def __str__(self):
        return f"{self.user_default_image} compared with {user_real_time_capture} successfully"