'''from my_project.weather import check_weather
# passed
def test_check_weather():
    assert check_weather(21.00) == "hot", 'temperatures greater than 20 degree \
must be considered as hot' '''



'''from my_project.weather import check_weather'''
# failed
'''def test_check_weather():
    assert check_weather(5.00) == "average", 'temperatures between 10 and 20 degree \
must be considered as average temperature' '''

# passed
'''def test_check_weather1():
    assert check_weather(21.00) == "hot", 'temperatures greater than 20 degree \
must be considered as hot'

# failed
def test_check_weather2():
    assert check_weather(5.00) == "average", 'temperatures greater than 20 degree \
must be considered as hot'

# passed
def test_check_weather3():
    assert check_weather(5.00) == "cold", 'temperatures greater than 20 degree \
must be considered as hot'

# passed
def test_check_weather4():
    assert check_weather(13.00) == "average", 'temperatures greater than 20 degree \
must be considered as hot'

#failed because every def test_function() is cosidored as a single test
def test_check_weather():
    assert check_weather(30.00) == "hot", "temperaturs grater than 20 degree must be considered as hot"
    assert check_weather(11.00) == "cold", "temperaturs lower than 10 degree must be considered as cold" '''

from my_project.weather import check_weather
import pytest
@pytest.mark.parametrize("temperature, expected", [
(21.00, "hot"),
(13.00, "average"),
(0.00, "cold"),
(15.00, "cold")
])
def test_check_weather(temperature, expected):
    ae: str = ""
    if temperature > 20:
        ae = "temperaturs grater than 20 degree must be considered as hot"
    elif 10 < temperature <= 20:
        ae = "temperaturs must be considered as average temperature"
    else:
        ae = "temperaturs lower than 10 degree must be considered as cold"
    assert check_weather(temperature) == expected, ae




