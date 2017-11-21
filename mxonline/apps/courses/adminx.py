# -*- coding:utf-8 -*-
__author__ = 'yangda'
__date__ = '2017/11/1 下午2:11'

import xadmin

from .models import Courses, Lesson, Video, CourseResource
import help_methods


class CoursesAdmin(object):
    list_display = help_methods.get_vars_list(Courses())
    search_fields = help_methods.get_vars_not_time_list(Courses())
    list_filter = help_methods.get_vars_list(Courses())


class LessonAdmin(object):
    list_display = help_methods.get_vars_list(Lesson())
    search_fields = help_methods.get_vars_not_time_list(Lesson())

    list_filter = help_methods.get_vars_list(Lesson())
    list_filter.append('course__name')


class VideoAdmin(object):
    list_display = help_methods.get_vars_list(Video())
    search_fields = help_methods.get_vars_not_time_list(Video())
    list_filter = help_methods.get_vars_list(Video())


class CourseResourceAdmin(object):
    list_display = help_methods.get_vars_list(CourseResource())
    search_fields = help_methods.get_vars_not_time_list(CourseResource())
    list_filter = help_methods.get_vars_list(CourseResource())


xadmin.site.register(Courses, CoursesAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)