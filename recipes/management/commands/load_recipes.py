import json
from django.core.management.base import BaseCommand
from recipes.models import Recipe

class Command(BaseCommand):
    help = 'Load recipes from JSON file into the database'

    def handle(self, *args, **kwargs):
        import json

        try:
            with open('recipes/US_recipes_null.json', encoding='utf-8') as f:
                data_dict = json.load(f)  # This gives you a dictionary

            if not isinstance(data_dict, dict):
                raise ValueError("Expected a dictionary of recipe entries")

            print(f"✅ Loaded {len(data_dict)} recipes from JSON.")

        except Exception as e:
            self.stderr.write(f"❌ Error reading JSON file: {e}")
            return

        success = 0

        for key, item in data_dict.items():
            try:
                title = item.get('title')
                if not title:
                    print(f"⚠️ Skipping recipe {key} — missing title.")
                    continue  # Skip this item
                Recipe.objects.create(
                    cuisine=item.get('cuisine', ''),
                    title=title,
                    rating=item.get('rating') or 0.0,
                    prep_time=item.get('prep_time') or 0,
                    cook_time=item.get('cook_time') or 0,
                    total_time=item.get('total_time') or 0,
                    description=item.get('description', ''),
                    nutrients=item.get('nutrients', {}),
                    serves=item.get('serves', '')
                )
                success += 1

            except Exception as e:
                self.stderr.write(f"⚠️ Failed to save recipe {key}: {e}")

        self.stdout.write(self.style.SUCCESS(f"✅ Successfully saved {success} recipes to the database."))
