# -*- coding:utf-8 -*-
__author__ = 'yang_da'
__date__ = '2017/11/8 上午9:36'

import xadmin

from .models import UserAsk, UserCourse, UserMessage, CourseComments, UserFavorate
import help_methods


class UserAskAdmin(object):
    lis_display = help_methods.get_vars_list(UserAsk())
    search_fields = help_methods.get_vars_not_time_list(UserAsk())
    list_filter = help_methods.get_vars_list(UserAsk())


class UserCourseAdmin(object):
    lis_display = help_methods.get_vars_list(UserCourse())
    search_fields = help_methods.get_vars_not_time_list(UserCourse())
    list_filter = help_methods.get_vars_list(UserCourse())


class UserMessageAdmin(object):
    lis_display = help_methods.get_vars_list(UserMessage())
    search_fields = help_methods.get_vars_not_time_list(UserMessage())
    list_filter = help_methods.get_vars_list(UserMessage())


class CourseCommentsAdmin(object):
    lis_display = help_methods.get_vars_list(CourseComments())
    search_fields = help_methods.get_vars_not_time_list(CourseComments())
    list_filter = help_methods.get_vars_list(CourseComments())


class UserFavoriteAdmin(object):
    lis_display = help_methods.get_vars_list(UserFavorate())
    search_fields = help_methods.get_vars_not_time_list(UserFavorate())
    list_filter = help_methods.get_vars_list(UserFavorate())


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorate, UserFavoriteAdmin)