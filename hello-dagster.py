from typing import List
from dagster import asset, AssetExecutionContext, AssetIn


@asset(key="my_awesome_first_asset", group_name="get_started")
def my_first_asset(context: AssetExecutionContext):
    """
    This is our first asset for testing purposes
    """
    print("this is a print message.")
    context.log.info("this is a log message.")
    return [1, 2, 3]


@asset(ins={"upstream": AssetIn(key="my_awesome_first_asset")}, group_name="get_started")
def my_second_asset(context: AssetExecutionContext, upstream: List):
    """
    This is our second asset
    """
    data = upstream + [4, 5, 6]
    context.log.info(f"Output data is: {data}")
    return data


@asset(ins={
    "first_upstream": AssetIn("my_awesome_first_asset"),
    "second_upstream": AssetIn("my_second_asset")
}, group_name="get_started")
def my_third_asset(
    context: AssetExecutionContext,
    first_upstream: List,
    second_upstream: List):
    """
    This is our third asset
    """
    data = {
        "first_asset": first_upstream,
        "second_asset": second_upstream,
        "third_asset": second_upstream + [7, 8]
    }
    context.log.info(f"Output data is: {data}")
    return data
