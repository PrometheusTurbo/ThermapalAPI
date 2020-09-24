import re


class Temperature:

    def __init__(self, string):
        self.string = string

    def wrapper(self):
        get_temperature = self._locate_temperature()
        temperature_int = int(get_temperature.split()[0])
        b_format_temperature_int = self._to_binary(temperature_int)
        i_format_temperature_int = self._grab_temperature(b_format_temperature_int)
        return f"{i_format_temperature_int}.{get_temperature.split()[1]}"

    def _locate_temperature(self):
        match_object = re.search(r"0 5 (\d+ \d+)", self.string)
        return match_object.group(1)

    def _to_binary(self, number):
        output = f"{number:b}"
        while len(output) < 8:
            output = "0" + output
        return output

    def _grab_temperature(self, decimal_string):
        temperature = decimal_string[2:]
        return int(temperature, 2)
