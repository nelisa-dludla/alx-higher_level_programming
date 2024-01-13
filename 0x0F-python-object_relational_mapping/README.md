# 0x0F. Python - Object-relational mapping

This directory serves as my first introduction to object-relational mapping

### Task 0: Get all states
- **File:** `0-select_states.py`
- **Description:** Write a script that lists all `states` from the database `hbtn_0e_0_usa`

### Task 1: Filter states
- **File:** `1-filter_states.py`
- **Description:** Write a script that lists all `states` with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`

### Task 2: Filter states by user input 
- **File:** `2-my_filter_states.py`
- **Description:** Write a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument

### Task 3: SQL Injection...
- **File:** `3-my_safe_filter_states.py`
- **Description:** Write a script that takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument. But this time, write one that is safe from MySQL injections!

### Task 4: Cities by states
- **File:** `4-cities_by_state.py`
- **Description:** Write a script that lists all `cities` from the database `hbtn_0e_4_usa`

### Task 5: All cities by state
- **File:** `5-filter_cities.py`
- **Description:** Write a script that takes in the name of a state as an argument and lists all `cities` of that state, using the database `hbtn_0e_4_usa`

### Task 6: First state model
- **File:** `model_state.py`
- **Description:** Write a python file that contains the class definition of a `State` and an instance `Base = declarative_base()`

### Task 7: All states via SQLAlchemy
- **File:** `7-model_state_fetch_all.py`
- **Description:** Write a script that lists all `State` objects from the database `hbtn_0e_6_usa`

### Task 8: First state
- **File:** `8-model_state_fetch_first.py`
- **Description:** Write a script that prints the first `State` object from the database `hbtn_0e_6_usa`

### Task 9: Contains 'a' 
- **File:** `9-model_state_filter_a.py`
- **Description:** Write a script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`

### Task 10: Get a state
- **File:** `10-model_state_my_get.py`
- **Description:** Write a script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`

### Task 11: Add a new state
- **File:** `11-model_state_insert.py`
- **Description:** Write a script that adds the `State` object “Louisiana” to the database `hbtn_0e_6_usa`

### Task 12: Update a state
- **File:** `12-model_state_update_id_2.py`
- **Description:** Write a script that changes the name of a `State` object from the database `hbtn_0e_6_usa`

### Task 13: Delete states
- **File:** `13-model_state_delete_a.py`
- **Description:** Write a script that deletes all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`

### Task 14: Cities in state
- **Files:** `model_city.py`, `14-model_city_fetch_by_state.py`
- **Description:** Write a Python file similar to `model_state.py` named `model_city.py` that contains the class definition of a `City` as well as a script that prints all `City` objects from the database `hbtn_0e_14_usa`

