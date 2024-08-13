import pytest

from exp_tecton.features.user_age import user_age


@pytest.mark.parametrize(
    "input_data,expected",
    [
        (
            {
                "timestamp": "2022-04-04T04:04:04",
                "user_birth_date": "1980-01-01",
            },
            {"user_age": 42},
        ),
        (
            {
                "timestamp": "1999-04-04T04:04:04",
                "user_birth_date": "1999-01-01",
            },
            {"user_age": 0},
        ),
    ],
)
def test_user_age(input_data, expected):
    actual = user_age.run_transformation({"input_data": input_data})
    assert actual == expected


@pytest.mark.parametrize(
    "quote_dates",
    [
        (
            {
                "timestamp": None,
                "user_birth_date": "2000-02-02",
            },
        ),
        (
            {
                "timestamp": None,
                "user_birth_date": None,
            },
        ),
    ],
)
def test_user_age_fails(quote_dates):
    with pytest.raises((ValueError, TypeError)):
        user_age.run_transformation({"input_data": quote_dates})
