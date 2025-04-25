# EC530-Assignment2

A lightweight, in-memory REST API to manage Users, Houses, Rooms, and Devices, built with FastAPI.
Supports full CRUD operations and offers automatic API documentation via Swagger UI.

## Features
- Built with FastAPI (fast, modern, async support).
- CRUD operations for:
  - Users
  - Houses (owned by users)
  - Rooms (inside houses)
  - Devices (inside rooms)
- In-memory storage (no database needed).
- Automatically generated Swagger UI and ReDoc docs.
- Full Pytest test suite with TestClient using httpx.
- Easily extendable into a real-world production app.
