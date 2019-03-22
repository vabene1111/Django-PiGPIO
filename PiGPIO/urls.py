from django.urls import path

from .views import *


urlpatterns = [
    path('', views.index, name='index'),
    path('api/set', SetPinView.as_view(), name='api_set_pin'),
    path('api/run', RunProgramView.as_view(), name='api_run_prog'),

    path('api/edit/step', EditStepView.as_view(), name='api_edit_step'),
    path('api/new/step', NewStepView.as_view(), name='api_new_step'),


    path('program/<int:pk>/', views.program, name='program'),

    # New/Edit/Delete Views

    path('new/program/', new.ProgramCreate.as_view(), name='new_program'),

    path('list/program', lists.program, name='list_program'),

    path('edit/program/<int:pk>/', edit.ProgramUpdate.as_view(), name='edit_program'),

    path('delete/program/<int:pk>/', edit.ProgramDelete.as_view(), name='delete_program'),

    path('redirect/delete/<slug:name>/<int:pk>/', edit.delete_redirect, name='redirect_delete'),
]

