from django.db import models

#################################################
#### LOGOS AND ICONS UPLOAD PATHS
#################################################

def language_logos_path(self):
    return f'graphics/logos/lenguajes/{self.name}'

def language_icon_path(self):
    return f'graphics/icons/lenguajes/{self.name}'

def framework_logos_path(self):
    return f'graphics/logos/frameworks/{self.name}'

def framework_icon_path(self):
    return f'graphics/icons/frameworks/{self.name}'

#################################################
#### MODELS RELATED WITH LANGUAGES
#################################################

class Language(models.Model):
    name = models.CharField(max_length=60, verbose_name='lenguaje', unique=True)
    description = models.TextField(verbose_name='descripción', blank=True)
    icon = models.ImageField(verbose_name='icon', upload_to=language_icon_path, blank=True)
    logo = models.ImageField(verbose_name='logo', upload_to=language_logos_path, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

class Framework(models.Model):
    language = models.ForeignKey(Language, models.CASCADE)
    name = models.CharField(max_length=60, verbose_name='framework', unique=True)
    description = models.TextField(verbose_name='descripción', blank=True)
    icon = models.ImageField(verbose_name='icon', upload_to=framework_icon_path, blank=True)
    logo = models.ImageField(verbose_name='logo', upload_to=framework_logos_path, blank=True)

    class Meta:
        ordering = ['language']

    def __str__(self):
        return f'{self.name}  ({self.language})'