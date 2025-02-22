# Generated by Django 5.1.6 on 2025-02-20 08:16

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.fields.StreamField([('heading_block', 2), ('paragraph_block', 3), ('image_block', 6), ('code', 9), ('block_quote', 12), ('embed_image', 14), ('embed_video', 15), ('embed_block', 16), ('markdown', 17)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'form_classname': 'title', 'required': True}), 1: ('wagtail.blocks.ChoiceBlock', [], {'blank': True, 'choices': [('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], 'required': False}), 2: ('wagtail.blocks.StructBlock', [[('heading_text', 0), ('size', 1)]], {}), 3: ('wagtail.blocks.RichTextBlock', (), {'icon': 'pilcrow', 'template': 'blocks/paragraph_block.html'}), 4: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': True}), 5: ('wagtail.blocks.CharBlock', (), {'required': False}), 6: ('wagtail.blocks.StructBlock', [[('image', 4), ('caption', 5), ('attribution', 5)]], {}), 7: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], 'help_text': 'Coding language', 'identifier': 'language', 'label': 'Language'}), 8: ('wagtail.blocks.TextBlock', (), {'identifier': 'code', 'label': 'Code'}), 9: ('wagtail.blocks.StructBlock', [[('language', 7), ('code', 8)]], {'label': 'Code'}), 10: ('wagtail.blocks.TextBlock', (), {}), 11: ('wagtail.blocks.CharBlock', (), {'blank': True, 'label': 'e.g. Mary Berry', 'required': False}), 12: ('wagtail.blocks.StructBlock', [[('text', 10), ('attribute_name', 11)]], {}), 13: ('wagtail.blocks.CharBlock', (), {'required': True}), 14: ('wagtail.blocks.StructBlock', [[('imagelink', 13), ('caption', 5), ('attribution', 5)]], {}), 15: ('wagtail.blocks.StructBlock', [[('videolink', 13), ('caption', 5), ('attribution', 5)]], {}), 16: ('wagtail.embeds.blocks.EmbedBlock', (), {'help_text': 'Insert an embed URL e.g https://www.youtube.com/watch?v=SGJFWirQ3ks', 'icon': 'media', 'template': 'blocks/embed_block.html'}), 17: ('wagtailmarkdown.blocks.MarkdownBlock', (), {})}, verbose_name='Page body'),
        ),
    ]
