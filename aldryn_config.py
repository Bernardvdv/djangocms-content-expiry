from aldryn_client import forms


class Form(forms.BaseForm):
    def to_settings(self, data, settings):
        settings['INSTALLED_APPS'].extend([
            'djangocms_content_expiry',
            'rangefilter',
        ])
        settings["DJANGOCMS_CONTENT_EXPIRY_ENABLED"] = True
        return settings