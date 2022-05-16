# Zoho Subscriptions Python Client Library

An Open source Python Client Library for integrating with Zoho Subscriptions Billing Solution

## Installation

Install the latest version 1.0.0 of the library with the following commands:

    $ pip install 'subscriptions-v1.0.0-py3-none-any.whl'

## Usage
Import the Zoho Subscriptions Python Client Library to your project

### Setup

**Setup Organization Id and OAuth Access Token**

1. Get Organization Id <a href="https://www.zoho.com/subscriptions/api/v1/#organization-id">refer</a>
2. Generate oauth token using <a href="https://www.zoho.com/subscriptions/api/v1/oauth/#overview">API Reference</a>

##### Sample Code:

<pre><code> from subscriptions import ZSClient

object = ZSClient()
object.set_oathtoken("{{Zoho Subscriptions Oauth Token}}")
object.set_organization_id("{{Zoho Organization Id}}")
object.set_host("{{Host name}}")
</code></pre>

## How to use

Use the below sample code for Customer Creation refer <a href="https://www.zoho.com/subscriptions/api/v1/customers/#create-a-customer">Api Docs</a>

Example to create a Customer:

<pre><code>from subscriptions import Customer

object = ZSClient()
object.set_oathtoken("{{Zoho Subscriptions Oauth Token}}")
object.set_organization_id("{{Zoho Organization Id}}")\
object.set_host("{{Host name}}")

customer = Customer()
customer.set_display_name("Patricia Boyale")
customer.set_email("patricia.boyale@zylker.com")
customer.set_phone("98765543210")

print(Customer.create(customer))
</code></pre>

## License

See the LICENCE file
