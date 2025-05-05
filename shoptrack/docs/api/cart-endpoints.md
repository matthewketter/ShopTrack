# [ShopTrack Documentation](../index.md): Cart Endpoints

This document describes the API endpoints for managing the shopping cart in ShopTrack.

Base URL: `http://127.0.0.1:5000/cart/`

## 1. View Cart Contents

Retrieve all items currently in the user's shopping cart.

### Endpoint

```
GET /cart/
```

### Description

Returns a list of products currently in the cart.

### Request

| Method | URL |
|:---|:---|
| GET | `/cart/` |

No authentication is required.  
No request body is necessary.

### Response

**Success Response (200 OK)**

```json
[
  {
    "id": 1,
    "name": "Wireless Mouse",
    "price": 29.99
  }
]
```

## 2. Add a Product to the Cart

Add a product to the shopping cart.

### Endpoint

```
POST /cart/
```

### Request

| Method | URL |
|:---|:---|
| POST | `/cart/` |

**Request Body:**

```json
{
  "product_id": 1
}
```

| Field | Type | Description |
|:---|:---|:---|
| `product_id` | Integer | ID of the product to add |

### Response

**Success Response (201 Created)**

```json
{
  "message": "Product added to cart",
  "cart": [...]
}
```

**Error Responses:**

| Code | Condition |
|:---|:---|
| 404 Not Found | If the product ID does not exist |

## 3. Clear the Cart

Remove all items from the cart.

### Endpoint

```
DELETE /cart/
```

### Response

**Success Response (200 OK)**

```json
{
  "message": "Cart cleared"
}
```
