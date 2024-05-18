# Generated by Django 4.2.11 on 2024-05-04 11:05

from django.db import migrations, models
import django.db.models.deletion
import uuid
import zelthy.apps.dynamic_models.fields
import zelthy.core.storage_utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appauth', '0006_appusermodel_app_objects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('object_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('circular_no', models.CharField(max_length=100, unique=True)),
                ('level_cutoff_date', models.DateField()),
                ('pdf_file', zelthy.core.storage_utils.ZFileField(upload_to=zelthy.core.storage_utils.RandomUniqueFileName, validators=[zelthy.core.storage_utils.validate_file_extension])),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Franchisee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('object_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('photo', zelthy.core.storage_utils.ZFileField(upload_to=zelthy.core.storage_utils.RandomUniqueFileName, validators=[zelthy.core.storage_utils.validate_file_extension])),
                ('name', models.CharField(max_length=100)),
                ('franchisee_type', models.CharField(choices=[('MF', 'MF - Master Franchisee'), ('DF', 'DF - District Franchisee'), ('DCF', 'DCF - District City Franchisee')], max_length=3)),
                ('abacus', models.BooleanField(default=False)),
                ('vedic_maths', models.BooleanField(default=False)),
                ('handwriting', models.BooleanField(default=False)),
                ('calligraphy', models.BooleanField(default=False)),
                ('robotics', models.BooleanField(default=False)),
                ('dob', models.DateField()),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3)),
                ('center_address', models.TextField()),
                ('communication_address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('educational_qualification', models.CharField(max_length=100)),
                ('present_occupation', models.CharField(max_length=100)),
                ('annual_income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('experience_in_franchisee_model', models.PositiveIntegerField()),
                ('find_about_us', models.CharField(choices=[('existing_franchisee', 'Existing Franchisee'), ('google', 'Google'), ('other', 'Other')], max_length=20)),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('user', zelthy.apps.dynamic_models.fields.ZOneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appauth.appusermodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('object_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('object_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('photo', zelthy.core.storage_utils.ZFileField(upload_to=zelthy.core.storage_utils.RandomUniqueFileName, validators=[zelthy.core.storage_utils.validate_file_extension])),
                ('centre_name', models.CharField(max_length=255)),
                ('program_name', models.CharField(choices=[('abacus', 'Abacus'), ('vedic_maths', 'Vedic Maths'), ('handwriting', 'Handwriting'), ('calligraphy', 'Calligraphy')], max_length=20)),
                ('dob', models.DateField()),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('qualification', models.CharField(max_length=255)),
                ('present_occupation', models.CharField(max_length=255)),
                ('annual_income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('how_did_you_come_to_know_us', models.CharField(choices=[('existing', 'Existing'), ('franchise', 'Franchise'), ('google', 'Google'), ('other', 'Other')], max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('franchise', zelthy.apps.dynamic_models.fields.ZForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_models.franchisee')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('user', zelthy.apps.dynamic_models.fields.ZOneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appauth.appusermodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TrainingDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('object_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('training_level', models.PositiveIntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('franchise', zelthy.apps.dynamic_models.fields.ZForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_models.franchisee')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('name', zelthy.apps.dynamic_models.fields.ZForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_models.teacher')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('object_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('s_id', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('photo', zelthy.core.storage_utils.ZFileField(upload_to=zelthy.core.storage_utils.RandomUniqueFileName, validators=[zelthy.core.storage_utils.validate_file_extension])),
                ('course', models.CharField(choices=[('abacus', 'Abacus'), ('vedic_maths', 'Vedic Maths'), ('handwriting', 'Handwriting')], max_length=20, null=True)),
                ('programme', models.CharField(choices=[('junior', 'Junior'), ('senior', 'Senior')], max_length=10, null=True)),
                ('level', models.IntegerField()),
                ('dob', models.DateField()),
                ('contact', models.CharField(max_length=20)),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10, null=True)),
                ('father_name', models.CharField(max_length=100, null=True)),
                ('father_occupation', models.CharField(max_length=100, null=True)),
                ('mother_name', models.CharField(max_length=100, null=True)),
                ('mother_occupation', models.CharField(max_length=100, null=True)),
                ('qualification', models.CharField(max_length=100, null=True)),
                ('reference_by', models.CharField(choices=[('paper_ads', 'Paper Ads'), ('parents', 'Parents'), ('social_media', 'Social Media'), ('others', 'Others')], max_length=20, null=True)),
                ('residential_address', models.TextField(null=True)),
                ('contact_number', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('school_name', models.CharField(max_length=100, null=True)),
                ('standard', models.CharField(max_length=50, null=True)),
                ('num_siblings', models.IntegerField(null=True)),
                ('join_date', models.DateField(auto_now_add=True)),
                ('course_start_date', models.DateField(null=True)),
                ('dropped', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('franchise', zelthy.apps.dynamic_models.fields.ZForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_models.franchisee')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('object_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('programme', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('contact', models.CharField(max_length=20)),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('school', zelthy.apps.dynamic_models.fields.ZForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_models.school')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LevelCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('object_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('student', zelthy.apps.dynamic_models.fields.ZForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_models.student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('object_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('photo', zelthy.core.storage_utils.ZFileField(upload_to=zelthy.core.storage_utils.RandomUniqueFileName, validators=[zelthy.core.storage_utils.validate_file_extension])),
                ('details', models.TextField()),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('object_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('mail', models.EmailField(max_length=254)),
                ('type', models.CharField(choices=[('Student', 'Student'), ('Franchisee', 'Franchisee'), ('Teacher', 'Teacher')], max_length=255)),
                ('phone_country_code', models.CharField(choices=[('+1', '+1 (United States)'), ('+44', '+44 (United Kingdom)'), ('+91', '+91 (India)'), ('+86', '+86 (China)'), ('+81', '+81 (Japan)'), ('+49', '+49 (Germany)'), ('+7', '+7 (Russia)'), ('+55', '+55 (Brazil)'), ('+33', '+33 (France)'), ('+39', '+39 (Italy)'), ('+82', '+82 (South Korea)')], max_length=5)),
                ('phone_number', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=255)),
                ('pin', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CompetitionStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('object_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('competition', zelthy.apps.dynamic_models.fields.ZForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_models.competition')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('franchise', zelthy.apps.dynamic_models.fields.ZForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_models.franchisee')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('student', zelthy.apps.dynamic_models.fields.ZForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_models.student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CompetitionResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('object_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('rank', models.PositiveIntegerField()),
                ('competition', zelthy.apps.dynamic_models.fields.ZForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_models.competition')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('student', zelthy.apps.dynamic_models.fields.ZForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_models.student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Birthday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('object_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('franchise', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
