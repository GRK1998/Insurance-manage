from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('insurance', '0002_policy'),
    ]

    operations = [
        migrations.CreateModel(
            name='PolicyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='Pending', max_length=100)),
                ('creation_date', models.DateField(auto_now=True)),
                ('Policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.Policy')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
        ),
    ]
