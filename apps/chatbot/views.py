# import openai
# from django.shortcuts import render
# from django.views import View
# from django.conf import settings

# class GenerateExerciseView(View):
#     template_name = 'generate_exercise.html'

#     def get(self, request):
#         return render(request, self.template_name)

#     def post(self, request):
#         openai.api_key = settings.OPENAI_API_KEY

#         # Example prompt to generate a JavaScript exercise
#         prompt = "Generate a JavaScript exercise for beginners."

#         # Use openai.Completion.create() to generate exercise
#         response = openai.Completion.create(
#             engine="text-davinci-003",
#             prompt=prompt,
#             max_tokens=150
#         )

#         exercise = {
#             "question": response["choices"][0]["text"].strip(),
#             "hint1": "Hint 1: Remember to use proper syntax.",
#             "hint2": "Hint 2: Think about the problem-solving steps."
#         }

#         return render(request, self.template_name, {"exercise": exercise})


# views.py
from django.shortcuts import render
from .api_utils import generate_exercise, generate_hint

def exercise_view(request):
    prompt = "Generate an exercise for JavaScript basics."
    exercise = generate_exercise(prompt)
    hint = generate_hint("Provide a hint for the exercise.")

    context = {
        'exercise': exercise,
        'hint': hint
    }

    return render(request, 'generate_exercise.html', context)
