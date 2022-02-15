# Copyright 2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_ui.helpers.service import BaseConfdService


class TransportService(BaseConfdService):
    resource_confd = 'sip_transports'

    def __init__(self, confd_client):
        self._confd = confd_client
