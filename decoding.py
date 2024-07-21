import wave

def bin_to_int(b):
    # Converts a binary string to an integer
    return int(b, 2)
# def decode_message(audio_file):
#     # Load the audio file
#     audio = wave.open(audio_file, 'rb')
#     frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    
#     # Extract the least significant bit of each byte in the audio data
#     message_bits = [str(frame_bytes[i] & 1) for i in range(len(frame_bytes))]
    
#     # Convert the binary string to a message
#     message = ''.join([chr(bin_to_int(''.join(message_bits[i:i+8]))) for i in range(0, len(message_bits), 8)])
    
#     # Find the delimiter to get the actual message
#     delimiter_index = message.find('###')
#     if delimiter_index != -1:
#         message = message[:delimiter_index]
#     else:
#         print("No hidden message found.")
#         return
    
#     print("Decoded message:", message)
#     audio.close()
#     return message


def decode_message(audio_file):
    # Load the audio file
    audio = wave.open(audio_file, 'rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    
    # Extract the least significant bit of each byte in the audio data
    message_bits = [str(frame_bytes[i] & 1) for i in range(len(frame_bytes))]
    
    # Convert the binary string to bytes
    message_bytes = bytearray([bin_to_int(''.join(message_bits[i:i+8])) for i in range(0, len(message_bits), 8)])
    
    # Find the delimiter to get the actual message
    delimiter_index = message_bytes.find(b'###')
    if delimiter_index != -1:
        message_bytes = message_bytes[:delimiter_index]
        message = message_bytes.decode('utf-8')
    else:
        print("No hidden message found.")
        return
    
    print("Decoded message:", message)
    audio.close()
    return message




