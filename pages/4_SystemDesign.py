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
    # DNS – Domain Name System

    DNS is one of the most important systems on the internet.

    Without DNS, users would have to remember long IP addresses instead of simple website names.

    Example:

    Instead of typing

    142.250.190.14

    we simply type

    google.com

    DNS converts the website name into the correct IP address.

    ---

    # 1. What is DNS

    DNS stands for **Domain Name System**.

    It is a system that converts **domain names** into **IP addresses**.

    Computers communicate using IP addresses.

    Humans prefer easy names.

    DNS connects these two worlds.

    Example:

    google.com → 142.250.190.14  
    youtube.com → 142.250.183.206

    ---

    # 2. Simple Analogy

    Think of DNS like a **phone contact list**.

    Instead of remembering a phone number, we remember a name.

    Example:

    Prasad → 9876543210

    Similarly:

    google.com → 142.250.190.14

    DNS is basically the **contact list of the internet**.

    ---

    # 3. Why DNS is Needed

    Imagine if DNS did not exist.

    To visit websites we would need to type IP addresses.

    Example:

    Instead of

    google.com

    we would type

    142.250.190.14

    Now imagine remembering IP addresses for thousands of websites.

    DNS solves this problem by mapping names to IP addresses.

    ---

    # 4. Important DNS Components

    ## Domain Name

    A domain name is the human readable website name.

    Examples:

    amazon.com  
    netflix.com  
    facebook.com

    ---

    ## IP Address

    The actual address of a server on the internet.

    Example:

    172.217.160.142

    Servers communicate using IP addresses.

    ---

    ## DNS Resolver

    A DNS resolver finds the IP address for a domain name.

    Usually provided by:

    • Internet Service Provider  
    • Google DNS (8.8.8.8)  
    • Cloudflare DNS (1.1.1.1)

    ---

    ## Root DNS Server

    Root servers are the top level DNS servers.

    They help direct requests to the correct domain servers.

    ---

    ## TLD Server

    TLD means Top Level Domain.

    Examples:

    .com  
    .org  
    .net  
    .in

    These servers manage domains under that extension.

    ---

    ## Authoritative DNS Server

    This server contains the final mapping between domain name and IP address.

    Example:

    netflix.com → 52.89.124.15

    ---

    # 5. DNS Resolution Process (Step by Step)

    Let us understand what happens when a user types a website.

    Step 1 – User enters URL

    Example:

    www.netflix.com

    Step 2 – Browser checks local cache

    If the IP address is already stored locally, the browser uses it directly.

    Step 3 – Request goes to DNS Resolver

    The resolver searches for the IP address.

    Step 4 – Resolver asks Root DNS Server

    Root server tells where to find the correct TLD server.

    Step 5 – Resolver asks TLD Server

    TLD server tells which server knows about the domain.

    Step 6 – Resolver asks Authoritative Server

    Authoritative server provides the correct IP address.

    Example:

    netflix.com → 52.89.124.15

    Step 7 – Resolver sends IP to browser

    Step 8 – Browser connects to the server

    The website finally loads.

    ---

    # 6. DNS Caching

    DNS caching stores recently used domain lookups.

    This speeds up future requests.

    Caching can happen in:

    • Browser cache  
    • Operating system cache  
    • ISP DNS cache

    Example:

    If you visited youtube.com recently, the IP address may already be stored locally.

    ---

    # 7. Types of DNS Records

    ## A Record

    Maps domain name to IPv4 address.

    Example:

    example.com → 93.184.216.34

    ---

    ## AAAA Record

    Maps domain name to IPv6 address.

    ---

    ## CNAME Record

    Creates an alias for another domain.

    Example:

    www.example.com → example.com

    ---

    ## MX Record

    Specifies mail servers for email delivery.

    ---

    ## TXT Record

    Stores text information for verification and security purposes.

    ---

    # 8. Real World Example

    User opens browser and types:

    amazon.com

    DNS converts the domain to an IP address.

    Example:

    amazon.com → 54.239.28.85

    Browser connects to that server.

    The server sends back the website data and the page loads for the user.

    ---

    # 9. Simple Memory Trick

    Remember this simple flow:

    User → Browser → DNS Resolver → Root Server → TLD Server → Authoritative Server → IP Address → Website Loads

    If you remember this chain, you can explain DNS clearly in interviews.
    """)

with st.expander("CDN (Content Delivery Network)"):
    st.markdown("""
**What it is**

A CDN stores copies of static files in many countries.

**Why we need it**

If a server is only in the US, users in India will get slow speed.

A CDN keeps copies of files close to users.

**What files are cached**

• Images  
• Videos  
• CSS  
• JavaScript  

**Example**

When you open Instagram, images load fast because
they are served from nearby CDN servers.
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