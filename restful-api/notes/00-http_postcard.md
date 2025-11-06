Task 0 — HTTP/HTTPS Quick Card (compact)
Goal (one sentence): 


A) HTTP vs HTTPS
1) HTTP : moves information between client and server, but it does not protect it in transit.
2) HTTPS : protects the information you send and receive by adding encryption on top of normal web communication.
3) Encrypted?  HTTP: Non-encrypted. Public.  |  HTTPS: Using SSL and tlS; the data is scrambled so only the right server can read it to keep safe.

4) Default ports: HTTP uses port 80, and HTTPS uses port 443.

5) One case that must use HTTPS (why): sending a password, because HTTPS hides it so no one can steal it.
6) One risk of plain HTTP: Someone on the same network can spy on what you type or see.

B) Request (what I sent)

7) Method: The method is the action you ask the server to do, like GET or POST.
8) Path + query: The path is the page or resource you want, and the query adds extra details like filters or search terms.
9) Two request headers: A request can include Content-Type to say what kind of data you are sending, and Accept to say what kind of data you want back.

10) Body? yes/no: it is a yes, the body holds the data you are sending, for example a JSON with user info.

C) Response (what I got back)

11) Status (e.g., 200 OK): The status is the servers reply code that tells if the request worked or failed, like 200 OK, it went through.

12) Two response headers (include Content-Type as one): One response header is Content-Type, which tells what format the server is sending, and another is Content-Length, which shows how big the data is.
   
13) Body (1 line): The body is the actual data the server sends back, like HTML or JSON.

D) Methods (when to use + tiny example)

14) GET: used to read data
   ex: GET /users → returns all users

15) POST: used to create something new
   ex: POST /users → creates a new user

16) PUT: replace the whole item
   ex: PUT /users/5 → replace user #5’s info

17) PATCH: update only part of an item
   ex: PATCH /users/5 → change only the email

18) DELETE: remove an item
   ex: DELETE /users/5 → delete user #5

E) Status codes (meaning + quick scenario)

19) 200 OK: request worked fine
   scenario: GET /users returns the list

20) 201 Created: something new was saved
   scenario: POST /users creates a new account

21) 400 Bad Request: the request was wrong or broken
   scenario: sending invalid JSON

22) 401 Unauthorized: user needs to log in first
   scenario: trying to access /profile with no token

23) 404 Not Found: item or page doesn’t exist
   scenario: GET /users/999 but user 999 is not there

Memory hooks (your own words, ≤5 words each)
Method = action | Path = resource | Status = result code | Headers = extra info | Body = data

