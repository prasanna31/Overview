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
    st.Page("./sub-pages/DNS.py", title="DNS"),

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