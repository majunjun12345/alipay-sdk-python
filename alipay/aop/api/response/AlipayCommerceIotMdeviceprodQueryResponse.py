#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantModel import MerchantModel
from alipay.aop.api.domain.MerchantModel import MerchantModel


class AlipayCommerceIotMdeviceprodQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotMdeviceprodQueryResponse, self).__init__()
        self._activate_time = None
        self._biz_type = None
        self._device_name = None
        self._device_sn = None
        self._img_url = None
        self._isv = None
        self._merchant = None
        self._status = None
        self._status_desc = None
        self._supplier_name = None

    @property
    def activate_time(self):
        return self._activate_time

    @activate_time.setter
    def activate_time(self, value):
        self._activate_time = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def device_name(self):
        return self._device_name

    @device_name.setter
    def device_name(self, value):
        self._device_name = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, value):
        self._img_url = value
    @property
    def isv(self):
        return self._isv

    @isv.setter
    def isv(self, value):
        if isinstance(value, MerchantModel):
            self._isv = value
        else:
            self._isv = MerchantModel.from_alipay_dict(value)
    @property
    def merchant(self):
        return self._merchant

    @merchant.setter
    def merchant(self, value):
        if isinstance(value, MerchantModel):
            self._merchant = value
        else:
            self._merchant = MerchantModel.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_desc(self):
        return self._status_desc

    @status_desc.setter
    def status_desc(self, value):
        self._status_desc = value
    @property
    def supplier_name(self):
        return self._supplier_name

    @supplier_name.setter
    def supplier_name(self, value):
        self._supplier_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotMdeviceprodQueryResponse, self).parse_response_content(response_content)
        if 'activate_time' in response:
            self.activate_time = response['activate_time']
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'device_name' in response:
            self.device_name = response['device_name']
        if 'device_sn' in response:
            self.device_sn = response['device_sn']
        if 'img_url' in response:
            self.img_url = response['img_url']
        if 'isv' in response:
            self.isv = response['isv']
        if 'merchant' in response:
            self.merchant = response['merchant']
        if 'status' in response:
            self.status = response['status']
        if 'status_desc' in response:
            self.status_desc = response['status_desc']
        if 'supplier_name' in response:
            self.supplier_name = response['supplier_name']
