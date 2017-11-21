# -*- coding:utf-8 -*-
__author__ = 'yang_da'
__date__ = '2017/11/1 下午5:44'

import xadmin

import help_methods
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = help_methods.get_vars_list(CityDict())
    search_fields = help_methods.get_vars_not_time_list(CityDict())
    list_filter = help_methods.get_vars_list(CityDict())


class CourseOrgAdmin(object):
    list_display = help_methods.get_vars_list(CourseOrg())
    search_fields = help_methods.get_vars_not_time_list(CourseOrg())
    list_filter = help_methods.get_vars_list(CourseOrg())


class TeacherAdmin(object):
    list_display = help_methods.get_vars_list(Teacher())
    search_fields = help_methods.get_vars_not_time_list(Teacher())
    list_filter = help_methods.get_vars_list(Teacher())


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)