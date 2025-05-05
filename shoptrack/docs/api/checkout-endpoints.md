# [ShopTrack Documentation](../index.md): Checkout Endpoint

This document describes the checkout API used to finalize purchases.

Base URL: `http://127.0.0.1:5000/checkout/`

## Checkout and Place an Order

Create a new order from the contents of the shopping cart.

### Endpoint

```
POST /checkout/
```

### Description

Completes the purchase and clears the shopping cart.

### Request

| Method | URL |
|:---|:---|
| POST | `/checkout/` |

No request body is required.

### Response

**Success Response (201 Created)**

```json
{
  "message": "Order placed successfully",
  "order": {
    "order_id": 1234,
    "items": [...],
    "total_amount": 59.98
  }
}
```

**Error Responses:**

| Code | Condition |
|:---|:---|
| 400 Bad Request | Cart is empty |
