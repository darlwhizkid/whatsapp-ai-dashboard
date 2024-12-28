├── app/
│   ├── __init__.py
│   ├── core/
│   │   ├── config.py        # Configuration settings
│   │   ├── database.py      # Database connections
│   │   └── security.py      # Authentication & security
│   ├── models/
│   │   ├── customer.py      # Customer data models
│   │   ├── ticket.py        # Support ticket models
│   │   └── appointment.py   # Appointment models
│   ├── services/
│   │   ├── whatsapp.py      # WhatsApp integration
│   │   ├── gemini.py        # Gemini AI integration
│   │   ├── slack.py         # Slack notifications
│   │   └── crm.py          # CRM operations
│   └── utils/
│       ├── logger.py        # Logging functionality
│       └── helpers.py       # Helper functions
├── alembic/                 # Database migrations
├── tests/                   # Test cases
└── main.py                 # Application entry point
