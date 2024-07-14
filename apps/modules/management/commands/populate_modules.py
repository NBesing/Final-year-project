from django.core.management.base import BaseCommand
from apps.modules.models import Module
from apps.levels.models import Level

class Command(BaseCommand):
    help = 'Populate the Module table with initial data'

    def handle(self, *args, **options):
        # Fetch the level instance or create if it doesn't exist
        level, created = Level.objects.get_or_create(id=1, defaults={"name": "Default Level"})

        # Sample data for the Module table
        modules_data = [
            {
                "id": 1,
                "title": "JavaScript Basics",
                "description": "This module covers the fundamental concepts of the language, including variables, data types, literals, and syntax.",
                "num_lessons": 13,
                "level": level
            },
            {
                "id": 2,
                "title": "JavaScript Operators",
                "description": "This module explores the various types of operators available, such as comparison, and logical operators",
                "num_lessons": 15,
                "level": level
            },
            {
                "id": 3,
                "title": "JavaScript Control flows",
                "description": "This module focuses on the control flow structures, including conditional statements and looping constructs",
                "num_lessons": 10,
                "level": level
            },
            {
                "id": 4,
                "title": "JavaScript Functions",
                "description": "This module delves into the creation and usage of reusable code blocks called functions",
                "num_lessons": 16,
                "level": level
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
                    "level": module_data["level"]
                }
            )

        self.stdout.write(self.style.SUCCESS('Modules table populated successfully.'))
