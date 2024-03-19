# SharePay 🤝

### Tagline: Simplifying Money Matters with Every Split!

Brief description or overview of your project goes here.

## Setup ⚙️

To run this project, follow these steps:

1. **Setting up Virtual Environment**:
   - Open PowerShell.
   - Run `python -m venv .venv` to create a virtual environment.
   - Run `.venv\Scripts\Activate.ps1` to activate the virtual environment.
   - If you encounter a script running denial/error, run `Set-ExecutionPolicy -Scope CurrentUser Unrestricted` and try activating the virtual environment again.

2. **Install Dependencies**:
   - While in the virtual environment, run:
     ```
     python -m pip install black
     python -m pip install django
     python -m pip install pillow
     ```

3. **Commands**:
   - Run server: `python manage.py runserver`
   - Create a new app: `python manage.py startapp <appName>`

## Authentication System 🔐

### Custom User Model
- Implemented a custom user model to handle logins and logouts.
- Extended the default user model to include additional fields like email, date of birth, etc.
- Avoid running the server or migrations after implementing the custom user model to prevent clashes with existing authentication systems.

## Features Implemented ✨

### Friend System
- Users can send friend requests by entering the recipient's username.
- Friend requests appear on the recipient's home page.
- Recipients can accept or reject friend requests, and senders are notified accordingly.
- Once accepted, the sender and recipient are added to each other's friend lists.

### Notification System
- Implemented a notification system for various events like friend requests, transactions, etc.
- Notifications are categorized and displayed in an off-canvas bar with a badge indicating new notifications.
- Each notification category is clickable and leads to a dedicated page (e.g., friends list, transaction history).

## Styling and Frontend Tasks 🎨

- Styled all pages to ensure consistency and cleanliness.
- Implemented success alerts on form completion using JavaScript to control timing.
- Organized notifications in an off-canvas bar with clickable categories.
- Designed a unique layout for displaying friends and transaction history using a wheel-like scroll.

## Planned Enhancements 🚧

- Add more functionality such as sending money between friends.
- Further refine styling and frontend design for a polished user experience.

## Additional Notes ℹ️

Include any additional notes or thoughts about the project here.

---

Feel free to adjust or expand upon this template based on your project's specific details and requirements.
