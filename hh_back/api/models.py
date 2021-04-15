from django.db import models


class Company(models.Model):
    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
    name = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=255)
    address = models.TextField()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address,
        }

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'
    name = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(
        Company, null=True, blank=True, on_delete=models.SET_NULL)

    def to_json(self):
        c = Company.objects.get(id=self.company.id)
        json_obj = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            # 'company':'',
        }
        json_obj['company'] =c.to_json()
        return json_obj
    def __str__(self):
        return self.name
