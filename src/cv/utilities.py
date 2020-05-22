from django.utils.crypto import get_random_string
from rest_framework import serializers
from usamo.settings import settings
import os
import random
import datetime
import jinja2
import pdfkit
import platform
import io

from .templates.templates import TEMPLATES_CHOICES


def create_unique_filename(prefix, ext):
    full_date = datetime.datetime.now()
    year = full_date.strftime("%Y")
    month = full_date.strftime("%m")
    day = full_date.strftime("%d")

    length = random.randint(32, 48)
    unique_string = get_random_string(length=length)
    unique_filename = unique_string + '.' + ext
    full_path = os.path.join(settings.MEDIA_ROOT, prefix,
                             year, month, day, unique_filename)
    while os.path.exists(full_path):
        length = random.randint(32, 48)
        unique_string = get_random_string(length=length)
        unique_filename = unique_string + '.' + ext
        full_path = os.path.join(
            settings.MEDIA_ROOT, prefix, year, month, day, unique_filename)

    return unique_filename


def generate(data, template):
    template_filename = next((filename for (name, filename) in TEMPLATES_CHOICES if name == template), None)
    if not template_filename:
        raise serializers.ValidationError("Not valid template name")

    # options for the pdf
    options = {
        'page-size': 'Letter',
        'margin-top': '0in',
        'margin-right': '0in',
        'margin-bottom': '0in',
        'margin-left': '0in'
    }

    # get paths
    module_dir = os.path.dirname(__file__)
    template_path = os.path.join(module_dir, 'templates/')
    html_path = os.path.join(module_dir, 'templates/generated.html')
    # get data and jinja
    env = jinja2.environment.Environment(
        loader=jinja2.FileSystemLoader(template_path)
    )

    # generate html and pdf
    template = env.get_template(template_filename)
    with io.open(html_path, "w", encoding="utf-8") as f:
        f.write(template.render(**data))
    if platform.system() != 'Windows':
        options['zoom'] = '0.78125'
    pdf = pdfkit.from_file(
        html_path, False, configuration=settings._get_pdfkit_config(), options=options)
    # right now it returns the pdf
    return pdf
