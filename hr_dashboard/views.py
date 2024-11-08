from django.shortcuts import render, redirect, get_object_or_404
from role_customization.models import Role, Criteria, LinkedAssessment
from role_customization.forms import RoleForm, CriteriaForm, AssessmentForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CriteriaSerializer


def hr_dashboard(request):
    return render(request, 'hr_dashboard/index.html')


def role_list(request):
    roles = Role.objects.all()
    return render(request, 'role_customization/role_list.html', {'roles': roles})


def role_create(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('role_list')
    else:
        form = RoleForm()
    return render(request, 'role_customization/role_form.html', {'form': form})


def role_update(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('role_list')
    else:
        form = RoleForm(instance=role)
    return render(request, 'role_customization/role_form.html', {'form': form})


def role_delete(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        role.delete()
        return redirect('role_list')
    return render(request, 'role_customization/role_confirm_delete.html', {'role': role})


def criteria_list(request):
    criteria = Criteria.objects.all()
    return render(request, 'role_customization/criteria_list.html', {'criteria': criteria})


def criteria_create(request):
    if request.method == 'POST':
        form = CriteriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('criteria_list')
    else:
        form = CriteriaForm()
    return render(request, 'role_customization/criteria_form.html', {'form': form})


def criteria_update(request, pk):
    criteria = get_object_or_404(Criteria, pk=pk)
    if request.method == 'POST':
        form = CriteriaForm(request.POST, instance=criteria)
        if form.is_valid():
            form.save()
            return redirect('criteria_list')
    else:
        form = CriteriaForm(instance=criteria)
    return render(request, 'role_customization/criteria_form.html', {'form': form})


def criteria_delete(request, pk):
    criteria = get_object_or_404(Criteria, pk=pk)
    if request.method == 'POST':
        criteria.delete()
        return redirect('criteria_list')
    return render(request, 'role_customization/criteria_confirm_delete.html', {'criteria': criteria})


def linked_assessment_list(request):
    linked_assessments = LinkedAssessment.objects.all()
    return render(request, 'role_customization/linked_assessment_list.html', {'linked_assessments': linked_assessments})


def linked_assessment_create(request):
    if request.method == 'POST':
        form = AssessmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('linked_assessment_list')
    else:
        form = AssessmentForm()
    return render(request, 'role_customization/linked_assessment_form.html', {'form': form})


def linked_assessment_update(request, pk):
    linked_assessment = get_object_or_404(LinkedAssessment, pk=pk)
    if request.method == 'POST':
        form = AssessmentForm(request.POST, instance=linked_assessment)
        if form.is_valid():
            form.save()
            return redirect('linked_assessment_list')
    else:
        form = AssessmentForm(instance=linked_assessment)
    return render(request, 'role_customization/linked_assessment_form.html', {'form': form})


def linked_assessment_delete(request, pk):
    linked_assessment = get_object_or_404(LinkedAssessment, pk=pk)
    if request.method == 'POST':
        linked_assessment.delete()
        return redirect('linked_assessment_list')
    return render(request, 'role_customization/linked_assessment_confirm_delete.html', {'linked_assessment': linked_assessment})


@api_view(['GET', 'POST'])
def criteria_data(request):
    if request.method == 'GET':
        criteria = Criteria.objects.all()
        serializer = CriteriaSerializer(criteria, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CriteriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
