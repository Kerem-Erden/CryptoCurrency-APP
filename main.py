import requests
import tkinter
from PIL import ImageTk, Image

# Initialize the main window
window = tkinter.Tk()
window.title("Crypto Widget")
window.minsize(200, 100)

# Load and display the image
img = Image.open("coin.png")
photo = ImageTk.PhotoImage(img)
image_label = tkinter.Label(window, image=photo)
image_label.pack()

# Input label
input_label = tkinter.Label(window, text="Enter cryptocurrency name: ")
input_label.pack()

# Input entry
input_entry = tkinter.Entry(window)
input_entry.pack()

# Result label
result_label = tkinter.Label(window, text="")
result_label.config(pady=10)
result_label.pack()

# Fetch cryptocurrency data
response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false")

def get_crypto_data():
    if response.status_code == 200:
        return response.json()
    else:
        return []

crypto_response = get_crypto_data()


# Function to display cryptocurrency price
def print_crypto_price():
    crypto_name = input_entry.get().lower()
    for crypto in crypto_response:
        if crypto['name'].lower() == crypto_name:
            price = crypto['current_price']
            result_label.config(text=f"The price of {crypto['name']} is ${price}")
            return
    result_label.config(text="Cryptocurrency not found please try again.")

# Price button
price_button = tkinter.Button(window, text="Price", command=print_crypto_price)
price_button.pack()

# Run the application
window.mainloop()
