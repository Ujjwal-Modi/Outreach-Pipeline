# 🚀 Automated Outreach Pipeline

> Transform a single company domain into qualified prospects and personalized outreach in minutes.

[![Live Demo](https://img.shields.io/badge/Live-Demo-success?style=for-the-badge)](https://outreach-pipeline-ten.vercel.app/)
[![Backend API](https://img.shields.io/badge/Backend-Render-blue?style=for-the-badge)](https://outreach-pipeline-n941.onrender.com)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge\&logo=github)](https://github.com/Ujjwal-Modi/Outreach-Pipeline)

![GitHub last commit](https://img.shields.io/github/last-commit/Ujjwal-Modi/Outreach-Pipeline)
![GitHub repo size](https://img.shields.io/github/repo-size/Ujjwal-Modi/Outreach-Pipeline)
![GitHub top language](https://img.shields.io/github/languages/top/Ujjwal-Modi/Outreach-Pipeline)

---

## 🌐 Live Links

### Frontend (Vercel)

https://outreach-pipeline-ten.vercel.app/

### Backend API (Render)

https://outreach-pipeline-n941.onrender.com

### GitHub Repository

https://github.com/Ujjwal-Modi/Outreach-Pipeline

---

# ⚡ Quick Demo

```text
Input Company Domain
        ↓
Find Similar Companies
        ↓
Discover Decision Makers
        ↓
Retrieve LinkedIn Profiles
        ↓
Resolve Work Emails
        ↓
Review Campaign
        ↓
Send Personalized Outreach
```

---

# 📖 Overview

Sales teams spend countless hours researching prospects, identifying decision-makers, finding verified emails, and manually sending outreach campaigns.

This process is repetitive, time-consuming, and difficult to scale.

**Automated Outreach Pipeline** automates the entire outbound prospecting workflow by transforming a single company domain into qualified prospects and ready-to-send outreach campaigns.

The user provides one input:

```text
company-domain.com
```

The platform handles everything else automatically.

---

# ❌ The Problem

Modern sales prospecting is fragmented across multiple tools.

A typical workflow looks like:

1. Search for similar companies
2. Research potential prospects
3. Find LinkedIn profiles
4. Discover work email addresses
5. Verify email validity
6. Create outreach campaigns
7. Send emails manually

This results in:

📉 Lower sales productivity

📉 Delayed outreach execution

📉 Lost opportunities

📉 High operational costs

📉 Repetitive manual work

📉 Limited scalability

A task that should take minutes often takes hours.

---

# 💡 Solution

Automated Outreach Pipeline combines prospect discovery, contact enrichment, and outreach automation into a single workflow.

### Input

```text
stripe.com
```

### Output

```text
✔ Similar Companies

✔ Senior Decision Makers

✔ LinkedIn Profiles

✔ Verified Work Emails

✔ Outreach Ready Contacts

✔ Email Campaign Delivery
```

No copy-pasting.

No spreadsheet juggling.

No switching between multiple tools.

---

# 🎯 Key Features

### Prospect Discovery

* Similar company identification
* Lookalike company generation
* Automated company research

### Contact Discovery

* CEO identification
* Founder discovery
* VP-level contact discovery
* Director-level prospecting

### Contact Enrichment

* LinkedIn profile retrieval
* Professional email discovery
* Contact validation

### Outreach Automation

* Campaign preparation
* Email delivery
* Brevo integration

### User Experience

* Modern React interface
* One-click workflow execution
* Human review before sending
* Real-time results

### Reliability

* Error handling
* API failure recovery
* Modular architecture
* Safe email workflow

---

# 🔄 Workflow

## Stage 1 – Similar Company Discovery

### Service

Ocean.io

### Responsibility

Discover companies that resemble the input company based on:

* Industry
* Market Position
* Company Characteristics
* Firmographics

### Input

```text
company.com
```

### Output

```text
Company A
Company B
Company C
...
```

---

## Stage 2 – Decision Maker Discovery

### Service

Prospeo

### Responsibility

Identify senior decision-makers for each discovered company.

### Typical Roles

* Founder
* CEO
* CTO
* COO
* VP Engineering
* VP Product
* VP Operations
* Directors

### Output

```text
Name
Role
LinkedIn URL
```

---

## Stage 3 – Contact Enrichment

### Responsibility

Resolve professional email addresses for discovered contacts.

### Output

```text
john.doe@company.com
```

Verified work email addresses ready for outreach.

---

## Stage 4 – Review Layer

Before sending emails, users can review:

* Companies
* Prospects
* Email Addresses
* Campaign Data

This acts as a safety checkpoint before delivery.

---

## Stage 5 – Email Delivery

### Service

Brevo

### Responsibility

Send outreach emails to verified prospects automatically.

---

# ⚙️ System Design

The platform follows a modular pipeline architecture.

Each stage is isolated and responsible for a specific business function.

```text
Company Domain
      ↓
Company Discovery
      ↓
Prospect Discovery
      ↓
Contact Enrichment
      ↓
Review Layer
      ↓
Email Delivery
```

## Why This Architecture?

### Scalability

Each service can be scaled independently.

### Maintainability

Business logic remains separated and easy to modify.

### Reliability

Failures in one stage do not require redesigning the entire workflow.

### Extensibility

New providers and integrations can be added with minimal effort.

Examples:

* CRM Integrations
* Additional Prospecting APIs
* Lead Scoring Systems
* AI Personalization Engines
* Multi-Channel Outreach

---

# 🧠 Engineering Decisions

## Safety Checkpoint

A review step was intentionally introduced before sending emails.

Benefits:

* Prevent accidental outreach
* Validate prospect data
* Improve campaign quality
* Save email credits

---

## Credit Optimization

The architecture supports significantly larger prospecting campaigns.

For demonstration purposes:

```text
Maximum Companies = 2

Maximum Prospects Per Company = 2
```

Reason:

* Faster demo execution
* Free-tier rate limits
* Reduced API costs
* Credit conservation

Removing these limits enables larger-scale prospecting campaigns.

---

## Fault Tolerance

The pipeline is designed to handle:

* Missing contacts
* Partial API responses
* Failed requests
* Empty datasets
* Invalid data

without crashing the entire workflow.

---

# 🛠️ Tech Stack

## Frontend

* React
* Vite
* Tailwind CSS
* Axios
* JavaScript

## Backend

* FastAPI
* Python

## APIs

* Ocean.io
* Prospeo
* Brevo

## Communication

* REST APIs
* JSON Data Exchange

## Deployment

### Frontend

Vercel

### Backend

Render

---

# 🔌 API Integrations

## Ocean.io

### Purpose

Find companies similar to a target organization.

### Documentation

https://app.ocean.io/docs/getting-started/authentication

### Flow

```text
Seed Domain
     ↓
Ocean.io
     ↓
Similar Companies
```

---

## Prospeo

### Purpose

Discover decision-makers and LinkedIn profiles.

### Documentation

https://prospeo.io/api-docs

### Flow

```text
Company Domain
      ↓
Prospeo
      ↓
Prospect Details
```

---

## Brevo

### Purpose

Send outreach campaigns.

### Documentation

https://developers.brevo.com/docs/getting-started

### Flow

```text
Verified Contacts
        ↓
Brevo
        ↓
Emails Sent
```

---

# 🚀 Local Setup

## Clone Repository

```bash
git clone https://github.com/Ujjwal-Modi/Outreach-Pipeline.git

cd Outreach-Pipeline
```

---

## Backend Setup

```bash
cd Backend

pip install -r requirements.txt
```

Create `.env`

```env
OCEAN_API_KEY=

PROSPEO_API_KEY=

BREVO_API_KEY=

FROM_NAME=

FROM_EMAIL=
```

Run Backend

```bash
uvicorn main:app --reload
```

---

## Frontend Setup

```bash
cd Frontend

npm install

npm run dev
```

---

# 📈 Scalability

Current Demo Configuration

```text
2 Companies

2 Prospects Per Company
```

These limits only exist for:

* Demo purposes
* Free-tier restrictions
* Faster execution
* API credit conservation

The architecture itself can support:

* Hundreds of companies
* Thousands of prospects
* Bulk outreach campaigns
* CRM integrations
* Scheduled outreach
* Multi-channel automation

---

# 💼 Business Value

### For Startups

Generate qualified leads faster.

### For Agencies

Scale outbound prospecting.

### For Sales Teams

Reduce manual prospecting effort.

### For Founders

Reach decision-makers efficiently.

### For B2B Organizations

Increase outreach volume without increasing operational workload.

---

# 🏆 Key Achievements

✅ Built a Full-Stack Sales Automation Platform

✅ Integrated Multiple Third-Party APIs

✅ Automated End-to-End Prospecting Workflow

✅ Implemented Safe Email Delivery Process

✅ Designed Modular Pipeline Architecture

✅ Built Production-Ready Frontend and Backend

✅ Solved a Real-World Sales Automation Problem

✅ Reduced Manual Prospecting Effort Significantly

---

# 🔮 Future Enhancements

* CRM Integrations
* Campaign Analytics
* AI Personalization
* Lead Scoring
* Multi-Channel Outreach
* LinkedIn Messaging Automation
* Automated Follow-Ups
* Workflow Scheduling
* Bulk Prospect Uploads

---

# 👨‍💻 Author

## Ujjwal Modi

B.Tech Computer Science Engineering
KIIT University

📧 Email

[ujjawalmodi321@gmail.com](mailto:ujjawalmodi321@gmail.com)

🔗 LinkedIn

https://www.linkedin.com/in/ujjawalmodi/

🔗 GitHub

https://github.com/Ujjwal-Modi

🔗 Portfolio

https://portfolio-six-ochre-77.vercel.app/

---

# ⭐ Support

If you found this project interesting, consider giving it a star on GitHub.

It helps others discover the project and supports future development.

---

<p align="center">

<b>One Domain → Similar Companies → Decision Makers → Verified Emails → Outreach Sent 🚀</b>

</p>
