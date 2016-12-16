from django.contrib import admin
from .models import Users

# Register your models here.
class SignupAdmin(admin.ModelAdmin):
	list_display = ['first_name','last_name','email']
	class Meta:
		model = Users

admin.site.register(Users,SignupAdmin)