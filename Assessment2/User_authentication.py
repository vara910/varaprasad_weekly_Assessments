from abc import ABC, abstractmethod

class UserAuthentication(ABC):
    @abstractmethod
    def login(self, username, password):
        pass

    @abstractmethod
    def logout(self):
        pass

class GoogleAuth(UserAuthentication):
    def login(self, username, password):
        return f"User {username} logged in with Google."

    def logout(self):
        return "User logged out from Google."
    
class FacebookAuth(UserAuthentication):
    def login(self, username, password):
        return f"User {username} logged in with Facebook."

    def logout(self):
        return "User logged out from Facebook."

google_auth = GoogleAuth()
facebook_auth = FacebookAuth()

print(google_auth.login("Alice", "password123")) 
print(facebook_auth.logout())