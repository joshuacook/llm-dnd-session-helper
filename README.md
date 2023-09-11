# LLDM

## Working with DB

1. add a model to the models dir
2. import the model in the alembic/env.py file
3. run `alembic revision --autogenerate -m "Description of the migration"`
4. run `alembic upgrade head`