from netbox.forms import NetBoxModelForm
from .models import Settings


class SettingsForm(NetBoxModelForm):
    class Meta:
        model = Settings
        fields = [
            "hostname",
            "username",
            "password",
            "version",
            "verify",
            "status",
        ]
        widgets = {
            "status": BootstrapMixin (
                choices=(
                    ("True", "Yes"),
                    ("False", "No"),
                )
            ),
            "verify": BootstrapMixin (
                choices=(
                    (True, "Yes"),
                    (False, "No"),
                )
            ),
        }
