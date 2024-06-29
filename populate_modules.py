import os
import django

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_its.settings')  # Replace 'project_its' with your actual project name
django.setup()

from apps.modules.models import Module
from apps.levels.models import Level

# Fetch the level instance or create if it doesn't exist
level = Level.objects.get_or_create(id=1, defaults={"name": "Default Level"})[0]

# Sample data for the Module table
modules_data = [
    {
        "id": 1,
        "title": "JavaScript Basics",
        "description": "This module looks into the overview of JS and some of its basic concepts",
        "num_lessons": 15,
        "level_id": level.id
    },
    {
        "id": 2,
        "title": "JavaScript Operators",
        "description": "This module looks into the different operators that are used in Javascript",
        "num_lessons": 16,
        "level_id": level.id
    },
    {
        "id": 3,
        "title": "JavaScript Control flows",
        "description": "This module looks into the different loops in JS",
        "num_lessons": 9,
        "level_id": level.id
    },
    {
        "id": 4,
        "title": "JavaScript Functions",
        "description": "This module looks into the JS functions such as how to call one, invoke etc",
        "num_lessons": 16,
        "level_id": level.id
    }
]

# Populate the Module table
for module_data in modules_data:
    Module.objects.update_or_create(
        id=module_data["id"],
        defaults={
            "title": module_data["title"],
            "description": module_data["description"],
            "num_lessons": module_data["num_lessons"],
            "level_id": module_data["level_id"]
        }
    )

print("Modules table populated successfully.")
    