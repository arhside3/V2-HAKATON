# Generated by Django 5.0 on 2023-12-10 22:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="shoppingcart",
            options={
                "verbose_name": "список проекта",
                "verbose_name_plural": "список проектов",
            },
        ),
    ]