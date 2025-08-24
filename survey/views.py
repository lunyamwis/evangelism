from django.shortcuts import render, get_object_or_404, redirect
from .models import Survey, Question, Response, Answer
from .forms import SurveyForm, QuestionForm, ResponseForm, AnswerForm
from django.forms import modelformset_factory

def survey_list(request):
    surveys = Survey.objects.all()
    return render(request, 'survey/survey_list.html', {'surveys': surveys})

def survey_detail(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    questions = survey.questions.all()

    if request.method == 'POST':
        response = Response.objects.create(survey=survey)
        for question in questions:
            answer_text = request.POST.get(f'question_{question.id}', '')
            Answer.objects.create(response=response, question=question, answer_text=answer_text)
        return redirect('survey_thankyou')

    return render(request, 'survey/survey_detail.html', {'survey': survey, 'questions': questions})

def survey_create(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey = form.save()
            return redirect('survey_add_questions', survey_id=survey.id)
    else:
        form = SurveyForm()
    return render(request, 'survey/survey_create.html', {'form': form})

def survey_add_questions(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    QuestionFormSet = modelformset_factory(Question, form=QuestionForm, extra=5)
    if request.method == 'POST':
        formset = QuestionFormSet(request.POST, queryset=Question.objects.filter(survey=survey))
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.survey = survey
                instance.save()
            return redirect('survey_list')
    else:
        formset = QuestionFormSet(queryset=Question.objects.filter(survey=survey))
    return render(request, 'survey/survey_add_questions.html', {'survey': survey, 'formset': formset})

def survey_thankyou(request):
    return render(request, 'survey/thank_you.html')
