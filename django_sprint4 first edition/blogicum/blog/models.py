from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


User = get_user_model()


class BaseModel(models.Model):
    is_published = models.BooleanField(
        'Опубликовано', default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.')
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ('created_at,')


class Category(BaseModel):
    title = models.CharField(
        'Заголовок', max_length=settings.MAX_FIELD_LENGTH, blank=False)
    description = models.TextField('Описание', blank=False)
    slug = models.SlugField(
        'Идентификатор', unique=True, blank=False,
        help_text=('Идентификатор страницы для URL; разрешены символы'
                   ' латиницы, цифры, дефис и подчёркивание.'))

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.title[:settings.REPRESENTATION_LENGTH]


class Location(BaseModel):
    name = models.CharField(
        'Название места', max_length=settings.MAX_FIELD_LENGTH, blank=False
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self) -> str:
        return self.name[:settings.REPRESENTATION_LENGTH]


class Post(BaseModel):
    title = models.CharField(
        'Заголовок', max_length=settings.MAX_FIELD_LENGTH, blank=False)
    text = models.TextField('Текст', blank=False)
    pub_date = models.DateTimeField(
        'Дата и время публикации', auto_now_add=False, blank=False,
        help_text=('Если установить дату и время в будущем — можно'
                   ' делать отложенные публикации.'))
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Местоположение'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория'
    )

    class Meta:
        default_related_name = 'posts'
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-pub_date',)

    def __str__(self) -> str:
        return self.title[:settings.REPRESENTATION_LENGTH]
    