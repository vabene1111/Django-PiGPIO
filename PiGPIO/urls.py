from django.urls import path

from .views import *


urlpatterns = [
    path('', views.index, name='index'),

    path('test', views.test, name='test'),
    path('blocky', views.blockly, name='blocky'),

    path('api/set', SetPinView.as_view(), name='api_set_pin'),

    path('api/run', RunProgramView.as_view(), name='api_run_prog'),
    path('api/run/old', RunProgramOldView.as_view(), name='api_run_prog_old'),
    path('api/delete/step', StopProgramView.as_view(), name='api_stop_prog'),

    path('api/edit/program', EditProgramView.as_view(), name='api_edit_program'),
    path('api/edit/step', EditStepView.as_view(), name='api_edit_step'),

    path('api/new/step', NewStepView.as_view(), name='api_new_step'),
    path('api/delete/step', DeleteStepView.as_view(), name='api_delete_step'),

    path('program/<int:pk>/', views.blockly, name='program'),
    path('program/old/<int:pk>/', views.program, name='program_old'),

    # New/Edit/Delete Views

    path('new/program/', new.ProgramCreate.as_view(), name='new_program'),

    path('list/program', lists.program, name='list_program'),

    path('edit/program/<int:pk>/', edit.ProgramUpdate.as_view(), name='edit_program'),

    path('delete/program/<int:pk>/', edit.ProgramDelete.as_view(), name='delete_program'),

    path('redirect/delete/<slug:name>/<int:pk>/', edit.delete_redirect, name='redirect_delete'),
]

