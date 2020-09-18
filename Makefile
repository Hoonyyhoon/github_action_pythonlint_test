format:
	black .
	isort . -rc

test:
	black .
	isort . -rc
	env PYTHONPATH=. pytest --pylint --flake8 --mypy
