def get_input(prompt, valid_responses=None):
    while True:
        user_input = input(prompt).strip().lower()

        if valid_responses is None or user_input in valid_responses:
            return user_input
        else:
            print("Sorry, I didn’t understand that. Please try again.")

def wifi_troubleshoot_chatbot():
    print("👋 Hi! I'm your Wi-Fi Troubleshooting Assistant.")
    print("Let's see if we can fix your Wi-Fi issue together.")

    power = get_input("📶 Is your router plugged in and showing lights? (yes/no): ", ["yes", "no"])
    
    if power == "no":
        print("🔌 Please plug in your router and wait for the lights to turn on. That may solve the problem!")
        return

    connection_type = get_input("🖥️ Are you using Wi-Fi or Ethernet? (wifi/ethernet): ", ["wifi", "ethernet"])
    
    if connection_type == "ethernet":
        print("🔧 Try using a different Ethernet cable or port on the router.")
        return
    
    other_devices = get_input("📱 Can other devices connect to the Wi-Fi? (yes/no): ", ["yes", "no"])
    
    if other_devices == "yes":
        print("🤖 It might be an issue with your device. Try restarting it or forgetting and rejoining the network.")
        return
    
    reboot = get_input("🔁 Have you tried rebooting your router? (yes/no): ", ["yes", "no"])
    
    if reboot == "no":
        print("🛠️ Please try unplugging the router for 30 seconds, then plug it back in.")
        return

    print("📡 If none of this worked, the issue might be with your internet provider. Contact them for further help.")

# Run the chatbot
if __name__ == "__main__":
    wifi_troubleshoot_chatbot()
