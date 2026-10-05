# Dataset generator

This project generates a random dataset consisting of users and orders. Scripts are written in Python and the project uses [uv](https://docs.astral.sh/uv/).

## Usage

The project provides two commands to generate datasets:

* `dataset-users` generates random users.
* `dataset-orders` generates random orders associated with users.

The generated datasets can be exported as CSV, JSON or JSON Lines.

### Generate users

Generate 10 users:

```
uv run python -m ece_bigdata_2026_fall.dataset_users -c 10
```

Generate users as CSV:

```
uv run python -m ece_bigdata_2026_fall.dataset_users -c 10 -o csv
```

Generate users as JSON Lines:

```
uv run python -m ece_bigdata_2026_fall.dataset_users -c 10 -o jsonline
```

### Generate orders

Generate orders for 2 users, with 1 to 2 orders per user:

```
uv run python -m ece_bigdata_2026_fall.dataset_orders -u 2 -C 1 -c 2
```

Generate orders as CSV:

```
uv run python -m ece_bigdata_2026_fall.dataset_orders -u 2 -C 1 -c 2 -o csv
```

Generate orders as JSON Lines:

```
uv run python -m ece_bigdata_2026_fall.dataset_orders -u 2 -C 1 -c 2 -o jsonline
```
