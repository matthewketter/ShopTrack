# [ShopTrack Documentation](../): Product Catalog Endpoints

This document describes the API endpoints related to browsing and managing the product catalog in ShopTrack.

Base URL: `http://127.0.0.1:5000/products/`

## 1. List All Products

Retrieve the full list of available products.

### Endpoint

```
GET /products/
```

### Description

Returns a list of products currently available in the catalog.

### Request

| Method | URL |
|:---|:---|
| GET | `/products/` |

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
| Field | Type | Description |
| ----- | ----- | ----- |
| `id` | Integer | Unique identifier for the product |
| `name` | String | Name of the product |
| `price` | Number (Float) | Price of the product in USD |

### **Error Responses**

| Code | Condition | Example Response |
| ----- | ----- | ----- |
| 500 Internal Server Error | If the server encounters an unexpected condition | `{ "error": "Internal Server Error" }` |

## **2. Notes**

* The product list is static unless modified via admin endpoints.
* All prices are displayed in US dollars (USD).
* No filtering or pagination is currently implemented.

Future enhancements may include:
* Product search and filtering
* Sorting by price or category
* Pagination of large product catalogs  
