# [ShopTrack Documentation](../): Manual API and App Validation

This document provides manual test steps to validate core functionality of the ShopTrack backend.

All tests assume the API server is running locally at `http://127.0.0.1:5000/`.

## 1. Health Check

- [ ] Visit `/` root endpoint
  - Expect: `{"message":"Welcome to ShopTrack API"}`
  - Status code: `200 OK`

## 2. Product Catalog

- [ ] `GET /products/`
  - Expect: JSON array of available products
  - Status code: `200 OK`

## 3. Cart Functionality

- [ ] `GET /cart/` before adding anything
  - Expect: Empty array `[]`
  - Status code: `200 OK`

- [ ] `POST /cart/` to add a product
  - Method: `POST`
  - Body: `{"product_id": 1}`
  - Expect: Product added to cart
  - Status code: `201 Created`

- [ ] `GET /cart/` after adding product
  - Expect: Array containing added product

- [ ] `DELETE /cart/`
  - Expect: Cart cleared (empty array)
  - Status code: `200 OK`

## 4. Checkout

- [ ] Attempt `POST /checkout/` with empty cart
  - Expect: `400 Bad Request`
  - Message: "Cart is empty"

- [ ] Add product to cart, then `POST /checkout/`
  - Expect: JSON with new `order_id`, `items`, and `total_amount`
  - Status code: `201 Created`
  - Cart should be cleared after checkout

## 5. Admin Actions

- [ ] `POST /admin/add-product`
  - Method: `POST`
  - Body: `{"name": "USB-C Cable", "price": 9.99}`
  - Expect: Product added with a new ID
  - Status code: `201 Created`

- [ ] `GET /products/` after adding new product
  - Expect: New product appears in product catalog

## 6. Webhooks (Stub)

- [ ] `POST /webhooks/new-order`
  - Expect: JSON message "Webhook triggered (stub)"
  - Status code: `200 OK`

# Known Limitations

- No authentication or authorization currently implemented
- Data is in-memory only; no persistence across server restarts
- Webhook system is stubbed and does not deliver real HTTP requests yet

# Testing Notes

- Use `curl`, Postman, or any API client
- Ensure correct `Content-Type: application/json` header for all `POST` requests
