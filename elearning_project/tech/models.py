from django.contrib.auth.models import AbstractUser
from django.db import models

class TechTeam(AbstractUser):
    bio = models.TextField(blank=True)
    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="groups",
        blank=True,
        related_name="tech_team_groups",
        related_query_name="tech_team_group",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="user permissions",
        blank=True,
        related_name="tech_team_permissions",
        related_query_name="tech_team_permission",
        help_text="Specific permissions for this user.",
    )

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
        permissions = [
            ('can_add_course', 'Can add courses'),
            ('can_delete_course', 'Can delete courses'),
            ('can_add_video', 'Can add videos'),
            ('can_delete_video', 'Can delete videos'),
            ('can_manage_credit', 'Can manage student credit'),
        ]
    