import re

def assess_password_strength(password):
    strength = 0
    feedback = []
    
    # Criteria
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if any(char.islower() for char in password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    if any(char.isupper() for char in password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")
    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character (!@#$%^&*(),.?\":{}|<>).")
    
    # Strength assessment
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    
    return strength_levels[strength], feedback

# Example Usage
password = input("Enter a password to assess: ")
strength, suggestions = assess_password_strength(password)
print(f"Password Strength: {strength}")
if suggestions:
    print("Suggestions:")
    for suggestion in suggestions:
        print(f"- {suggestion}")
