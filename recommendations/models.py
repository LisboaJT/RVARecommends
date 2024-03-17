from django.db import models


class Restaurant(models.Model):
    # name = models.CharField(max_length=255)
    # category = models.CharField(max_length=255)
    index_name = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    description = models.TextField()
    category = models.CharField(max_length=255, blank=True, null=True)
    is_curated = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class VotingData(models.Model):
    voter_id = models.CharField(max_length=255)  # or an IntegerField, adjust based on your data
    restaurant_a = models.ForeignKey(Restaurant, related_name='votes_as_a', on_delete=models.CASCADE)
    restaurant_b = models.ForeignKey(Restaurant, related_name='votes_as_b', on_delete=models.CASCADE)
    # Include other fields necessary for the recommendation logic

    class Meta:
        unique_together = [['restaurant_a', 'restaurant_b', 'voter_id']]  # Assuming this combination is unique
