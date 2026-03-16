import streamlit as st

st.set_page_config(page_title="System Design Encyclopedia", layout="wide")

st.title("High Level Design Components – Practical Encyclopedia")

st.markdown("""
In system design interviews, many students get confused because there are
too many components. The trick is to group them.

Every large system can be understood using **5 simple layers**.

EDGE → TRAFFIC → COMPUTE → DATA → RELIABILITY

Think of it like a **shopping mall**:

Users enter the gate → Security directs people → Shops do the work →
Goods are stored in warehouses → CCTV and guards keep things safe.

The same idea applies to software systems.
""")

# ----------------------------------------------------------
st.header("1. EDGE LAYER – Where Users Enter")

with st.expander("DNS (Domain Name System)"):
   st.set_page_config(page_title="DNS Explained", layout="wide")

   st.markdown("""
The Domain Name System (DNS) is the naming infrastructure of the internet.  
It exists to translate human-readable domain names into machine-readable IP addresses.  
Every device connected to the internet communicates using IP addresses, but humans
prefer to remember simple names such as **google.com** or **openai.com** rather than
numerical addresses like **142.250.190.14**.

DNS acts as a distributed directory that maps domain names to their corresponding
IP addresses. Whenever a user enters a website address in a browser, DNS performs
a lookup process to determine which server hosts that website and returns the
correct IP address so the browser can establish a connection.

DNS is therefore one of the fundamental services of the internet. Without DNS,
users would have to memorize the numerical IP address of every website they want
to visit.


### Why DNS Exists

The internet is built on the Internet Protocol (IP), which identifies machines
using numerical addresses. These addresses are efficient for computers but
extremely difficult for humans to remember.

DNS solves this problem by introducing a hierarchical naming system where
meaningful domain names represent numerical IP addresses. This abstraction
layer allows people to interact with the internet using simple names while
computers continue to communicate using numbers.


### Basic Example

When a user types:

    google.com

into the browser, the system cannot directly contact the website because it
does not yet know the IP address of the server hosting that domain.

DNS resolves the name into an IP address such as:

    142.250.190.14

The browser then uses this IP address to send requests to the correct server
and retrieve the webpage.


### DNS Hierarchy

DNS is designed as a hierarchical distributed system rather than a single
centralized database. The hierarchy allows the system to scale across the
entire internet.

The structure contains several levels:

Root Level  
The root level sits at the top of the DNS hierarchy and directs queries to
the correct top-level domain servers.

Top-Level Domains (TLDs)  
These represent the major categories of domains such as:

    .com
    .org
    .edu
    .net
    .gov

Each top-level domain is managed by authoritative servers responsible for
handling queries related to that domain.

Second-Level Domains  
These are the main domain names registered by users or organizations.

Example:

    google.com
    wikipedia.org
    mit.edu

Subdomains  
Organizations can create additional subdivisions under their main domain.

Example:

    mail.google.com
    docs.google.com
    api.example.com

This hierarchy allows the DNS system to distribute responsibility across
thousands of servers worldwide.


### Components of DNS Resolution

Several components work together to resolve a domain name.

DNS Resolver  
A DNS resolver is typically provided by an Internet Service Provider (ISP)
or a public DNS service. It receives queries from the user's device and
performs the lookup process to find the correct IP address.

Root Name Servers  
Root servers are the first step in the DNS lookup process. They direct the
resolver to the correct top-level domain servers.

TLD Name Servers  
These servers store information about domains within a specific top-level
domain such as .com or .org.

Authoritative Name Servers  
These servers hold the final DNS records for a domain and provide the
actual IP address associated with the requested domain name.


### DNS Lookup Process

The DNS lookup process occurs whenever a user accesses a website.

1. The user enters a domain name into the browser.

2. The browser checks its local cache to see whether it already knows the
   IP address for that domain.

3. If the address is not cached, the browser sends a query to a DNS resolver.

4. The resolver contacts a root server to determine which top-level domain
   server is responsible for the domain.

5. The root server directs the resolver to the appropriate TLD server.

6. The TLD server points the resolver to the authoritative name server for
   the domain.

7. The authoritative name server returns the correct IP address.

8. The resolver sends this IP address back to the browser.

9. The browser uses the IP address to contact the web server and request
   the webpage.


### DNS Records

DNS stores information in structured records known as DNS records.

A Record  
Maps a domain name to an IPv4 address.

AAAA Record  
Maps a domain name to an IPv6 address.

CNAME Record  
Creates an alias for a domain by pointing one domain name to another.

MX Record  
Specifies the mail servers responsible for receiving email for a domain.

NS Record  
Identifies the authoritative name servers for a domain.

TXT Record  
Stores arbitrary text data, often used for domain verification and
security mechanisms.


### DNS Caching

DNS queries are cached at multiple levels to improve performance and reduce
network traffic. Once a resolver retrieves a domain's IP address, it stores
the result temporarily.

If another user requests the same domain during the cache period, the resolver
can return the stored result without repeating the entire lookup process.

Caching significantly speeds up browsing and reduces load on DNS infrastructure.


### Distributed Design

DNS is designed as a distributed system with servers located across the world.
No single server contains all domain information. Instead, responsibility is
delegated across many independent name servers.

This architecture ensures that DNS remains scalable, reliable, and fault
tolerant even as the number of internet users and websites continues to grow.


### Importance of DNS

DNS is essential for the functioning of the modern internet because it:

• Provides human-friendly naming for internet resources  
• Enables scalable addressing across billions of devices  
• Allows domain ownership and management by different organizations  
• Supports efficient routing of internet traffic  

In essence, DNS serves as the internet’s global phonebook, translating
readable domain names into the numerical addresses required for network
communication.
""")

with st.expander("CDN (Content Delivery Network)"):
    st.markdown("""
# CDN – Content Delivery Network

A CDN helps websites deliver content to users **much faster**.

When users visit a website, they may be located in different countries.
If the server is far away, loading the website becomes slow.

A **Content Delivery Network (CDN)** solves this problem by storing
copies of website content in many locations around the world.

Example:

A server may be located in the **United States**.

But users in **India, Japan, and Europe** can receive the content
from servers that are closer to them.

This reduces delay and improves website speed.

---

# 1. What is a CDN

CDN stands for **Content Delivery Network**.

It is a network of servers placed in different geographical locations.

These servers store **cached copies of website content**.

When a user visits the website, the CDN serves the content
from the **nearest server** instead of the main server.

Example:

User in India visits a website.

Instead of loading data from a server in the US,
the CDN serves the content from a **server in India**.

This makes the website load faster.

---

# 2. Simple Analogy

Think of a CDN like **multiple warehouses for a company**.

Imagine a company has only **one warehouse in Delhi**.

If a customer in **Chennai** orders a product,
delivery will take many days.

Now imagine the company has warehouses in:

Delhi  
Mumbai  
Chennai  
Bangalore

The product can be delivered from the **nearest warehouse**.

A CDN works exactly like this for website content.

---

# 3. Why CDN is Needed

Without a CDN, every user request must go to the **main server**.

Problems:

• High latency (slow loading)  
• Server overload  
• Poor user experience  

A CDN solves these problems.

Benefits:

• Faster website loading  
• Reduced load on main server  
• Better performance worldwide

---

# 4. Important CDN Components

## Origin Server

The origin server is the **main server where the website is hosted**.

It contains the original files such as:

HTML  
Images  
Videos  
CSS  
JavaScript

The CDN copies content from the origin server.

---

## Edge Server

Edge servers are CDN servers located close to users.

These servers store cached copies of content.

When users request data, the **edge server delivers it quickly**.

---

## CDN Cache

CDN cache stores frequently accessed content.

Instead of requesting data from the origin server every time,
the CDN serves it from the cache.

This reduces load on the origin server.

---

# 5. How CDN Works (Step by Step)

Let us understand what happens when a user visits a website.

Step 1 – User enters website URL

Example:

example.com

Step 2 – DNS directs request to CDN

Instead of sending the request directly to the origin server,
DNS sends it to the CDN.

Step 3 – CDN finds the nearest edge server

The CDN identifies which server is closest to the user.

Step 4 – Edge server checks cache

If the content is already cached,
the edge server sends it directly to the user.

Step 5 – If content is not cached

The CDN fetches it from the origin server.

Step 6 – CDN stores a copy

The content is cached in the edge server for future requests.

Step 7 – User receives the content

The website loads faster.

---

# 6. What Content CDN Usually Stores

CDNs mainly cache **static content**.

Examples:

Images  
Videos  
CSS files  
JavaScript files  
Fonts

These files do not change frequently,
so they are perfect for caching.

---

# 7. Real World Example

Suppose Netflix stores its main servers in the US.

Users in India want to watch movies.

If every request goes to the US,
video streaming will become slow.

Instead, Netflix uses CDN servers in many countries.

When a user in India watches a movie,
the video is streamed from a **nearby CDN server**.

This makes streaming smooth and fast.

---

# 8. Popular CDN Providers

Many companies provide CDN services.

Examples:

Cloudflare  
Amazon CloudFront  
Akamai  
Fastly  
Google Cloud CDN

These companies maintain thousands of servers worldwide.

---

# 9. Simple Memory Trick

Remember this simple flow:

User → DNS → CDN Edge Server → Cache → Origin Server (if needed)

If the content is cached:

User → CDN Edge Server → Website Loads Fast

If not cached:

User → CDN → Origin Server → Cache → User

This is how CDNs improve internet performance.
""")

with st.expander("API Gateway"):
    st.markdown("""
**What it is**

API Gateway is the **main entry gate for backend services**.

All requests first go to the API Gateway.

**Why we need it**

Without API gateway, the client would need to call
many microservices directly.

API Gateway simplifies this.

**Responsibilities**

• Authentication  
• Request routing  
• Rate limiting  
• Logging  

**Example**

Mobile app → API Gateway → User Service / Payment Service
""")

# ----------------------------------------------------------
st.header("2. TRAFFIC MANAGEMENT – Controlling Requests")

with st.expander("Load Balancer"):
    st.markdown("""
**What it is**

A load balancer distributes requests across many servers.

**Why we need it**

If one server receives all requests it will crash.

Load balancer spreads the work.

**Example**

1000 users send requests.

Instead of one server handling everything:

Server1 → 250 requests  
Server2 → 250 requests  
Server3 → 250 requests  
Server4 → 250 requests

**Benefit**

System becomes faster and safer.
""")

with st.expander("Rate Limiter"):
    st.markdown("""
**What it is**

A rate limiter controls how many requests a user can send.

**Why we need it**

Without rate limiting:

• Hackers can attack the system  
• Bots can overload servers  

**Example**

Twitter allows only a certain number of tweets per minute.

**Simple rule**

```
User can send only 100 requests per minute
```
""")

with st.expander("Circuit Breaker"):
    st.markdown("""
**What it is**

Circuit breaker stops requests to a failing service.

**Why we need it**

If one service crashes and other services keep calling it,
the whole system may fail.

Circuit breaker temporarily blocks the calls.

**Example**

Payment service is down.

Instead of waiting forever:

System returns:

```
Payment service unavailable. Try later.
```
""")

# ----------------------------------------------------------
st.header("3. COMPUTE LAYER – Where Work Happens")

with st.expander("Application Servers"):
    st.markdown("""
**What it is**

Application servers run backend code.

They contain the business logic.

**Examples of business logic**

• Login verification  
• Order placement  
• Payment processing  

**Example flow**

User login request → Application server checks username/password.
""")

with st.expander("Microservices"):
    st.markdown("""
**What it is**

Instead of one big application, we divide the system
into small independent services.

**Why we need it**

Large systems become difficult to maintain.

Small services are easier to manage.

**Example**

Instead of one large app:

User Service  
Payment Service  
Notification Service  
Order Service

Each service does one job.
""")

with st.expander("Background Workers"):
    st.markdown("""
**What it is**

Background workers process tasks that do not need
immediate response.

**Why we need it**

Some tasks take time.

Example:

• Sending emails  
• Video processing  
• Image resizing  

Instead of making the user wait, we process them in background.

**Example**

User uploads photo → background worker compresses image.
""")

# ----------------------------------------------------------
st.header("4. DATA LAYER – Where Data is Stored")

with st.expander("Relational Databases (SQL)"):
    st.markdown("""
**What it is**

A structured database where data is stored in tables.

**Example table**

Users table

| id | name | email |
|----|------|------|

**Why we use SQL databases**

• Strong consistency  
• Transactions  
• Reliable storage

**Examples**

PostgreSQL  
MySQL
""")

with st.expander("NoSQL Databases"):
    st.markdown("""
**What it is**

Databases designed for large scale systems
where flexible data structure is needed.

**Types**

Document database → MongoDB  
Key-value store → DynamoDB  
Column store → Cassandra  

**Why we use them**

Better scalability compared to traditional databases.
""")

with st.expander("Cache"):
    st.markdown("""
**What it is**

Cache stores frequently used data in memory.

Memory is much faster than disk.

**Why we need it**

If database is queried every time,
system becomes slow.

Cache stores popular data.

**Example**

Trending videos list stored in Redis.
""")

with st.expander("Message Queue"):
    st.markdown("""
**What it is**

A message queue allows services to communicate asynchronously.

**Why we need it**

Services should not depend on each other directly.

Queues help decouple them.

**Example**

User signs up → message placed in queue

Other services read the message:

• Email service sends welcome mail  
• Analytics service records new user
""")

# ----------------------------------------------------------
st.header("5. RELIABILITY LAYER – Keeping System Healthy")

with st.expander("Monitoring"):
    st.markdown("""
**What it is**

Monitoring tools track system health.

**Things monitored**

• CPU usage  
• Memory usage  
• Response time  
• Error rate  

If something goes wrong engineers can see it quickly.
""")

with st.expander("Logging"):
    st.markdown("""
**What it is**

Logs record events happening inside the system.

Example log

```
User 1023 logged in at 10:02 AM
```

Logs help debug problems later.
""")

with st.expander("Auto Scaling"):
    st.markdown("""
**What it is**

Auto scaling automatically increases or decreases
the number of servers.

**Example**

During IPL match streaming:

Traffic increases → more servers start automatically.

After match:

Traffic decreases → servers shut down.
""")

with st.expander("Replication"):
    st.markdown("""
**What it is**

Replication means keeping multiple copies of data.

**Why we need it**

If one database server crashes,
another copy is available.

This improves reliability.
""")

# ----------------------------------------------------------

st.header("Simple Memory Trick")

st.markdown("""
Remember this simple chain:

User → DNS → CDN → Load Balancer → Servers → Cache → Database → Monitoring

If you remember this flow, you can explain most system designs in interviews.
""")