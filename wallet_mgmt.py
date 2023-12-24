from rvn_python import Ravencoin

# Initialize connection to RavenCoin Core wallet
rpc_user = 'your_rpc_user'
rpc_password = 'your_rpc_password'
rpc_port = '8766'  # Default port for RavenCoin Core
rpc_connection = Ravencoin(rpc_user, rpc_password, port=rpc_port)

def create_asset(asset_name, quantity, reissuable=False):
    # Create a new asset
    result = rpc_connection.issue(asset_name, quantity, reissuable)
    return result

def transfer_asset(asset_name, to_address, quantity):
    # Transfer asset to another address
    result = rpc_connection.sendasset(to_address, {asset_name: quantity})
    return result

if __name__ == "__main__":
    # Example: Create an asset
    asset_name = "MyToken"
    quantity = 1000
    create_result = create_asset(asset_name, quantity)
    print(f"Asset creation result: {create_result}")

    # Example: Transfer asset
    to_address = "recipient_address"
    transfer_result = transfer_asset(asset_name, to_address, quantity)
    print(f"Asset transfer result: {transfer_result}")
