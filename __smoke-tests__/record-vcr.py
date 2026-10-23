"""VCR runner for tap-acumatica smoke tests."""

from typing import ClassVar

from hotglue_smoke_test.vcr.tap import VCRTapTestRunner


class ConnectorTapTestRunner(VCRTapTestRunner):
    # Entity discovery reads `name` and `version` into the next request URL.
    # Token refresh reads relative `expires_in` and adds it to the current clock.
    PRESERVE_KEYS: ClassVar[set[str]] = {
        "expires_in",
        "name",
        "version",
    }

    def module(self) -> str:
        return "tap_acumatica.tap"

    def launch(self):
        from tap_acumatica.tap import TapAcumatica

        TapAcumatica.cli()


if __name__ == "__main__":
    ConnectorTapTestRunner.main()
