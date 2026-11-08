from django.db import migrations


CATEGORIES = [
    {
        'name': 'Hustler of the Batch',
        'slug': 'hustler-of-the-batch',
        'display_order': 21,
    },
    {
        'name': 'Borrower of the Batch',
        'slug': 'borrower-of-the-batch',
        'display_order': 22,
    },
]


def add_categories(apps, schema_editor):
    AwardCategory = apps.get_model('awards', 'AwardCategory')
    database = schema_editor.connection.alias
    for category in CATEGORIES:
        AwardCategory.objects.using(database).get_or_create(
            slug=category['slug'],
            defaults={
                **category,
                'slot_type': 'gendered',
                'slot_a_label': 'Boy Nominee',
                'slot_b_label': 'Girl Nominee',
                'is_active': True,
                'accepts_online_nominations': True,
            },
        )


class Migration(migrations.Migration):
    dependencies = [
        ('awards', '0004_make_selected_categories_gendered'),
    ]

    operations = [
        migrations.RunPython(add_categories, migrations.RunPython.noop),
    ]
