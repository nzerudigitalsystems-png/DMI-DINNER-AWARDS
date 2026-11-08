from django.db import migrations


CATEGORY_NAMES = [
    'Swazi of the Batch',
    'Stoner of the Batch',
    'Chidakwa of the Batch',
    'Class Rep of the Batch',
    'Most Beautiful Female of the Batch',
    'Most Handsome Male of the Batch',
    'Resilient of the Batch',
]


def make_categories_gendered(apps, schema_editor):
    AwardCategory = apps.get_model('awards', 'AwardCategory')
    AwardCategory.objects.using(schema_editor.connection.alias).filter(
        name__in=CATEGORY_NAMES
    ).update(
        slot_type='gendered',
        slot_a_label='Male Nominee',
        slot_b_label='Female Nominee',
    )


class Migration(migrations.Migration):
    dependencies = [
        ('awards', '0003_seed_award_categories'),
    ]

    operations = [
        migrations.RunPython(make_categories_gendered, migrations.RunPython.noop),
    ]
