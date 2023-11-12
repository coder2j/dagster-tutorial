from dagster import asset, AssetExecutionContext


@asset
def my_first_asset(context: AssetExecutionContext):
    """
    This is our first asset for testing purposes
    """
    print("this is a print message.")
    context.log.info("this is a log message.")
    return [1, 2, 3]
