from app.util import common
import json as py_json
from flask import jsonify, request


def response_json(body=None):
    """
    * 返回Json数据
    * @param  dict body
    * @return json
    """
    if body is None:
        body = {}
    common.log().debug(
        py_json.dumps({
            'LOG_ID': common.unique_id(),
            'IP_ADDRESS': request.remote_addr,
            'REQUEST_URL': request.url,
            'REQUEST_METHOD': request.method,
            'PARAMETERS': request.args,
            'RESPONSES': body
        }))
    return jsonify(body)


def error(msg='', code=400):
    """
    返回错误信息
    :param  msg 错误提示
    :param  code 错误码
    :return json 返回的json字符串
    """
    return response_json({'code': code, 'error': True, 'msg': msg})


def success(data='', msg='ok', code=200):
    """
    返回成功信息
    :param  data 返回数据内容
    :param  msg 提示信息
    :param  code 状态码
    :return json 返回的json字符串
    """
    return response_json({'code': code, 'data': data, 'msg': msg})
