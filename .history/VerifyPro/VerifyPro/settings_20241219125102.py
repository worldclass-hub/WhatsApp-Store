"""
Django settings for VerifyPro project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

import os

from .jazzmin import JAZZMIN_SETTINGS

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5-1&xy8kp8@-p5x$y2ni^fih^*fhi!8^7n0r&dx!-c(u&bcp+3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'IDGenie',
    'crispy_forms',
    'crispy_bootstrap5',
    
    # other apps

    'ckeditor',
    'ckeditor_uploader',  # Only if you plan to use the CKEditor file upload feature
]


# Static and media file settings (needed for file uploads)
import os

MEDIA_URL = '/media/'  # URL to access media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Path to save media files locally



CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



ROOT_URLCONF = 'VerifyPro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Add your custom template directory here
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'VerifyPro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


JAZZMIN_SETTINGS = JAZZMIN_SETTINGS



# CKEditor file upload settings
CKEDITOR_UPLOAD_PATH = "uploads/"  # Path to save uploaded files


# CKEditor configuration
# CKEditor configuration
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono-lisa',  # This will set the skin to 'moono-lisa' as requested
        'height': 400,  # Set the height for the editor
        'width': '100%',  # Full width
        'contentsCss': [
            '/static/ckeditor/ckeditor_custom.css',  # Path to your custom CSS
        ],
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms', 'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField']},
            '/',
            {'name': 'basicstyles', 'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph', 'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert', 'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # Forces the next toolbar to appear on a new line
            {'name': 'yourcustomtools', 'items': [
                'Preview',  # Add custom buttons here
                'Maximize',
            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # This uses the custom toolbar config
        'tabSpaces': 4,  # Set tab spaces to 4
        'extraPlugins': ','.join([
            'uploadimage',  # Enable image upload plugin
            'div',  # Enable div plugin
            'autolink',  # Enable auto-link plugin
            'autoembed',  # Enable auto-embed plugin
            'embedsemantic',  # Enable embed semantic plugin
            'autogrow',  # Enable auto-grow plugin
            'devtools',  # Enable devtools plugin
            'widget',  # Enable widget plugin
            'lineutils',  # Enable line utils plugin
            'clipboard',  # Enable clipboard plugin
            'dialog',  # Enable dialog plugin
            'dialogui',  # Enable dialog UI plugin
            'elementspath',  # Enable elementspath plugin
        ]),
    }
}
