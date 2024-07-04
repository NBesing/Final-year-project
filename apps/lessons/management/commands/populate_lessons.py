import json
from django.core.management.base import BaseCommand, CommandError
from apps.lessons.models import Lesson  # Adjust import path as per your structure

class Command(BaseCommand):
    help = 'Populate Lesson model with data from JSON file'

    def handle(self, *args, **options):
        json_file = 'fixtures/lessons.json'  # Replace with your JSON file path

        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                lessons_data = json.load(f)

                for lesson_data in lessons_data:
                    try:
                        lesson_fields = lesson_data.get('fields', {})
                        module_id = lesson_fields.get('module_id')
                        title = lesson_fields.get('title')
                        description = lesson_fields.get('description')
                        content = lesson_fields.get('content', {})  # Assuming content is directly from JSON

                        if module_id is None or title is None:
                            raise ValueError("Module ID and Title must be provided.")

                        lesson, created = Lesson.objects.update_or_create(
                            pk=lesson_data['pk'],  # Use 'pk' to uniquely identify lessons
                            defaults={
                                'module_id': module_id,
                                'title': title,
                                'description': description,
                                'content': content  # Assuming content is directly from JSON
                            }
                        )

                        if created:
                            self.stdout.write(self.style.SUCCESS(f'Lesson "{lesson.title}" created'))
                        else:
                            self.stdout.write(self.style.SUCCESS(f'Lesson "{lesson.title}" updated'))

                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'Failed to process lesson: {e}'))

                self.stdout.write(self.style.SUCCESS('Successfully populated lessons'))

        except FileNotFoundError:
            raise CommandError(f'File "{json_file}" does not exist')
