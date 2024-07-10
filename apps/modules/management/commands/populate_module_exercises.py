import json
from django.core.management.base import BaseCommand
from apps.modules.models import ModuleExercise, Module

class Command(BaseCommand):
    help = 'Load module exercises from a JSON file'

    def handle(self, *args, **kwargs):
        fixture_file = 'fixtures/module_exercise.json'
        
        try:
            with open(fixture_file, 'r') as file:
                exercises = json.load(file)
            
            for exercise in exercises:
                module_id = exercise['fields']['module_id']  # Correctly access 'module_id'
                
                # Ensure module_id exists in Module table
                try:
                    module = Module.objects.get(id=module_id)
                except Module.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Module with id {module_id} does not exist. Skipping exercise creation.'))
                    continue
                
                # Create ModuleExercise instance
                ModuleExercise.objects.create(
                    id=exercise['pk'],  # Assuming 'pk' is the primary key in your JSON
                    module=module,
                    title=exercise['fields']['title'],
                    content=exercise['fields']['content'],
                    number_of_attempts=exercise['fields']['number_of_attempts'],
                    number_of_hints=exercise['fields']['number_of_hints'],
                    hints=exercise['fields']['hints']
                )
            
            self.stdout.write(self.style.SUCCESS('Successfully loaded module exercises'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'Fixture file not found: {fixture_file}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Invalid JSON format in the fixture file'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to load module exercises: {e}'))
