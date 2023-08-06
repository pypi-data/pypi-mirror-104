from urllib.parse import urljoin, urlparse

import requests
import json

from .const import API_BASE, API_GET_DATASHEET_QS_SET, DEFAULT_PAGE_SIZE
from .datasheet import Datasheet
from .exceptions import ErrorSortParams
from .vika_type import RawGETResponse


class Vika:
    def __init__(self, token, **kwargs):
        self.request = requests.Session()
        self.auth(token)
        self._api_base = API_BASE

    @property
    def api_base(self):
        return self._api_base

    def set_api_base(self, api_base):
        self._api_base = api_base

    def set_request(self, config):
        # TODO  配置 request 请求（timeout）
        pass

    def auth(self, token):
        self.request.headers.update({"Authorization": f"Bearer {token}"})

    def datasheet(self, dst_id_or_url, **kwargs):
        if dst_id_or_url.startswith("dst"):
            dst_id = dst_id_or_url
        elif dst_id_or_url.startswith("http"):
            url = urlparse(dst_id_or_url)
            url_path_list = url.path.split("/")
            dst_id = url_path_list[-2]
            view_id = url_path_list[-1]
            if view_id and view_id.startswith("viw"):
                kwargs.update({"viewId": view_id})
        else:
            raise Exception("Bad URL")
        return Datasheet(self, dst_id, records=[], **kwargs)

    @staticmethod
    def check_sort_params(sort):
        if not isinstance(sort, list):
            return False
        return all([('field' in i and 'order' in i) for i in sort])

    def fetch_datasheet(self, dst_id, **kwargs):
        params = {}
        for key in kwargs:
            if key in API_GET_DATASHEET_QS_SET:
                params_value = kwargs.get(key)
                if key == 'sort':
                    if self.check_sort_params(params_value):
                        params_value = [json.dumps(i) for i in params_value]
                    else:
                        raise ErrorSortParams('sort 参数格式有误')
                params.update({key: params_value})
        resp = self.request.get(
            urljoin(self.api_base, f"/fusion/v1/datasheets/{dst_id}/records"),
            params=params,
        ).json()
        resp = RawGETResponse(**resp)
        return resp

    def fetch_datasheet_all(self, dst_id, **kwargs):
        """
        不主动传入 pageSize 和 pageNum 时候，主动加载全部记录。
        """
        page_size = kwargs.get("pageSize", DEFAULT_PAGE_SIZE)
        page_num = kwargs.get("pageNum", 1)
        page_params = {"pageSize": page_size, "pageNum": page_num}
        kwargs.update(page_params)
        records = []
        resp = self.fetch_datasheet(dst_id, **kwargs)
        if resp.success:
            records += resp.data.records
            current_total = page_size * page_num
            if current_total < resp.data.total:
                kwargs.update({"pageNum": page_num + 1})
                records += self.fetch_datasheet_all(dst_id, **kwargs)
        else:
            print(f"[{dst_id}] get page:{page_num} fail\n {resp.message}")
        return records
