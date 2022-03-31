from django.db import models

# Create your models here.
class Ehierint(models.Model):
    code_id = models.IntegerField()
    parent_id = models.IntegerField()
    value = models.IntegerField()
    meaning = models.CharField(max_length=1000)
    selectable = models.IntegerField()
    showcase_order = models.IntegerField()
    encoding_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ehierint'
    
    def __str__(self):
        return self.meaning


class Ehierstring(models.Model):
    code_id = models.IntegerField()
    parent_id = models.IntegerField()
    value = models.CharField(max_length=1000)
    meaning = models.CharField(max_length=1000)
    selectable = models.IntegerField()
    showcase_order = models.IntegerField()
    encoding_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ehierstring'


class Encoding(models.Model):
    encoding_id = models.IntegerField()
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
    encoding_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'esimpdate'


class Esimpint(models.Model):
    value = models.IntegerField()
    meaning = models.CharField(max_length=1000)
    showcase_order = models.IntegerField()
    encoding_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'esimpint'


class Esimpreal(models.Model):
    value = models.IntegerField()
    meaning = models.CharField(max_length=1000)
    showcase_order = models.IntegerField()
    encoding_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'esimpreal'


class Esimpstring(models.Model):
    value = models.CharField(max_length=1000)
    meaning = models.CharField(max_length=1000)
    showcase_order = models.IntegerField(blank=True, null=True)
    encoding_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'esimpstring'


class Field(models.Model):
    field_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=1000)
    availability = models.IntegerField()
    stability = models.IntegerField()
    private = models.IntegerField()
    value_type = models.IntegerField()
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
    encoding_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'field'

    # def __str__(self):
    #     return self.version.values()

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
    data = models.JSONField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ukb37912'
    


class TestDb(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    
    class Meta:
        managed = False
        db_table = 'uquery_testdb'
