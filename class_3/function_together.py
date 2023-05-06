# function for sending an email
def send_email(to, /, subject, body, *, cc=None, bcc=None):
    print(f"Sending email to: {to}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    if cc:
        print(f"Cc: {cc}")
    if bcc:
        print(f"Bcc: {bcc}")

# Using the send_email() function with standard, position-only, and keyword-only arguments
send_email("michael@example.com", "Hello, Michael!", "I hope this emails finds you well.", cc="bob@example.com")