import csv
from django.contrib.auth.models import User
from invitation.models import Profile  # adjust if Profile is in a different app

with open('user_batch.csv', encoding='utf-8-sig', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        username = row['Username'].strip()
        email = row['Email Address '].strip() if row['Email Address '] else ''
        password = row['Password'].strip()
        first_name = row['Name'].strip()
        instagram = row['Instagram Handle '].strip()

        if username and password:
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.email = email
                user.first_name = first_name
                user.set_password(password)
                user.save()
                Profile.objects.update_or_create(user=user, defaults={'instagram': instagram})
                print(f"✅ Created user: {username}")
            else:
                print(f"⚠️ User already exists: {username}")
