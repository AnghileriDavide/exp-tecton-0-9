from tecton import RequestSource, on_demand_feature_view
from tecton.types import Field, Int64, String

user_age_request = RequestSource(
    schema=[
        Field("timestamp", String),
        Field("user_birth_date", String),
    ]
)


@on_demand_feature_view(
    sources=[user_age_request],
    mode="python",
    name="user_age:v1",
    schema=[Field("user_age", Int64)],
    owner="davide.anghileri@prima.it",
    tags={"release": "development"},
    description="Returns the age (int) of the user with respect to the timestamp",
)
def user_age(input_data):
    from datetime import datetime
    from dateutil.relativedelta import relativedelta

    birth_date = datetime.strptime(input_data["user_birth_date"], "%Y-%m-%d")
    timestamp = datetime.strptime(input_data["timestamp"], "%Y-%m-%dT%H:%M:%S")
    return {"user_age": relativedelta(timestamp, birth_date).years}