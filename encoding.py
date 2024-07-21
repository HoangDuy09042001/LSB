import wave
from pydub import AudioSegment
def int_to_bin(i):
    # Converts an integer to a binary string
    return bin(i)[2:].zfill(8)

def bin_to_int(b):
    # Converts a binary string to an integer
    return int(b, 2)

def convert_mp3_to_wav(mp3_file, wav_file):
    # Convert MP3 to WAV
    audio = AudioSegment.from_mp3(mp3_file)
    audio.export(wav_file, format="wav")
    print(f"Converted {mp3_file} to {wav_file}")
def encode_message(audio_file, message, output_file):
    if audio_file.lower().endswith('.mp3'):
        wav_file = audio_file.rsplit('.', 1)[0] + '.wav'
        convert_mp3_to_wav(audio_file, wav_file)
        audio_file = wav_file
    # Load the audio file
    audio = wave.open(audio_file, 'rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    
    # Encode the message in UTF-8 and add a delimiter
    message_bytes = message.encode('utf-8') + b'###'
    
    # Convert the message bytes to a binary string
    message_bits = ''.join([int_to_bin(byte) for byte in message_bytes])
    
    # Modify the least significant bit of each byte in the audio data
    for i in range(len(message_bits)):
        frame_bytes[i] = (frame_bytes[i] & 254) | int(message_bits[i])
    
    # Write the modified audio data to the output file
    frame_modified = bytes(frame_bytes)
    with wave.open(output_file, 'wb') as fd:
        fd.setparams(audio.getparams())
        fd.writeframes(frame_modified)
    
    print("Message encoded and saved to", output_file)
    audio.close()



