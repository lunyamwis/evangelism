from django.db import models

class ChurchMember(models.Model):
    full_name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.full_name


class BaptizedMember(models.Model):
    full_name = models.CharField(max_length=255)
    baptism_date = models.DateField()
    contact_info = models.CharField(max_length=255, blank=True)
    originating_outreach = models.CharField(
        max_length=50,
        choices=[
            ('bible_work', 'Bible Work'),
            ('medical_missionary', 'Medical Missionary'),
            ('other', 'Other'),
        ],
        default='other'
    )
    assigned_follower = models.ForeignKey(
        ChurchMember,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='members_to_nurture'
    )
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} ({self.baptism_date})"


class FollowUpInteraction(models.Model):
    member = models.ForeignKey(BaptizedMember, on_delete=models.CASCADE, related_name='follow_ups')
    date = models.DateField()
    method = models.CharField(
        max_length=100,
        choices=[
            ('phone_call', 'Phone Call'),
            ('home_visit', 'Home Visit'),
            ('email', 'Email'),
            ('group_meeting', 'Group Meeting'),
            ('other', 'Other'),
        ]
    )
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Follow-up on {self.date} via {self.method} for {self.member.full_name}"
