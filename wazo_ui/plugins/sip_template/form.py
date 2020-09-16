# Copyright 2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_babel import lazy_gettext as l_
from wtforms.fields import (
    FieldList,
    FormField,
    HiddenField,
    SelectField,
    SelectMultipleField,
    StringField,
    SubmitField,
)
from wtforms.validators import InputRequired, Length

from wazo_ui.helpers.form import BaseForm


class TransportForm(BaseForm):
    uuid = SelectField(l_('Transport'), choices=[])
    name = HiddenField()


class TemplateForm(BaseForm):
    uuid = HiddenField()


class BasePJSIPOptionsForm(BaseForm):
    def to_dict(self):
        return super().to_dict(empty_string=True)

    option_key = SelectField(choices=[], validators=[InputRequired()])
    option_value = StringField()


class IdentifyPJSIPOptionsForm(BasePJSIPOptionsForm):
    option_key = SelectField(
        choices=[
            ('match', 'match'),
            ('endpoint', 'endpoint'),
            ('srv_lookups', 'srv_lookups'),
            ('match_header', 'match_header'),
        ],
        validators=[InputRequired()]
    )


class RegistrationPJSIPOptionsForm(BasePJSIPOptionsForm):
    option_key = SelectField(
        choices=[
            ('contact_header_params', 'contact_header_params'),
            ('forbidden_retry_interval', 'forbidden_retry_interval'),
            ('fatal_retry_interval', 'fatal_retry_interval'),
            ('line', 'line'),
            ('support_path', 'support_path'),
            ('support_outbound', 'support_outbound'),
            ('auth_rejection_permanent', 'auth_rejection_permanent'),
            ('client_uri', 'client_uri'),
            ('contact_user', 'contact_user'),
            ('expiration', 'expiration'),
            ('max_retries', 'max_retries'),
            ('outbound_proxy', 'outbound_proxy'),
            ('retry_interval', 'retry_interval'),
            ('server_uri', 'server_uri'),
            ('transport', 'transport'),
        ],
        validators=[InputRequired()]
    )


class EndpointSIPForm(BaseForm):
    uuid = HiddenField()
    label = StringField(l_('Label'), [Length(max=128)])
    name = StringField(l_('Name'), [Length(max=128)])
    aor_section_options = FieldList(FormField(BasePJSIPOptionsForm))
    auth_section_options = FieldList(FormField(BasePJSIPOptionsForm))
    endpoint_section_options = FieldList(FormField(BasePJSIPOptionsForm))
    identify_section_options = FieldList(FormField(IdentifyPJSIPOptionsForm))
    registration_section_options = FieldList(FormField(RegistrationPJSIPOptionsForm))
    registration_outbound_auth_section_options = FieldList(FormField(BasePJSIPOptionsForm))
    outbound_auth_section_options = FieldList(FormField(BasePJSIPOptionsForm))
    transport = FormField(TransportForm)
    template_uuids = SelectMultipleField(l_('Parent Templates'), choices=[])
    templates = FieldList(FormField(TemplateForm))
    submit = SubmitField()
