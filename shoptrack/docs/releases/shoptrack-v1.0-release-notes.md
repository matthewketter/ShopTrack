# [ShopTrack Documentation](../): Release Notes

## Version 1.0.0

**Release Date:** April 28, 2025

## Overview

This is the first public release of **ShopTrack**, a lightweight e-commerce and order management platform designed for small to mid-sized businesses.

ShopTrack provides a streamlined shopping experience for customers and efficient operational management tools for administrators.

This release includes all core functionality necessary to support a basic e-commerce workflow, from browsing products to placing and managing orders.

## New Features

| Feature | Description |
|:---|:---|
| Product Catalog | Customers can browse available products with name and pricing details. |
| Shopping Cart | Customers can add products to a cart, view cart contents, and clear the cart. |
| Checkout Process | Customers can complete purchases and generate a basic order summary. |
| Admin Product Management | Admins can add new products to the catalog via API. |
| Webhook Simulation | Stubs are available to simulate webhook notifications on new orders. |

## API Endpoints

| Endpoint | Method | Description |
|:---|:---|:---|
| `/products/` | GET | Retrieve available products |
| `/cart/` | GET | View cart contents |
| `/cart/` | POST | Add product to cart |
| `/cart/` | DELETE | Clear the cart |
| `/checkout/` | POST | Complete checkout and create order |
| `/admin/add-product` | POST | Add a new product (Admin only) |
| `/webhooks/new-order` | POST | Simulate webhook for new order |

Full [documentation](../) is available.

## Known Limitations

- No authentication or authorization currently implemented (admin and user actions are unsecured)
- No database or persistent storage (cart and products exist in-memory only)
- No payment gateway integration (checkout is a simulated order process)
- Webhook system is stubbed; no actual HTTP calls are sent externally
- No pagination or filtering on the product catalog
- No order history tracking after checkout (orders are ephemeral)

## Planned Future Enhancements

- User authentication and role-based access control (Admin vs Customer)
- Persistent data storage using a database
- Integration with external payment gateways
- Full webhook delivery support with retry logic
- Search, filtering, and pagination for product catalog
- Order history and customer account features

# Support

For feedback, bug reports, or feature requests, please open an issue in the [ShopTrack GitHub repository](https://github.com/matthewketter/ShopTrack).
