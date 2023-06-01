from django.db import models

class Meeting(models.Model):
    HISTORY_LOVE = (
        ('Да', 'Да'),
        ('Нет', "Нет"),
        ('Никогда', 'Никогда')
    )

    P_OF_D = (
        ('Для дружбы', 'Для дружбы'),
        ('Для отношений', 'Для отношений'),
        ('Для брака', 'Для брака')
    )

    name = models.CharField("Ваше имя?", max_length=100)
    age = models.PositiveIntegerField('Ваш возраст?', default=18)
    image = models.ImageField('Добавьте фотку', upload_to='')
    about = models.TextField('Расскажите о себе?', blank=True, null=True)
    number_phone = models.CharField('Ваш номер телефона', max_length=13)
    video = models.URLField('Ваш любимый фильм', blank=True, null=True)
    history_love = models.CharField('Были ли вы в отношениях?', max_length=100, choices=HISTORY_LOVE)
    purpose_of_dating = models.CharField('Цель знакомства?', max_length=100, choices=P_OF_D)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Анкету'
        verbose_name_plural = 'Анкеты'

class Reviews(models.Model):
    name_reviews = models.ForeignKey(Meeting, on_delete=models.CASCADE,
                                     related_name='comment_object')
    description = models.TextField('ваш отзыв')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description