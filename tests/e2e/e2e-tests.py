name: e2e tests

on:
  push:
    branches:
      - main
    paths-ignore:
      - '**.md'
  pull_request:
    paths-ignore:
      - '**.md'
  workflow_dispatch:

jobs:
  test-setup-python:
    name: Test setup-python
    runs-on: ${{ matrix.operating-system }}
    strategy:
      matrix:
        operating-system:
          [
            ubuntu-22.04,
            windows-latest,
            macos-latest
          ]
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python 3.13
        uses: actions/setup-python@v4
        with:
          python-version: 3.13
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: |
          pytest tests/
      - name: Verify Python version
        run: python -c "import sys; assert sys.version_info[:2] == (3, 9)"

  test-setup-node:
    name: Test setup-node
    runs-on: ${{ matrix.operating-system }}
    strategy:
      matrix:
        operating-system:
          [
            ubuntu-22.04,
            windows-latest,
            macos-latest
          ]
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 16
      - name: Install dependencies
        run: npm install
      - name: Run tests
        run: npm test
      - name: Verify Node version
        run: node -v
- name: Install system dependencies
  run: sudo apt-get install -y libpq-dev build-essential
  - name: Cache dependencies
  uses: actions/cache@v3
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-
      env:
  DATABASE_URL: ${{ secrets.DATABASE_URL }}
  SECRET_KEY: ${{ secrets.SECRET_KEY }}
  - name: Retry dependency installation
  run: pip install -r requirements.txt || pip install -r requirements.txt
