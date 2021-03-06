# Generated by Django 3.2.4 on 2021-07-24 12:05

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('age', models.IntegerField(default=20)),
                ('mobilenumber', models.CharField(max_length=10, null=True)),
                ('uimg', models.ImageField(default='ics.jpg', upload_to='Profilepics/')),
                ('role', models.IntegerField(choices=[(1, 'Guest'), (2, 'Manager'), (3, 'User')], default=1)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Rolereq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rltype', models.IntegerField(choices=[(2, 'Manager'), (3, 'User')])),
                ('pfe', models.ImageField(default='ics.jpg', upload_to='Rolereqpics/')),
                ('is_checked', models.BooleanField(default=False)),
                ('uname', models.CharField(max_length=50)),
                ('ud', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carname', models.CharField(max_length=30)),
                ('carprice', models.IntegerField()),
                ('carmodel', models.CharField(choices=[('carcategory', 'Select Category'), ('4-door sedan', '4-Door Sedan'), ('station wagon', 'Station Wagon'), ('sports car', 'Sports Car'), ('2-door coupes', '2-Door Coupes'), ('convertibles', 'Convertibles'), ('mini-vans', 'Mini-vans'), ('suv', 'SUV'), ('pickup trucks', 'Pickup Trucks'), ('vans', 'Vans'), ('hatchback', 'Hatchback')], default='carcategory', max_length=20)),
                ('purchased_year', models.IntegerField()),
                ('carfuel', models.CharField(choices=[('fuel type', 'Select Fuel Type'), ('petrol', 'Petrol'), ('disel', 'Disel'), ('cng', 'CNG'), ('electric', 'Electric')], default='fuel type', max_length=20)),
                ('carseats', models.IntegerField()),
                ('carkms', models.IntegerField()),
                ('carimg', models.ImageField(default='w.jpg', upload_to='static/')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
