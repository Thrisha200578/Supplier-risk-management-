# Supplier-risk-management-
Suppliers risk  management for dropshipping where  the dropshippers find suppliers based on sentiment analysis
SupplyChain AI — Dropshipper Interface

Overview
Suppliers risk  management for dropshipping is a front-end prototype designed to support dropshippers in discovering verified manufacturers, evaluating supplier reliability using AI-driven insights, managing orders, and providing feedback.
The system demonstrates an integrated workflow covering supplier search, risk analysis, order tracking, and review submission.

This project is implemented as a client-side web interface using HTML, CSS, and JavaScript.

---

Features

1. Authentication

- Separate login page for user authentication
- Validates credentials before granting access
- Controls entry into seller dashboard modules

---

2. Seller Dashboard

Provides an overview of platform capabilities:

- Verified Manufacturer discovery
- AI Sentiment Analysis insights
- Risk Scoring evaluation
- Smart Order Tracking access

This acts as the main navigation hub.

---

3. Manufacturer Search Interface

Allows dropshippers to find suppliers.

Capabilities

- Text-based product search
- Image upload search simulation
- Sorting options:
  - Rating
  - AI Sentiment
  - Risk Level

Manufacturer Cards Display

- Location
- Rating
- Sentiment classification
- Risk label
- Industry tags
- Actions:
  - View Details
  - Contact Supplier
  - Place Order (enhanced)

---

4. Orders Management Interface

Order Summary

- Total Orders
- In Transit
- Delivered

Order List

Each order displays:

- Product details
- Manufacturer information
- Quantity
- Delivery status updates

Expanded Order Details

- Tracking number
- Estimated delivery
- Timeline progress visualization
- Cancel request option
- Reorder functionality

---

5. Review Submission

- Submit feedback after order completion
- Helps evaluate supplier performance
- Simulates data contribution for AI sentiment scoring

---

6. Notification System

- Bell icon alert center
- Displays system events:
  - Order placed
  - Cancellation requested
  - Review submitted
- Unread notification counter

---

Technology Stack

- HTML5
- CSS3
- Vanilla JavaScript
- No external frameworks
- Client-side simulation only

---

Project Structure

Single-file modular interface approach:

- login.html
- seller.html
- traildropship.html (search & orders views)
- Embedded styles and scripts

---

Workflow (DFD Alignment)

1. User logs in
2. Searches manufacturers
3. Selects supplier
4. Places/Tracks orders
5. Submits reviews
6. Receives notifications

---

Limitations

- No backend integration
- Data stored temporarily in memory
- AI scoring simulated
- Messaging and order placement are frontend mock implementations

---

Future Improvements

- Backend database integration
- Real supplier communication
- Payment gateway support
- Real logistics tracking API
- Machine learning-based scoring models

---

Author

Student Project — Supplier Risk Management for Dropshipping
