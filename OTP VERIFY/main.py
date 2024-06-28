import random

# Function to generate a 6-digit OTP
def generate_otp():
    return random.randint(100000, 999999)

# Assume sending OTP functionality here
def send_otp(otp):
    print("OTP sent successfully: ", otp)  # You can modify this to send OTP using email or SMS

# Validate OTP
def validate_otp(otp_entered, otp_generated):
    return otp_entered == otp_generated

# Main code
# Generate OTP
otp = generate_otp()

# Sending OTP
send_otp(otp)

# Simulating OTP verification
otp_entered = int(input("Enter the OTP you received: "))

# Validate OTP
if validate_otp(otp_entered, otp):
    print("OTP verification successful!")
else:
    print("OTP verification failed. Please try again.")
