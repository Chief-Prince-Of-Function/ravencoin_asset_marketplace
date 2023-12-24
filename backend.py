import sqlite3

# Connect to SQLite database (this will create a new database if it doesn't exist)
conn = sqlite3.connect('liquidity_pool.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table for liquidity pool information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS liquidity_pool (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pool_name TEXT NOT NULL,
        asset_1 TEXT NOT NULL,
        asset_2 TEXT NOT NULL,
        liquidity_provider_address TEXT NOT NULL,
        liquidity_amount REAL NOT NULL
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

def add_liquidity_pool(pool_name, asset_1, asset_2, provider_address, liquidity_amount):
    conn = sqlite3.connect('liquidity_pool.db')
    cursor = conn.cursor()

    # Insert a new liquidity pool record
    cursor.execute('''
        INSERT INTO liquidity_pool (pool_name, asset_1, asset_2, liquidity_provider_address, liquidity_amount)
        VALUES (?, ?, ?, ?, ?)
    ''', (pool_name, asset_1, asset_2, provider_address, liquidity_amount))

    conn.commit()
    conn.close()

def redeem_liquidity(pool_name, redemption_amount):
    conn = sqlite3.connect('liquidity_pool.db')
    cursor = conn.cursor()

    # Retrieve the liquidity pool record
    cursor.execute('SELECT * FROM liquidity_pool WHERE pool_name = ?', (pool_name,))
    pool = cursor.fetchone()

    if pool:
        # Check if there is enough liquidity for redemption
        if pool[5] >= redemption_amount:
            # Perform redemption and update the liquidity pool record
            new_liquidity_amount = pool[5] - redemption_amount
            cursor.execute('''
                UPDATE liquidity_pool
                SET liquidity_amount = ?
                WHERE pool_name = ?
            ''', (new_liquidity_amount, pool_name))

            conn.commit()
            print(f"Redemption successful. Pool: {pool_name}, Redeemed Amount: {redemption_amount}")
        else:
            print("Insufficient liquidity for redemption.")
    else:
        print(f"Liquidity pool '{pool_name}' not found.")

    conn.close()

def retrieve_liquidity_pools():
    conn = sqlite3.connect('liquidity_pool.db')
    cursor = conn.cursor()

    # Retrieve all liquidity pool records
    cursor.execute('SELECT * FROM liquidity_pool')
    pools = cursor.fetchall()

    conn.close()
    return pools

# Example: Add liquidity pool information
add_liquidity_pool('Pool1', 'RVN', 'USD', 'provider_address_1', 1000.0)
add_liquidity_pool('Pool2', 'RVN', 'BTC', 'provider_address_2', 500.0)

# Example: Redeem liquidity
redeem_liquidity('Pool1', 200.0)

# Example: Retrieve all liquidity pools
all_pools = retrieve_liquidity_pools()
print("\nAll Liquidity Pools:")
for pool in all_pools:
    print(pool)
