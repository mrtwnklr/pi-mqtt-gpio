from __future__ import print_function

from pi_mqtt_gpio.modules import GenericGPIO

CONFIG_SCHEMA = {
    "output_get": {
        "type": "boolean",
        "required": False,
        "empty": False,
        "default": True
    }
}

class GPIO(GenericGPIO):
    """
    Implementation of GPIO class for outputting to STDIO.
    """

    def __init__(self, config):
        print("__init__(config=%r)" % config)

        self.output_get = config["output_get"]

    def setup_pin(self, pin, direction, pullup, pin_config):
        print(
            "setup_pin(pin=%r, direction=%r, pullup=%r, pin_config=%r)"
            % (pin, direction, pullup, pin_config)
        )
        initial = pin_config.get("initial")
        if initial is not None:
            if initial == "high":
                self.set_pin(pin, True)
            elif initial == "low":
                self.set_pin(pin, False)

    def set_pin(self, pin, value):
        print("set_pin(pin=%r, value=%r)" % (pin, value))

    def get_pin(self, pin):
        if self.output_get:
            print("get_pin(pin=%r)" % pin)
        return False
