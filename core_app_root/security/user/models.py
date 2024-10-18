from django.db import models

# Create your models here.
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# from django.
import uuid
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.
import hashlib
from django.contrib.postgres.fields import ArrayField


# from core_app_root.apple_gifting.models import AppleModel

class UserManager(BaseUserManager):
    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404

    def create_user(self, email, password=None, **kwargs):
        """Create and return a `User` with an email, phone number, username and password."""
        # if username is None:
        #     raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')
        
        if password is None:
            raise TypeError('User must have an email.')

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **kwargs):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have an email.')
        # if username is None:
        #     raise TypeError('Superusers must have an username.')

        user = self.create_user(email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    public_id = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
    username = models.CharField(db_index=True, max_length=255, unique=True,blank=True,null=True)
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    # country = CountryField(blank=False,null=True)
    country=models.CharField(max_length=1000,null=True,blank=True)
    # phone_number=models.CharField(max_length=300,blank=True,null=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)  # Add this line
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    confirm_password=models.CharField(max_length=1000,null=True,blank=True)
    phone_number=models.CharField(max_length=1000,null=True,blank=True)
    # confirm_password=hashlib.sha256(str(confirm_password).encode()).hexdigest()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    face_encoding = models.BinaryField(blank=True, null=True)
    objects = UserManager()
   
    def __str__(self):
        return f"{self.email}"
    def save(self, *args, **kwargs):
        
        if self.confirm_password:
            self.confirm_password = hashlib.sha256(str(self.confirm_password).encode()).hexdigest()
        super().save(*args, **kwargs)
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    # def __str__(self):
    #     return str(self.full_name)


# class Image(models.Model):
#     file_title=models.CharField(max_length=2000,)
#     image = models.FileField(upload_to='images/')  # or ImageField

class PhoneNumbersModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_phone_numbers',blank=True,null=True)
    phone=models.CharField(blank=True,null=True)
    code=models.CharField(blank=True,null=True)
    
    
from django.db import models

# Create your models here.
class AppleGiftingModel(models.Model):
    number_of_apples=models.IntegerField(blank=True,null=True)
    sender=models.EmailField(blank=True,null=True)

    reciever=models.EmailField(blank=True,null=True)
    reciever_accepts=models.BooleanField(default=False,null=True,blank=True)
    reciever_rejects=models.BooleanField(default=False,null=True,blank=True)


    def __str__(self):
        return f"{self.sender} sent total of {self.number_of_apples} apples to {self.reciever}"

class AppleRecievedNotificationDashboard(models.Model):
    amount_sent=models.IntegerField(default=0,null=True,blank=True)
    receiver_email=models.EmailField(null=True,blank=True)
    sender_email=models.EmailField(null=True,blank=True)
    days_left=models.TextField(null=True,blank=True)
    apple_message_alert=models.TextField(null=True,blank=True)
    location_of_the_gifter=models.TextField(null=True,blank=True)
    interests_of_the_sender=models.TextField(null=True,blank=True)
    education_level_of_sender=models.TextField(null=True,blank=True)
    family_planning_of_sender=models.TextField(null=True,blank=True)
    beliefs=models.TextField(null=True,blank=True)
    accept_button=models.BooleanField(default=False,null=True,blank=True)
    reject_button=models.BooleanField(default=False,null=True,blank=True)

class AppleSentDashbaord(models.Model):
    amount_sent=models.IntegerField(default=0,null=True,blank=True)
    receiver_email=models.EmailField(blank=True,null=True)
    sender_email=models.EmailField(blank=True,null=True)
    days_left=models.TextField(null=True,blank=True)
    apple_message_alert=models.TextField(null=True,blank=True)
    location_of_the_reciever=models.TextField(null=True,blank=True)
    interests_of_the_reciever=models.TextField(null=True,blank=True)
    education_level_of_reciever=models.TextField(null=True,blank=True)
    family_planning_of_reciever=models.TextField(null=True,blank=True)
    beliefs=models.TextField(null=True,blank=True)
    accept_button=models.BooleanField(default=False,null=True,blank=True)
    reject_button=models.BooleanField(default=False,null=True,blank=True)

class BookMarkDashboard(models.Model):
    email_of_user_bookmarked=models.EmailField(unique=True,blank=True,null=True)
    name_of_user_bookmarked=models.TextField()
    profile_picture=models.TextField()
    location=models.TextField()
    interests=models.TextField()
 # Returns the username of the associated User



class AppleModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    rotting_apples=models.FloatField(default=0,null=True)
    apple_recieved=models.FloatField(default=0,null=True)
    total_apple_sent=models.FloatField(default=0,null=True)
    accepted_apple=models.FloatField(default=0,null=True)
    is_expired=models.BooleanField(default=False,null=True)
    bucket_of_apple=models.FloatField(default=10,null=True)


    def __str__(self):
        return f"{self.user} Apple Profile Details" 

class OnboardingUserDetails(models.Model):
    # profile_photo=models.FileField(upload_to='kyc_images',blank=True,null=True)
    age=models.CharField(null=True,blank=True)
    photo=models.FileField(upload_to='user_images',null=True,blank=True)
    home_town=models.TextField(blank=True,null=True)
    education=models.TextField(blank=True,null=True)
    bio=models.TextField(null=True,blank=True) 
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    interests = ArrayField(
        models.CharField(max_length=100000, blank=True),
         
    )
    
    # images = models.ManyToManyField(Image, related_name='models',blank=True)
    gender=models.CharField(max_length=200,blank=True)
    primary_interest=models.TextField()
    height=models.CharField(max_length=10000,blank=True)
    opening_move=models.TextField()
    dob=models.DateField(blank=True)
    values=ArrayField(
      models.CharField(max_length=100000,blank=True),
    )
    habits=ArrayField(
      models.CharField(max_length=100000,blank=True)
    )
    family_planning=ArrayField(
      models.CharField(max_length=100000,blank=True)
    )
    beliefs=ArrayField(
      models.CharField(max_length=100000,blank=True)
    )
    communities=ArrayField(
      models.CharField(max_length=100000,blank=True)
    )
    name=models.CharField(max_length=1000,blank=True)
    current_location=models.CharField(max_length=2000,blank=True,null=True)
    language=models.CharField(max_length=1000,blank=True,null=True)
    preference=ArrayField(
      models.CharField(max_length=100000,blank=True,null=True),
      null=True,blank=True,
    )
    region=models.CharField(max_length=2000,blank=True)

    preferred_quality_in_others=ArrayField(
        models.CharField(max_length=10000,blank=True,null=True),
        null=True,blank=True
    )
    
 
  
    current_age = models.IntegerField(null=True, blank=True)  # Store age as an integer in years

    # Method to calculate age from date of birth
    def calculate_age(self):
        if self.dob:
            today = date.today()
            years = today.year - self.dob.year

            # Adjust if today's date is before the birthday in the current year
            if (today.month, today.day) < (self.dob.month, self.dob.day):
                years -= 1

            # Format the age as 'years-months-days'
            self.age = f"{years} years"
            self.current_age = years
        else:
            self.age = "DOB not provided"
            self.current_age = None
        
        # Save the updated age
        self.save()

    def __str__(self):
        return f"{self.user} have completed onboarding stage"
    
    # def __str__(self):
    #     return f"{self.user} have completed onboarding stage"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)  
    profile_picture = models.ImageField(upload_to='profile/', blank=True, null=True)  
    phone_number = models.CharField(max_length=15, blank=True, null=True) 
    onboarding_details=models.OneToOneField(OnboardingUserDetails,on_delete=models.CASCADE)
    strengths=models.TextField(null=True,blank=True)
    weaknesses=models.TextField(null=True,blank=True)
    suggestions_user_emails=ArrayField(
        models.EmailField(null=True,blank=True),
        null=True,blank=True
    )

    def __str__(self):
        return self.user.username 



class PurchaseLog(models.Model):
    apple_purchase_logs = models.JSONField()

    def __str__(self):
        return f"Purchase Logs: {self.apple_purchase_logs}"
        
class UserProfileSummary(models.Model):
    interested_in=models.TextField(null=True,blank=True)
    language=models.TextField(null=True,blank=True)
    age_range=models.TextField(null=True,blank=True)
    amount_of_apple_range=models.TextField(null=True,blank=True)
    travel_mode_on=models.BooleanField(default=False,blank=True,null=True)
    distance_range=models.TextField(null=True,blank=True,)
    interests=models.TextField(null=True,blank=True)



