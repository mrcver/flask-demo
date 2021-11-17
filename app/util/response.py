from app.util import common


def error(msg='', code=400):
    """
    返回错误信息
    :param  msg 错误提示
    :param  code 错误码
    :return json 返回的json字符串
    """
    return common.json({'code': code, 'error': True, 'msg': msg})


def success(data='', msg='ok', code=200):
    """
    返回成功信息
    :param  data 返回数据内容
    :param  msg 提示信息
    :param  code 状态码
    :return json 返回的json字符串
    """
    return common.json({'code': code, 'data': data, 'msg': msg})
