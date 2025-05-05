# [ShopTrack Documentation](../index.md): Webhook Endpoints

This document describes the stub webhook API used to simulate external event notifications.

Base URL: `http://127.0.0.1:5000/webhooks/`

## Simulate New Order Webhook

Simulate sending a webhook notification when a new order is placed.

### Endpoint

```
POST /webhooks/new-order
```

### Description

Triggers a simulated webhook call (stubbed response).

### Request

| Method | URL |
|:---|:---|
| POST | `/webhooks/new-order` |

No request body is required.

### Response

**Success Response (200 OK)**

```json
{
  "message": "Webhook triggered (stub)"
}
```
