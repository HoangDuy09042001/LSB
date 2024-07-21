# import tkinter as tk
# from tkinter import filedialog, messagebox
# from tkinter import ttk
# import shutil
# from encoding import encode_message
# from decoding import decode_message
# import os

# def process_encode_audio_and_text(audio_path, text):
#     if not audio_path or not text:
#         messagebox.showerror("Error", "Please provide both audio and text")
#         return None

#     # Save the audio file to input.wav
#     encode_dir = "data/encode"
#     os.makedirs(encode_dir, exist_ok=True)
#     input_audio_path = os.path.join(encode_dir, "input.wav")
#     output_audio_path = os.path.join(encode_dir, "output.wav")
#     shutil.copy(audio_path, input_audio_path)
    
#     encode_message(audio_file=input_audio_path, message=text, output_file=output_audio_path)
#     messagebox.showinfo("Success", f"Audio encoded and saved at {output_audio_path}")

#     return output_audio_path

# def process_decode_audio_and_text(audio_path):
#     if not audio_path:
#         messagebox.showerror("Error", "Please provide an audio file")
#         return

#     decode_dir = "data/decode"
#     os.makedirs(decode_dir, exist_ok=True)
#     input_audio_path = os.path.join(decode_dir, "input.wav")
#     shutil.copy(audio_path, input_audio_path)
    
#     output_text = decode_message(audio_file=input_audio_path)
#     return output_text

# def select_audio_file(entry):
#     audio_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
#     entry.delete(0, tk.END)
#     entry.insert(0, audio_path)

# def save_encoded_file(output_path):
#     if output_path:
#         save_path = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("Audio Files", "*.wav")])
#         if save_path:
#             shutil.copy(output_path, save_path)
#             messagebox.showinfo("Saved", f"File saved at {save_path}")

# def encode_audio():
#     audio_path = audio_entry.get()
#     text = text_entry.get()
#     output_path = process_encode_audio_and_text(audio_path, text)
#     if output_path:
#         save_encoded_file(output_path)

# def decode_audio():
#     audio_path = decode_audio_entry.get()
#     hidden_message = process_decode_audio_and_text(audio_path)
#     decode_text_entry.delete(0, tk.END)
#     decode_text_entry.insert(0, hidden_message)

# root = tk.Tk()
# root.title("Audio Steganography")

# # Encoder
# encoder_frame = ttk.LabelFrame(root, text="Encoder", padding=(20, 10))
# encoder_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# ttk.Label(encoder_frame, text="Upload Audio").grid(row=0, column=0, padx=5, pady=5)
# audio_entry = ttk.Entry(encoder_frame, width=40)
# audio_entry.grid(row=0, column=1, padx=5, pady=5)
# ttk.Button(encoder_frame, text="Browse", command=lambda: select_audio_file(audio_entry)).grid(row=0, column=2, padx=5, pady=5)

# ttk.Label(encoder_frame, text="Enter Text").grid(row=1, column=0, padx=5, pady=5)
# text_entry = ttk.Entry(encoder_frame, width=40)
# text_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

# ttk.Button(encoder_frame, text="Encode", command=encode_audio).grid(row=2, column=1, columnspan=2, pady=10)

# # Decoder
# decoder_frame = ttk.LabelFrame(root, text="Decoder", padding=(20, 10))
# decoder_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# ttk.Label(decoder_frame, text="Upload Audio").grid(row=0, column=0, padx=5, pady=5)
# decode_audio_entry = ttk.Entry(decoder_frame, width=40)
# decode_audio_entry.grid(row=0, column=1, padx=5, pady=5)
# ttk.Button(decoder_frame, text="Browse", command=lambda: select_audio_file(decode_audio_entry)).grid(row=0, column=2, padx=5, pady=5)

# ttk.Button(decoder_frame, text="Decode", command=decode_audio).grid(row=1, column=1, columnspan=2, pady=10)

# ttk.Label(decoder_frame, text="Hidden Message").grid(row=2, column=0, padx=5, pady=5)
# decode_text_entry = ttk.Entry(decoder_frame, width=40)
# decode_text_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

# root.mainloop()




import tkinter as tk
from tkinter import ttk
import webview

def create_browser(url):
    # Create a webview window with the given URL
    global browser
    browser = webview.create_window("Embedded Browser", url, width=800, height=600)
    webview.start()

def load_url():
    url = url_entry.get()
    if url:
        # Load the URL into the existing webview window
        if browser:
            browser.load_url(url)

# Create the main window
root = tk.Tk()
root.title("Tkinter Browser")

# Create a frame for the URL entry and load button
top_frame = ttk.Frame(root, padding="10")
top_frame.pack(side=tk.TOP, fill=tk.X)

# URL entry
url_entry = ttk.Entry(top_frame, width=50)
url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Load button
load_button = ttk.Button(top_frame, text="Load URL", command=load_url)
load_button.pack(side=tk.LEFT)

# Initialize browser as None
browser = None

# Start the webview browser window with the provided URL
create_browser("http://127.0.0.1:7860")

# Start the Tkinter main loop
root.mainloop()



