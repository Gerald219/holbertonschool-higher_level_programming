# HTTP vs HTTPS

When you visit a website, your browser uses HTTP or HTTPS to talk to it.

**HTTP**
This is like mailing a postcard. Anyone who handles it can read what you wrote. No locks, no secrets.

**HTTPS**
This is like putting your message in a locked box. Only the person with the key can open it. It scrambles your info so nobody else can see or change it.

**How you can spot the difference:**

- HTTP = open postcard (not safe)
- HTTPS = locked box (safe)
- HTTPS shows a little padlock icon in your browser.

# HTTP Request and Response

When your browser and a website interact, it sends responses back and forth.

**HTTP Request (you asking):**
Your browser responds to the server that says:

- **Method:** What you want to do (GET = “send me something” or POST = “heres some data”).
- **Path:** The address of the platform or data you want.
- **Headers:** Extra info about the response (type of content).
- **Body (optional):** The data you’re sending.

**HTTP Response (server answering):**
The server writes back with:

- **Status line:** A quick summary (200 = “Everything’s fine,” 404 = “Can’t find it”).
- **Headers:** More notes about what’s inside (like “this is HTML”).
- **Body:** The actual thing you asked for (like the webpage or some data).

# Common HTTP Methods

- **GET:** Get data, example-> opening a webpage.
- **POST:** Send new data, push data, uploading a form.
- **PUT:** Change existing data, example-> editing data of a profile.
- **DELETE:** Remove data.

# Common HTTP Status Codes

- **200 OK:** Everything worked.
- **201 Created:** Something was created.
- **400 Bad Request:** The request was invalid.
- **404 Not Found:** The item was not found.
- **500 Internal Server Error:** The server had an error.

