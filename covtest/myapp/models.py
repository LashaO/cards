from django.db import models

# Create your models here.

class Order(models.Model):
    date = models.DateField()
    #input
    glovo_id = models.IntegerField()
    glovo_code = models.CharField(max_length=255)
    glovo_description = models.TextField()
    glovo_scheduleTime = models.CharField(max_length=255)
    # glovo_addresses = models.CharField()
    glovo_state = models.CharField(max_length=255)
    glovo_reference = models.TextField()

    # processing
    # if glovo_address.type == 'DELIVERY':

    # glovo_addess_latitude = 
    # glovo_addess_longitude = 
    # glovo_address_phone = 
    # glovo_address_type = 
    # glovo_address_label = 
    # glovo_address_details = 
    # glovo_address_contactPhone = 
    # glovo_address_contactPerson = 
    # glovo_address_instructions = 

    # 




    # status control
    # ['pending', ]
    # status = 
    # cancelled_labs = []
    # accepted_by = 
    # status_countdown = 

    def __str__(self):
        return str(self.glovo_id)



    # 
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Lab(models.Model):
    working_time_start = models.DateField()
    working_time_end = models.DateField()

    # # if time > working_time_start & ... :
    #     status = 

    longitude = models.FloatField()
    latitude = models.FloatField()
    override_status = models.BooleanField() # for temporarily disallowing labs from taking orders
    order_count =  models.IntegerField()
    
    # when a new lab is added do viewers have to be refreshed?
    # atomic?

    # sender in lab save() receiver in view while loop