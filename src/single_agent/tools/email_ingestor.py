import imaplib
import os
from typing import List, Tuple
from dotenv import load_dotenv
from single_agent.models.models import UserInfo, EmailModel

load_dotenv()  # Load environment variables from .env file


class EmailIngestor:
    def __init__(self):
        # create user info object to store user information
        try:
            self.user_info = UserInfo(
                user_id=os.environ["USER_ID"],
                email=os.environ["EMAIL_ADDRESS"],
                name=os.environ["USER_NAME"]
            )
        except ValueError as e:
            raise ValueError(f"Invalid user information: {e}")
 
    # Connect securely via IMAP
    # Replace with actual password retrieval logic
    def connect_to_email(self) -> None:
        """Connect to the email server using IMAP.
        Raises:
            ConnectionError: If the connection to the email server fails.
        """
        try:
            self.mail = imaplib.IMAP4_SSL(host="imap.gmail.com")
            self.mail.login(user=self.user_info.email, password=str(os.environ["EMAIL_PASSWORD"]))
            self.mail.select(mailbox="inbox")
        except imaplib.IMAP4.error as e:
            raise ConnectionError(f"Failed to connect to email server: {e}")
    
    def fetch_emails(self, search_criteria: str = 'ALL') -> Tuple[str, List[bytes]]:
        """Fetch emails based on search criteria.
        Args:
            search_criteria (str): The IMAP search criteria (default is 'ALL').
        Raises:
            RuntimeError: If there is an error fetching emails.
        """
        try:
            status, messages = self.mail.search(charset=None, criterion=search_criteria)
            if status != "OK":
                raise Exception("Failed to fetch emails.")
            email_ids: List[str] = messages[0].split()
            return status, email_ids
        except Exception as e:
            raise RuntimeError(f"Error fetching emails: {e}")
    
    def map_raw_messsages_to_email_model(self, raw_messages: List[bytes]) -> List[EmailModel]:
        """Map raw email messages to EmailModel.
        Args:
            raw_messages (List[bytes]): List of raw email messages.
        Returns:
            List[EmailModel]: List of EmailModel objects.
        """
        email_models: List[EmailModel] = []
        for raw_message in raw_messages:
            # Here you would parse the raw_message to extract user info
            # For demonstration, we are using the existing user_info
            email_models.append(EmailModel(
                subject="Dummy Subject",
                sender=self.user_info.email,
                date="2024-01-01",
                body=raw_message.decode(encoding="utf-8")
            ))
        return email_models
    