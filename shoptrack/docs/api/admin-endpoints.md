# [ShopTrack Documentation](../index.md): Admin Endpoints

This document describes the administrative API for managing products.

Base URL: `http://127.0.0.1:5000/admin/`

## Add a New Product

Create a new product in the catalog.

### Endpoint

```
POST /admin/add-product
```

### Request

| Method | URL |
|:---|:---|
| POST | `/admin/add-product` |

**Request Body:**

```json
{
  "name": "USB-C Cable",
  "price": 9.99
}
```

| Field | Type | Description |
|:---|:---|:---|
| `name` | String | Name of the new product |
| `price` | Float | Price of the product |

### Response

**Success Response (201 Created)**

```json
{
  "message": "Product added",
  "product": {
    "id": 4,
    "name": "USB-C Cable",
    "price": 9.99
  }
}
```
