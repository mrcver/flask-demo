import cerberus
from flask import request
from app.util.exception import CustomErrorHandlers
from app.util.common import json


def validateInput(rules, error_msg=None):
    """
    参数校验方法
    :param rules: 校验规则
    :param error_msg: 返回的错误信息
    :return:
    """
    v = cerberus.Validator(rules, error_handler=CustomErrorHandlers(custom_messages=error_msg))
    # v = ObjectValidator(rules)
    # 这边修改成json格式接收参数
    requests = request.get_json()
    if v.validate(requests):  # validate
        return True
    error = {'msg': v.errors, 'error_code': 400, 'error': True}
    return json(error)
