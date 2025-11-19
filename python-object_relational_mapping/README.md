<!-- anchor for "back to top" -->
<a id="readme-top"></a>

<p align="center">
  <a href="#readme-top">
    <img alt="Assignment: Python — object-relational mapping" src="https://img.shields.io/badge/Assignment-Python%20--%20object--relational%20mapping-blue">
  </a>
  <a href="#task-function-glossary">
    <img alt="Tasks: 18" src="https://img.shields.io/badge/Tasks-18-6c757d">
  </a>
</p>

---

# Python — object-relational mapping

#### Learn: use MySQLdb to send SQL from Python; read command line args with sys.argv; sort and filter rows with SELECT; avoid SQL injection by using safe parameters; list related data from two tables; define SQLAlchemy models for tables; create an engine and session; query with filter, order_by, first; add, update, and delete rows through ORM objects; use relationships between State and City; see how one query can load states with their cities or cities with their state.

## PROJECT 1

This project covers:

- Direct database access with **MySQLdb**.
- Reading credentials and values from **command line arguments**.
- Sending SQL: `SELECT`, `WHERE`, `ORDER BY`, joins between tables.
- Understanding **SQL injection** risk and how to avoid it.
- Moving from raw SQL to **SQLAlchemy ORM**.
- Defining models for `states` and `cities` using `declarative_base`.
- Creating an **engine** and **session**, and running ORM queries.
- Using **filter**, **order_by**, **first**, and loops over ORM results.
- Creating, updating, and deleting rows with ORM objects.
- Building **relationships** between State and City and using them from both sides.

<a id="task-function-glossary"></a>
## Task Function Summaries - function, definition, result.

### 0) Python — object-relational mapping — Get all states
- **What it does:** Connects to `hbtn_0e_0_usa` and prints all rows in the `states` table in order by id.  
  *Example: (1, 'California'), (2, 'Arizona'), ...*
- **Function learned/applied:** MySQLdb connection, cursor, basic SELECT with ORDER BY, reading `sys.argv` for login and database name.
- **Result obtained:** A list of all states printed as tuples `(id, 'name')`, one per line, matching the project example.
---

### 1) Python — object-relational mapping — Filter states
- **What it does:** Shows only the states whose names start with the letter `N` from `hbtn_0e_0_usa`.  
  *Example: (4, 'New York'), (5, 'Nevada')*
- **Function learned/applied:** Adding a WHERE condition on the state name, still using MySQLdb and sorting by id.
- **Result obtained:** A filtered list of state tuples where the name begins with `N`, printed in ascending id order.
---

### 2) Python — object-relational mapping — Filter states by user input
- **What it does:** Takes a state name from the command line and prints all states whose name matches that value.  
  *Example: passing "Arizona" prints only (2, 'Arizona')*
- **Function learned/applied:** Building a query that uses user input in the WHERE clause, showing how inserting raw text into SQL can be unsafe.
- **Result obtained:** Matching state rows printed as tuples, sorted by id, based on the exact name given by the user.
---

### 3) Python — object-relational mapping — SQL Injection safe filter
- **What it does:** Does the same name filter as task 2 but protects the database from SQL injection attacks.  
  *Example: a strange input does not delete or change the table*
- **Function learned/applied:** Parameterized queries with MySQLdb, where SQL text and user values are kept separate to avoid injection.
- **Result obtained:** Correct matches for the given state name, with the query staying safe even if the user passes SQL-looking text.
---

### 4) Python — object-relational mapping — Cities by states
- **What it does:** Lists all cities from `hbtn_0e_4_usa` and shows each city with its state name.  
  *Example: (1, 'San Francisco', 'California')*
- **Function learned/applied:** Joining two tables (`cities` and `states`) in one SQL query, using MySQLdb and ordering by `cities.id`.
- **Result obtained:** Each line prints a tuple `(city_id, 'city_name', 'state_name')`, ordered by city id, showing how foreign keys link tables.
---

### 5) Python — object-relational mapping — All cities by state
- **What it does:** Takes a state name and prints all city names from that state in one comma-separated line.  
  *Example: Texas → Dallas, Houston, Austin*
- **Function learned/applied:** Safe parameterized join between `cities` and `states`, filtering by a given state name and collecting names into one string.
- **Result obtained:** A single line with city names separated by commas for the chosen state, or an empty line if there are no matching cities.
---

### 6) Python — object-relational mapping — First state model
- **What it does:** Defines the `State` class and base needed by SQLAlchemy to map the `states` table.  
  *Example: later calls to metadata.create_all create the table from this model*
- **Function learned/applied:** Using `declarative_base`, setting `__tablename__`, and declaring columns for `id` and `name`.
- **Result obtained:** A Python model that describes the `states` table structure so other scripts can create the table and work with state objects.
---

### 7) Python — object-relational mapping — All states via SQLAlchemy
- **What it does:** Uses SQLAlchemy to list all states from `hbtn_0e_6_usa` as model objects instead of raw tuples.  
  *Example: prints "1: California", "2: Arizona", ...*
- **Function learned/applied:** Creating an engine and session, importing `Base` and `State`, querying all State objects with `order_by`.
- **Result obtained:** One line per state in the format `id: name`, showing that ORM objects can replace direct SQL tuples.
---

### 8) Python — object-relational mapping — First state
- **What it does:** Prints only the first state when ordered by id, or "Nothing" if the table is empty.  
  *Example: "1: California"*
- **Function learned/applied:** Using `order_by` with `first()` to get a single ORM object, and handling the case where no result is found.
- **Result obtained:** Either `id: name` for the first state, or the word `Nothing` if there are no states.
---

### 9) Python — object-relational mapping — Contains a
- **What it does:** Lists all states whose names contain the letter `a` from `hbtn_0e_6_usa`.  
  *Example: California, Arizona, Texas, Nevada*
- **Function learned/applied:** Filtering ORM queries on the `name` field using a condition that checks for a substring, plus ordering results.
- **Result obtained:** Lines in the form `id: name` for each state whose name includes the letter `a`, sorted by id.
---

### 10) Python — object-relational mapping — Get a state
- **What it does:** Takes a state name from the command line and prints the id of the state with that name, or "Not found".  
  *Example: Texas → 3; Illinois → Not found*
- **Function learned/applied:** Using SQLAlchemy filter to look up a single row by an exact name value, then checking if any match was found.
- **Result obtained:** The id of the matching state printed alone, or the message `Not found` if there is no row with that name.
---

### 11) Python — object-relational mapping — Add a new state
- **What it does:** Creates the state “Louisiana” in `hbtn_0e_6_usa` and prints its new id.  
  *Example: after running, shows "6" and Louisiana appears in the table*
- **Function learned/applied:** Creating a new ORM object, adding it to the session, committing, and reading the id generated by the database.
- **Result obtained:** A new state row is added to the database and its id is printed so you can confirm the insert worked.
---

### 12) Python — object-relational mapping — Update a state
- **What it does:** Changes the name of the state with id `2` to “New Mexico” in `hbtn_0e_6_usa`.  
  *Example: id 2 was "Arizona", now becomes "New Mexico"*
- **Function learned/applied:** Selecting a single state by id with SQLAlchemy, updating one field, and committing the change.
- **Result obtained:** The row with id 2 is updated so that its name is “New Mexico”, while all other rows stay the same.
---

### 13) Python — object-relational mapping — Delete states
- **What it does:** Deletes all states whose names contain the letter `a` from `hbtn_0e_6_usa`.  
  *Example: only states without `a` remain, like New Mexico and New York*
- **Function learned/applied:** Filtering a query to get multiple ORM objects, deleting them from the session, and committing once for all deletes.
- **Result obtained:** All states with `a` in their names are removed, and a later list shows only the states whose names do not contain `a`.
---

### 14) Python — object-relational mapping — Cities in state
- **What it does:** Adds a `City` model and prints all cities from `hbtn_0e_14_usa` together with their state names.  
  *Example: "California: (1) San Francisco"*
- **Function learned/applied:** Defining a second model (`City`) with a foreign key to `states.id`, and using SQLAlchemy queries to join city and state data.
- **Result obtained:** Lines in the form `<state name>: (<city id>) <city name>`, sorted by city id, showing the link between the two tables through ORM.
---

### 15) Python — object-relational mapping — City relationship (advanced)
- **What it does:** Improves the State and City models so that each State has a list of its cities, and each City points back to its State. Also creates “California” with “San Francisco” using this relationship.  
  *Example: one state row and one linked city row created in `hbtn_0e_100_usa`*
- **Function learned/applied:** Adding a `relationship` on the State side with cascade rules, and a back reference from City to State, then using this relationship to create linked rows.
- **Result obtained:** A new database with a State and City linked through ORM relationships, showing how objects can manage related rows without writing join SQL by hand.
---

### 16) Python — object-relational mapping — List relationship (advanced)
- **What it does:** Lists every state and its cities from `hbtn_0e_101_usa` using the `cities` relationship on the State model.  
  *Example: each state on one line, then its cities on indented lines*
- **Function learned/applied:** Using a single ORM query to load states and their cities, then looping over the relationship list instead of writing manual joins.
- **Result obtained:** Output like:
  - `1: California`  
    `    1: San Francisco`  
    `    2: San Jose`  
  where states are sorted by id and each state’s cities are also sorted by id.
---

### 17) Python — object-relational mapping — From city (advanced)
- **What it does:** Lists every city from `hbtn_0e_101_usa` and shows the state each city belongs to in one line.  
  *Example: "1: San Francisco -> California"*
- **Function learned/applied:** Querying City objects and using the `state` relationship to access their parent State, while sorting by city id.
- **Result obtained:** Lines in the form `<city id>: <city name> -> <state name>`, showing the direction City → State using ORM relationships.
---

