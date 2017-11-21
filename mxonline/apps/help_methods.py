# -*- coding:utf-8 -*-
__author__ = 'yang_da'
__date__ = '2017/11/1 下午3:29'

import copy

def get_vars_list(instance):
    vars_list = vars(instance).keys()
    for var_key in copy.deepcopy(vars_list):
        if var_key.startswith('_') or var_key.startswith('__'):
            vars_list.remove(var_key)

        if var_key.find('id') != -1:
            vars_list.remove(var_key)

    return vars_list


def get_vars_not_time_list(instance):
    vars_list = vars(instance).keys()
    for var_key in copy.deepcopy(vars_list):
        if var_key.startswith('_') or var_key.startswith('__'):
            vars_list.remove(var_key)

        if var_key.find('id') != -1:
            vars_list.remove(var_key)

        if var_key.find('time') != -1:
            vars_list.remove(var_key)
    return vars_list


