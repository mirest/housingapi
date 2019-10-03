from django.db import models


class Apartment(models.Model):
    id = models.IntegerField(
        db_column='ApartmentId', primary_key=True)
    apartmentname = models.CharField(
        db_column='ApartmentName', unique=True, max_length=50)
    unitprice = models.DecimalField(
        db_column='UnitPrice', max_digits=12, decimal_places=2, blank=True, null=True)
    locationid = models.ForeignKey(
        'Location', models.CASCADE(), db_column='LocationId')
    specification = models.TextField(db_column='Specification')

    class Meta:
        db_table = 'Apartment'


class Location(models.Model):
    id = models.IntegerField(db_column='LocationId', primary_key=True)
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    address = models.CharField(max_length=100)
    customerid = models.ForeignKey(
        'User', models.CASCADE(), db_column='CustomerId')
    specs = models.TextField(db_column='Specs')

    class Meta:
        db_table = 'Location'


class MessageRecipients(models.Model):
    id = models.IntegerField(primary_key=True)
    messageid = models.ForeignKey(
        'Messages', models.CASCADE(), db_column='MessageId')
    customerid = models.ForeignKey(
        'User', models.CASCADE(), db_column='CustomerId')

    class Meta:
        db_table = 'MessageRecipients'


class Messages(models.Model):
    id = models.AutoField(db_column='MessageId', primary_key=True)
    content = models.CharField(db_column='Content', max_length=256)
    type = models.CharField(db_column='Type', max_length=50)
    senderid = models.ForeignKey(
        'User', models.CASCADE(), db_column='SenderId')
    attachments = models.TextField(db_column='Specs')

    class Meta:
        db_table = 'Messages'


class Serviceproviderservices(models.Model):
    id = models.IntegerField(primary_key=True)
    serviceproviderid = models.ForeignKey(
        'Serviceproviders', models.CASCADE(), db_column='ServiceProviderId')
    price = models.DecimalField(
        db_column='Price', max_digits=18, decimal_places=0)
    serviceid = models.ForeignKey(
        'Services', models.CASCADE(), db_column='ServiceId')

    class Meta:
        db_table = 'ServiceProviderServices'


class ServiceProviders(models.Model):
    id = models.AutoField(
        db_column='ServiceProviderId', primary_key=True)
    serviceprovidername = models.CharField(
        db_column='ServiceProviderName', max_length=200)
    phone = models.CharField(db_column='Phone', max_length=50)
    email = models.CharField(db_column='Email', max_length=50)
    address = models.CharField(db_column='Address', max_length=50)
    active = models.BooleanField(db_column='Active')
    managerid = models.ForeignKey(
        'User', models.CASCADE(), db_column='ManagerId')

    class Meta:
        db_table = 'ServiceProviders'


class Services(models.Model):
    id = models.AutoField(db_column='ServiceId', primary_key=True)
    servicename = models.CharField(
        db_column='ServiceName', unique=True, max_length=40)

    class Meta:
        db_table = 'Services'


class ServiceSubscribers(models.Model):
    id = models.IntegerField(primary_key=True)
    apartmentid = models.ForeignKey(
        Apartment, models.CASCADE(), db_column='ApartmentId')
    serviceid = models.ForeignKey(
        Services, models.CASCADE(), db_column='ServiceId')

    class Meta:
        db_table = 'ServiceSubscribers'


class User(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    # Field name made lowercase.
    id = models.IntegerField(db_column='UserId', primary_key=True)
    phone = models.CharField(max_length=20)
    occupation = models.CharField(max_length=50, blank=True, null=True)
    image = models.CharField(max_length=50, blank=True, null=True)
    interests = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'User'


class UserGroups(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        db_table = 'User_groups'
        unique_together = (('user', 'group'),)


class UserUserPermissions(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        db_table = 'User_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)
    location = models.CharField(max_length=180, blank=True, null=True)

    class Meta:
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)
