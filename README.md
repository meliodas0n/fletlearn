# Chrono

Chrono is an amazing todo + tracking app that is going to surpass Jira in a few thousand years.

## How to Install
1. Install python3.11 and venv 
    ```shell
    sudo apt install python3.11 python3.11-venv
    ```

2. Create a virtual environment:
    ```shell
    python3.11 -m venv .venv
    ```

3. Activate the newly created environment:
    ```shell
    source ./.venv/bin/activate
    ```

4. Install poetry:
    ```shell
    pip3 install poetry
    ```

5. Install required dependencies using poetry:
    ```shell
    poetry install
    ```

6. To run tests:
    ```shell
    cd chrono; python3.11 -m unittest test_app.py
    ```

7. Run the app:
    ```shell
    python3.11 chrono
    ```
