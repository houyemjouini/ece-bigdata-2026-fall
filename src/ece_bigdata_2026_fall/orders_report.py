import argparse
import os

import duckdb


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--product", default=None)
    args = parser.parse_args()

    bucket = os.environ["LAB_BUCKET_NAME"]

    con = duckdb.connect()

    query = """
        SELECT
            product,
            SUM(quantity) AS total_quantity
        FROM read_parquet(?)
    """

    params = [f"s3://{bucket}/large/orders_large.parquet"]

    if args.product:
        query += " WHERE product = ?"
        params.append(args.product)

    query += """
        GROUP BY product
        ORDER BY total_quantity DESC
    """

    result = con.execute(query, params).fetchall()

    for product, total_quantity in result:
        print(f"{product}: {total_quantity:,}")


if __name__ == "__main__":
    main()
