# [ShopTrack Documentation](../index.md): Getting Started Guide

Welcome to **ShopTrack**!  
This guide walks you through buying your first product, from browsing available items to completing your first checkout.

Estimated Time: 5–10 minutes  
Skill Level: Beginner

## Prerequisites

Before you begin:

- Ensure the ShopTrack API server is running locally at `http://127.0.0.1:5000/`
- Have a web browser, `curl`, or Postman available for sending API requests
- No account or authentication is required for this walkthrough

## Step 1: Browse Available Products

First, retrieve the current list of products:

```bash
curl http://127.0.0.1:5000/products/
```

You should receive a response like:

```json
[
  {
    "id": 1,
    "name": "Wireless Mouse",
    "price": 29.99
  },
  {
    "id": 2,
    "name": "Mechanical Keyboard",
    "price": 79.99
  },
  {
    "id": 3,
    "name": "HD Monitor",
    "price": 199.99
  }
]
```

Take note of the product `id` you would like to purchase.

## Step 2: Add a Product to Your Cart

Now, add a product to your cart by specifying its `product_id`.

Example: Add the Wireless Mouse (ID 1):

```bash
curl -X POST -H "Content-Type: application/json" -d '{"product_id":1}' http://127.0.0.1:5000/cart/
```

Expected response:

```json
{
  "message": "Product added to cart",
  "cart": [
    {
      "id": 1,
      "name": "Wireless Mouse",
      "price": 29.99
    }
  ]
}
```

## Step 3: View Cart Contents

Verify that your cart contains the correct product:

```bash
curl http://127.0.0.1:5000/cart/
```

Expected response:

```json
[
  {
    "id": 1,
    "name": "Wireless Mouse",
    "price": 29.99
  }
]
```

## Step 4: Complete Your Purchase (Checkout)

Once your cart looks good, complete the checkout process:

```bash
curl -X POST http://127.0.0.1:5000/checkout/
```

Expected response:

```json
{
  "message": "Order placed successfully",
  "order": {
    "order_id": 1234,
    "items": [
      {
        "id": 1,
        "name": "Wireless Mouse",
        "price": 29.99
      }
    ],
    "total_amount": 29.99
  }
}
```

After checkout, the cart will be automatically cleared.

## Troubleshooting

| Issue | Solution |
|:---|:---|
| Cart is empty when checking out | Ensure you have added a product using `POST /cart/` |
| Product not found error | Verify the `product_id` exists by retrieving `/products/` first |
| Server not responding | Ensure the API server is running at `http://127.0.0.1:5000/` |
| Unexpected error | Restart the Flask server and clear the cart |

## What's Next?

Now that you've completed your first purchase:

- Explore adding multiple products before checkout
- Try creating a new product using the `/admin/add-product` endpoint
- Review system behavior during checkout and webhook stubs

Visit the full [documentation](../index.md) for detailed endpoint references.
