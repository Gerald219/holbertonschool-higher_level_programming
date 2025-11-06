Task 1 — curl quick notes

Goal (1 sentence): Use curl to GET data, see headers, and POST data to a public API.

A) Check curl

Version run:
$ curl --version
Output (first line):

curl 8.5.0 (x86_64-pc-linux-gnu)

curl 8.4.0 (aarch64-unknown-linux-gnu)

curl 7.88.1 (x86_64-apple-darwin)

curl 7.68.0 (x86_64-pc-linux-gnu)

curl 8.7.1 (x86_64-w64-mingw32)

Fetch a web page:
$ curl http://example.com

What did you see (1 line):

HTML for “Example Domain”

The Example Domain homepage markup

A small HTML page titled “Example Domain”

Simple sample page HTML content

Minimal HTML with “Example Domain” title

B) GET posts from JSONPlaceholder

Command:
$ curl https://jsonplaceholder.typicode.com/posts

First 1–2 titles you saw (copy tiny snippet):

"sunt aut facere..." , "qui est esse"

sunt aut facere repellat..., qui est esse

title: "sunt aut facere..."

#1 sunt aut facere..., #2 qui est esse

"sunt aut facere..." / "qui est esse"

C) Only the headers (-I)

Command:
$ curl -I https://jsonplaceholder.typicode.com/posts

Status + two headers (e.g., Content-Type, Date):

Status:

HTTP/2 200

HTTP/1.1 200 OK

200 OK

HTTP/2 200 OK

HTTP/1.1 200

Header 1:

Content-Type: application/json; charset=utf-8

Date: Thu, 06 Nov 2025 20:00:00 GMT

Cache-Control: max-age=43200

Server: cloudflare

X-Powered-By: Express

Header 2:

Date: Thu, 06 Nov 2025 20:00:00 GMT

Content-Length: <varies>

Vary: Origin, Accept-Encoding

Connection: keep-alive

ETag: W/"xxxx-xxxx"

D) Send a POST (fake create)
Command (URL-encoded body):
$ curl -X POST \
  -d "title=foo&body=bar&userId=1" \
  https://jsonplaceholder.typicode.com/posts

Returned (examples you observed):
{"title":"foo","body":"bar","userId":"1","id":101}
{"id":101,"title":"foo","body":"bar","userId":"1"}

One-line summary:
A JSON object echoing the sent fields plus "id": 101 (simulated create).

Mini glossary

-I → fetch headers only

-X POST → choose HTTP method

-d → send body data (defaults to form-encoded)
