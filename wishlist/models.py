from django.db import models

class WishlistItem(models.Model):
    item = models.CharField(max_length=255)
    type = models.CharField(max_length=100, blank=True)
    brand = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    image = models.URLField(blank=True)  # direct image URL
    preference = models.CharField(
        max_length=100,
        choices=[
            ("favorite", "Stephcynie's Favorite"),
            ("alternative", "Alternative"),
            ("giftcard", "Gift Card"),
        ],
        blank=True
    )
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return self.item
