import streamlit as st

st.set_page_config(page_title="HLD Encyclopedia", layout="wide")

st.title("High Level Design Components Encyclopedia")

st.markdown("""
High Level Design (HLD) is about designing systems that are scalable, reliable,
and efficient. Most large distributed systems can be understood by organizing
their components into a few conceptual layers.

### Mental Model

EDGE → TRAFFIC → COMPUTE → DATA → RELIABILITY

1. Edge Layer – Where users enter the system  
2. Traffic Layer – How requests are routed  
3. Compute Layer – Where business logic runs  
4. Data Layer – Where information is stored  
5. Reliability Layer – How the system survives failures
""")

# ============================================================
st.subheader("1. Edge Layer — User Entry Layer")

with st.expander("API Gateway"):
    st.markdown("""
Single entry point for all client requests.

Responsibilities
- Authentication
- Authorization
- Request routing
- Rate limiting
- API aggregation
- Request validation

Example:
Mobile apps communicate with the API gateway instead of directly
calling microservices.
""")

with st.expander("CDN (Content Delivery Network)"):
    st.markdown("""
Distributed network of servers that cache static content.

Benefits
- Reduced latency
- Lower backend load
- Faster global delivery

Cached content includes:
Images, videos, CSS, JavaScript.
""")

with st.expander("DNS"):
    st.markdown("""
Domain Name System translates domain names into IP addresses.

Example

google.com → 142.250.190.14

Without DNS users would need to remember IP addresses.
""")

with st.expander("Reverse Proxy"):
    st.markdown("""
A server that sits in front of backend servers and forwards requests.

Benefits
- Security
- SSL termination
- Request routing
- Load balancing
""")

with st.expander("Edge Caching"):
    st.markdown("""
Caching content close to the user.

This reduces latency and reduces the number of requests
reaching backend servers.
""")

# ============================================================
st.subheader("2. Traffic Management Layer")

with st.expander("Load Balancer"):
    st.markdown("""
Distributes incoming requests across multiple servers.

Goals
- Prevent overload
- Improve reliability
- Enable horizontal scaling

Common Algorithms
- Round Robin
- Least Connections
- Consistent Hashing
""")

with st.expander("Service Discovery"):
    st.markdown("""
Helps services dynamically locate each other.

In distributed systems services frequently change instances.
Service discovery maintains a registry of available services.
""")

with st.expander("Rate Limiter"):
    st.markdown("""
Restricts the number of requests a client can make
within a defined time window.

Purpose
- Prevent abuse
- Protect backend systems
- Maintain fairness
""")

with st.expander("Traffic Shaping"):
    st.markdown("""
Controls request flow to prioritize important traffic
and smooth traffic spikes.
""")

with st.expander("Circuit Breaker"):
    st.markdown("""
Stops requests from reaching a failing service.

Prevents cascading failures in distributed systems.
""")

# ============================================================
st.subheader("3. Compute Layer — Business Logic")

with st.expander("Application Servers"):
    st.markdown("""
Servers that execute backend application code.

Examples
- User authentication
- Payment processing
- Order management
""")

with st.expander("Microservices"):
    st.markdown("""
Architectural style where applications are divided
into small independent services.

Benefits
- Independent deployment
- Scalability
- Fault isolation
""")

with st.expander("Containers"):
    st.markdown("""
Lightweight environments that package applications
with dependencies.

Example technology: Docker
""")

with st.expander("Container Orchestration"):
    st.markdown("""
Systems that manage container deployment,
scaling, networking, and health.

Example: Kubernetes
""")

with st.expander("Serverless Functions"):
    st.markdown("""
Code executed on demand without managing servers.

Benefits
- Automatic scaling
- Pay per execution
- Reduced infrastructure management
""")

with st.expander("Background Workers"):
    st.markdown("""
Processes that execute asynchronous tasks.

Examples
- Email sending
- Video processing
- Image resizing
""")

# ============================================================
st.subheader("4. Data Layer — Storage Systems")

with st.expander("Relational Databases (SQL)"):
    st.markdown("""
Structured databases with tables and relationships.

Examples
- PostgreSQL
- MySQL

Strengths
- ACID transactions
- Strong consistency
""")

with st.expander("NoSQL Databases"):
    st.markdown("""
Databases designed for flexible schemas and scalability.

Examples
- MongoDB
- Cassandra
- DynamoDB

Types
- Document stores
- Key-value stores
- Column stores
- Graph databases
""")

with st.expander("Cache"):
    st.markdown("""
In-memory storage used for frequently accessed data.

Benefits
- Extremely fast access
- Reduces database load

Example: Redis
""")

with st.expander("Search Engines"):
    st.markdown("""
Specialized systems optimized for text search and indexing.

Example: Elasticsearch
""")

with st.expander("Message Queues"):
    st.markdown("""
Systems that allow asynchronous communication between services.

Benefits
- Decoupling services
- Reliable task processing

Examples
- RabbitMQ
- Amazon SQS
""")

with st.expander("Event Streaming Platforms"):
    st.markdown("""
Platforms designed for high-throughput real-time event processing.

Example: Apache Kafka
""")

with st.expander("Object Storage"):
    st.markdown("""
Storage optimized for large binary files.

Examples
- Images
- Videos
- Backups

Example technologies
- Amazon S3
- Google Cloud Storage
""")

# ============================================================
st.subheader("5. Reliability & Operations Layer")

with st.expander("Monitoring"):
    st.markdown("""
Tracks system health metrics.

Examples
- CPU usage
- Memory usage
- Latency
- Error rates
""")

with st.expander("Logging"):
    st.markdown("""
Records system events for debugging and auditing.

Logs help engineers diagnose failures and analyze system behavior.
""")

with st.expander("Alerting"):
    st.markdown("""
Automatically notifies engineers when abnormal
conditions occur.

Example triggers
- High latency
- Error spikes
- Server failures
""")

with st.expander("Distributed Tracing"):
    st.markdown("""
Tracks requests across multiple services.

Helps diagnose latency problems in microservice architectures.
""")

with st.expander("Auto Scaling"):
    st.markdown("""
Automatically increases or decreases the number of servers
based on traffic load.
""")

with st.expander("Replication"):
    st.markdown("""
Maintains multiple copies of data to improve
availability and reliability.
""")

with st.expander("Sharding"):
    st.markdown("""
Splits large datasets across multiple machines
to support high traffic workloads.
""")

with st.expander("Backup and Disaster Recovery"):
    st.markdown("""
Processes that restore system data after failures.

Includes
- Snapshots
- Incremental backups
- Cross-region replication
""")

with st.expander("Feature Flags"):
    st.markdown("""
Allow enabling or disabling features dynamically
without redeploying applications.
""")

# ============================================================
st.subheader("Mental Model Summary")

st.markdown("""
To remember the entire High Level Design stack:

EDGE → TRAFFIC → COMPUTE → DATA → RELIABILITY

or

ENTRY → ROUTE → PROCESS → STORE → PROTECT

This structure works for almost every system design problem
including Instagram, Netflix, Uber, and WhatsApp.
""")