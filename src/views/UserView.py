from flask import request
from flask_restful import Resource

from src.tests.TestDatas import datas
from src.utils.Result import success


class UserView(Resource):
    """
    通过继承 Resource 来实现调用 GET/POST 等动作方法
    """

    def get(self):
        """
        GET 请求
        :return:
        """
        name = request.args.get("name")
        return success(message='hi {}'.format(name), data=datas)

    def post(self):
        # 参数数据
        json_data = request.get_json()

        # 追加数据到列表中
        new_id = len(datas) + 1
        datas.append({'id': new_id, **json_data})

        # 返回新增的最后一条数据
        return success(message='ok', data=datas[new_id - 1])
