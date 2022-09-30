# Generated by Django 3.2.6 on 2021-09-01 22:45

from django.db import migrations, models
import django.db.models.deletion
import tests.testapp.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtailmedia.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0059_apply_collection_ordering"),
        ("wagtailmedia", "0004_duration_optional_floatfield"),
        ("wagtailmedia_tests", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogStreamPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("author", models.CharField(max_length=255)),
                ("date", models.DateField(verbose_name="Post date")),
                (
                    "body",
                    wagtail.core.fields.StreamField(
                        [
                            (
                                "heading",
                                wagtail.core.blocks.CharBlock(
                                    form_classname="title", icon="title"
                                ),
                            ),
                            (
                                "paragraph",
                                wagtail.core.blocks.RichTextBlock(icon="pilcrow"),
                            ),
                            (
                                "media",
                                tests.testapp.models.TestMediaBlock(icon="media"),
                            ),
                            (
                                "video",
                                wagtailmedia.blocks.VideoChooserBlock(icon="media"),
                            ),
                            (
                                "audio",
                                wagtailmedia.blocks.AudioChooserBlock(icon="media"),
                            ),
                        ]
                    ),
                ),
                (
                    "featured_media",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="wagtailmedia.media",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
