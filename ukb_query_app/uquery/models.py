# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from psycopg2 import paramstyle


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DataDictionaryShowcase(models.Model):
    path = models.TextField(blank=True, null=True)
    fieldid = models.BigIntegerField(primary_key=True)
    show_field = models.TextField(blank=True, null=True)
    participants = models.BigIntegerField(blank=True, null=True)
    items = models.BigIntegerField(blank=True, null=True)
    stability = models.TextField(blank=True, null=True)
    valuetype = models.TextField(blank=True, null=True)
    units = models.TextField(blank=True, null=True)
    itemtype = models.TextField(blank=True, null=True)
    strata = models.TextField(blank=True, null=True)
    sexed = models.TextField(blank=True, null=True)
    instances = models.BigIntegerField(blank=True, null=True)
    array = models.BigIntegerField(blank=True, null=True)
    coding = models.ForeignKey('Encoding', models.DO_NOTHING, db_column='coding', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_dictionary_showcase'
        unique_together = (('coding', 'fieldid'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Ehierint(models.Model):
    code_id = models.IntegerField()
    parent_id = models.IntegerField()
    value = models.IntegerField()
    meaning = models.CharField(max_length=1000)
    selectable = models.IntegerField()
    showcase_order = models.IntegerField()
    fk_encoding_ehierint = models.OneToOneField('Encoding', models.DO_NOTHING, db_column='fk_encoding_ehierint', primary_key=True)

    class Meta:
        managed = False
        db_table = 'ehierint'
        unique_together = (('fk_encoding_ehierint', 'meaning', 'value'),)


class Ehierstring(models.Model):
    code_id = models.IntegerField()
    parent_id = models.IntegerField()
    value = models.CharField(max_length=1000)
    meaning = models.CharField(max_length=1000)
    selectable = models.IntegerField()
    showcase_order = models.IntegerField()
    fk_encoding_ehierstring = models.OneToOneField('Encoding', models.DO_NOTHING, db_column='fk_encoding_ehierstring', primary_key=True)

    class Meta:
        managed = False
        db_table = 'ehierstring'
        unique_together = (('fk_encoding_ehierstring', 'meaning', 'value', 'parent_id'),)


class Encoding(models.Model):
    encoding_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=1000)
    availability = models.IntegerField()
    coded_as = models.IntegerField()
    structure = models.IntegerField()
    num_members = models.IntegerField()
    descript = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'encoding'


class Esimpdate(models.Model):
    value = models.DateField()
    meaning = models.CharField(max_length=1000)
    showcase_order = models.IntegerField()
    fk_encoding_esimpdate = models.OneToOneField(Encoding, models.DO_NOTHING, db_column='fk_encoding_esimpdate', primary_key=True)

    class Meta:
        managed = False
        db_table = 'esimpdate'
        unique_together = (('fk_encoding_esimpdate', 'meaning', 'value'),)


class Esimpint(models.Model):
    value = models.IntegerField()
    meaning = models.CharField(max_length=1000)
    showcase_order = models.IntegerField()
    fk_encoding_esimpint = models.OneToOneField(Encoding, models.DO_NOTHING, db_column='fk_encoding_esimpint', primary_key=True)

    class Meta:
        managed = False
        db_table = 'esimpint'
        unique_together = (('fk_encoding_esimpint', 'value'), ('fk_encoding_esimpint', 'value'),)


class Esimpreal(models.Model):
    value = models.IntegerField()
    meaning = models.CharField(max_length=1000)
    showcase_order = models.IntegerField()
    fk_encoding_esimpreal = models.ForeignKey(Encoding, models.DO_NOTHING, db_column='fk_encoding_esimpreal')

    class Meta:
        managed = False
        db_table = 'esimpreal'


class Esimpstring(models.Model):
    value = models.CharField(max_length=1000)
    meaning = models.CharField(max_length=1000)
    showcase_order = models.IntegerField(blank=True, null=True)
    fk_encoding_esimpstring = models.ForeignKey(Encoding, models.DO_NOTHING, db_column='fk_encoding_esimpstring')

    class Meta:
        managed = False
        db_table = 'esimpstring'


class Field(models.Model):
    field_num = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=1000)
    availability = models.IntegerField()
    stability = models.IntegerField()
    private = models.IntegerField()
    value_type = models.CharField(max_length=1000)
    base_type = models.IntegerField()
    item_type = models.IntegerField()
    strata = models.IntegerField()
    instanced = models.IntegerField()
    arrayed = models.IntegerField()
    sexed = models.IntegerField()
    units = models.CharField(max_length=1000, blank=True, null=True)
    instance_min = models.IntegerField()
    instance_max = models.IntegerField()
    array_min = models.IntegerField()
    array_max = models.IntegerField()
    notes = models.CharField(max_length=1000, blank=True, null=True)
    debut = models.CharField(max_length=1000)
    version = models.CharField(max_length=1000)
    num_participants = models.IntegerField()
    item_count = models.IntegerField()
    showcase_order = models.IntegerField()
    tier = models.IntegerField()
    instance_id = models.IntegerField()
    encoding = models.ForeignKey(Encoding, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'field'

class Fieldsum(models.Model):
    title = models.CharField(max_length=1000)
    item_type = models.IntegerField()
    field_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fieldsum'


class Instances(models.Model):
    instance_id = models.IntegerField()
    descript = models.CharField(max_length=1000)
    num_members = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'instances'


class Insvalue(models.Model):
    index = models.IntegerField()
    title = models.CharField(max_length=1000)
    descript = models.CharField(max_length=1000)
    instance_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'insvalue'


class RecordColumn(models.Model):
    table_name = models.CharField(max_length=1000)
    column_name = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    value_type = models.IntegerField()
    encoding_id = models.IntegerField()
    orda = models.IntegerField()
    units = models.CharField(max_length=1000, blank=True, null=True)
    notes = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record_column'


class RecordTable(models.Model):
    table_name = models.CharField(max_length=1000)
    parent_name = models.CharField(max_length=1000, blank=True, null=True)
    title = models.CharField(max_length=1000)
    available = models.IntegerField()
    private = models.IntegerField()
    record_field_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'record_table'


class Ukb37912(models.Model):
    data = models.JSONField()

    class Meta:
        managed = False
        db_table = 'ukb37912'


class UqueryTestdb(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'uquery_testdb'


class UqueryUkb37912Test2(models.Model):
    id = models.BigAutoField(primary_key=True)
    data = models.JSONField()

    class Meta:
        managed = False
        db_table = 'uquery_ukb37912_test2'

class testJSON(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)