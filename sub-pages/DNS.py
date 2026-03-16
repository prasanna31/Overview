import streamlit as st

st.set_page_config(page_title="DNS Explained", layout="wide")

st.title("DNS – Domain Name System")

st.markdown("""
DNS is one of the most important systems on the internet.

Without DNS, users would have to remember long IP addresses
instead of simple website names.

Example:

Instead of typing

142.250.190.14

we simply type

google.com

DNS converts the website name into the correct IP address.
""")

# ----------------------------------------------------------

st.header("1. What is DNS")

st.markdown("""
DNS stands for **Domain Name System**.

It is a system that converts **domain names** into **IP addresses**.

Computers communicate using IP addresses.

Humans prefer easy names.

DNS connects these two worlds.

Example:

google.com → 142.250.190.14  
youtube.com → 142.250.183.206
""")

# ----------------------------------------------------------

st.header("2. Simple Analogy")

st.markdown("""
Think of DNS like a **phone contact list**.

Instead of remembering a phone number, we remember a name.

Example:

Prasad → 9876543210

Similarly:

google.com → 142.250.190.14

DNS is basically the **contact list of the internet**.
""")

# ----------------------------------------------------------

st.header("3. Why DNS is Needed")

st.markdown("""
Imagine if DNS did not exist.

To visit websites we would need to type IP addresses.

Example:

Instead of

google.com

we would type

142.250.190.14

Now imagine remembering IP addresses for thousands of websites.

DNS solves this problem by mapping names to IP addresses.
""")

# ----------------------------------------------------------

st.header("4. Important DNS Components")

st.subheader("Domain Name")

st.markdown("""
A domain name is the human readable website name.

Example:

amazon.com  
netflix.com  
facebook.com
""")

st.subheader("IP Address")

st.markdown("""
The actual address of a server on the internet.

Example:

172.217.160.142

Servers communicate using IP addresses.
""")

st.subheader("DNS Resolver")

st.markdown("""
A DNS resolver finds the IP address for a domain name.

Usually provided by:

• Internet Service Provider  
• Google DNS (8.8.8.8)  
• Cloudflare DNS (1.1.1.1)
""")

st.subheader("Root DNS Server")

st.markdown("""
Root servers are the top level DNS servers.

They help direct requests to the correct domain servers.
""")

st.subheader("TLD Server")

st.markdown("""
TLD means Top Level Domain.

Examples:

.com  
.org  
.net  
.in

These servers manage domains under that extension.
""")

st.subheader("Authoritative DNS Server")

st.markdown("""
This server contains the final mapping between
domain name and IP address.

Example:

netflix.com → 52.89.124.15
""")

# ----------------------------------------------------------

st.header("5. DNS Resolution Process (Step by Step)")

st.markdown("""
Let us understand what happens when a user types a website.
""")

st.markdown("""
Step 1 – User enters URL

Example:

www.netflix.com

Step 2 – Browser checks local cache

If the IP address is already stored locally,
the browser uses it directly.

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
""")

# ----------------------------------------------------------

st.header("6. DNS Caching")

st.markdown("""
DNS caching stores recently used domain lookups.

This speeds up future requests.

Caching can happen in:

• Browser cache  
• Operating system cache  
• ISP DNS cache

Example:

If you visited youtube.com recently,
the IP address may already be stored locally.
""")

# ----------------------------------------------------------

st.header("7. Types of DNS Records")

st.subheader("A Record")

st.markdown("""
Maps domain name to IPv4 address.

Example:

example.com → 93.184.216.34
""")

st.subheader("AAAA Record")

st.markdown("""
Maps domain name to IPv6 address.
""")

st.subheader("CNAME Record")

st.markdown("""
Creates an alias for another domain.

Example:

www.example.com → example.com
""")

st.subheader("MX Record")

st.markdown("""
Specifies mail servers for email delivery.
""")

st.subheader("TXT Record")

st.markdown("""
Stores text information for verification
and security purposes.
""")

# ----------------------------------------------------------

st.header("8. Real World Example")

st.markdown("""
User opens browser and types:

amazon.com

DNS converts the domain to an IP address.

Example:

amazon.com → 54.239.28.85

Browser connects to that server.

The server sends back the website data,
and the page loads for the user.
""")

# ----------------------------------------------------------

st.header("9. Simple Memory Trick")

st.markdown("""
Remember this simple flow:

User → Browser → DNS Resolver → Root Server → TLD Server → Authoritative Server → IP Address → Website Loads

If you remember this chain,
you can explain DNS clearly in interviews.
""")