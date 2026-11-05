from django.db import migrations


DEFAULT_CATEGORIES = [
    {
        'name': 'Yaza of the Batch',
        'slug': 'yaza-of-the-batch',
        'slot_type': 'gendered',
        'slot_a_label': 'Male Yaza',
        'slot_b_label': 'Female Yaza',
    },
    {
        'name': 'Gist Mami and Gist Papi',
        'slug': 'gist-mami-and-gist-papi',
        'slot_type': 'gendered',
        'slot_a_label': 'Gist Papi',
        'slot_b_label': 'Gist Mami',
    },
    {
        'name': 'Enjoyment Mami and Enjoyment Papi',
        'slug': 'enjoyment-mami-and-enjoyment-papi',
        'slot_type': 'gendered',
        'slot_a_label': 'Enjoyment Papi',
        'slot_b_label': 'Enjoyment Mami',
    },
    {
        'name': 'Most Smart',
        'slug': 'most-smart',
        'slot_type': 'gendered',
        'slot_a_label': 'Most Smart Male',
        'slot_b_label': 'Most Smart Female',
    },
    {
        'name': 'Swazi of the Batch',
        'slug': 'swazi-of-the-batch',
        'slot_type': 'single',
        'slot_a_label': 'Nominee',
        'slot_b_label': '',
    },
    {
        'name': 'Stoner of the Batch',
        'slug': 'stoner-of-the-batch',
        'slot_type': 'single',
        'slot_a_label': 'Nominee',
        'slot_b_label': '',
    },
    {
        'name': 'Chidakwa of the Batch',
        'slug': 'chidakwa-of-the-batch',
        'slot_type': 'single',
        'slot_a_label': 'Nominee',
        'slot_b_label': '',
    },
    {
        'name': 'Prayer Warrior of the Batch',
        'slug': 'prayer-warrior-of-the-batch',
        'slot_type': 'gendered',
        'slot_a_label': 'Male Prayer Warrior',
        'slot_b_label': 'Female Prayer Warrior',
    },
    {
        'name': 'Most Interactive',
        'slug': 'most-interactive',
        'slot_type': 'gendered',
        'slot_a_label': 'Most Interactive Male',
        'slot_b_label': 'Most Interactive Female',
    },
    {
        'name': 'Class Rep of the Batch',
        'slug': 'class-rep-of-the-batch',
        'slot_type': 'single',
        'slot_a_label': 'Nominee',
        'slot_b_label': '',
    },
    {
        'name': 'Most Beautiful Female of the Batch',
        'slug': 'most-beautiful-female-of-the-batch',
        'slot_type': 'single',
        'slot_a_label': 'Nominee',
        'slot_b_label': '',
    },
    {
        'name': 'Most Handsome Male of the Batch',
        'slug': 'most-handsome-male-of-the-batch',
        'slot_type': 'single',
        'slot_a_label': 'Nominee',
        'slot_b_label': '',
    },
    {
        'name': 'Best Dressed',
        'slug': 'best-dressed',
        'slot_type': 'gendered',
        'slot_a_label': 'Best Dressed Male',
        'slot_b_label': 'Best Dressed Female',
    },
    {
        'name': 'Best Duo',
        'slug': 'best-duo',
        'slot_type': 'pair',
        'slot_a_label': 'First Member',
        'slot_b_label': 'Second Member',
    },
    {
        'name': 'Couple of the Batch',
        'slug': 'couple-of-the-batch',
        'slot_type': 'pair',
        'slot_a_label': 'Partner A',
        'slot_b_label': 'Partner B',
    },
    {
        'name': 'Best Entertainer of the Batch',
        'slug': 'best-entertainer-of-the-batch',
        'slot_type': 'gendered',
        'slot_a_label': 'Best Entertainer Male',
        'slot_b_label': 'Best Entertainer Female',
    },
    {
        'name': 'Hacker of the Batch',
        'slug': 'hacker-of-the-batch',
        'slot_type': 'single',
        'slot_a_label': 'Nominee',
        'slot_b_label': '',
    },
    {
        'name': 'Innovator of the Batch',
        'slug': 'innovator-of-the-batch',
        'slot_type': 'single',
        'slot_a_label': 'Nominee',
        'slot_b_label': '',
    },
    {
        'name': 'Producer of the Batch',
        'slug': 'producer-of-the-batch',
        'slot_type': 'single',
        'slot_a_label': 'Nominee',
        'slot_b_label': '',
    },
    {
        'name': 'Resilient of the Batch',
        'slug': 'resilient-of-the-batch',
        'slot_type': 'single',
        'slot_a_label': 'Nominee',
        'slot_b_label': '',
    },
]


def seed_categories(apps, schema_editor):
    AwardCategory = apps.get_model('awards', 'AwardCategory')
    database = schema_editor.connection.alias

    for order, category in enumerate(DEFAULT_CATEGORIES, start=1):
        AwardCategory.objects.using(database).get_or_create(
            slug=category['slug'],
            defaults={
                **category,
                'display_order': order,
                'is_active': True,
                'accepts_online_nominations': True,
            },
        )


class Migration(migrations.Migration):
    dependencies = [
        ('awards', '0002_alter_awardcategory_created_at_and_more'),
    ]

    operations = [
        migrations.RunPython(seed_categories, migrations.RunPython.noop),
    ]
