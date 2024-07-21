import gradio as gr
import shutil
from encoding import encode_message
from decoding import decode_message
# Giả sử bạn có hàm xử lý như sau:
def process_encode_audio_and_text(audio, text):
    # Lưu tệp âm thanh vào audio.wav
    audio_path = "data/encode/input.wav"
    shutil.copy(audio, audio_path)
    output_path="data/encode/output.wav"
    encode_message(audio_file=audio_path, message=text, output_file=output_path)


    return output_path
def process_decode_audio_and_text(audio):
    audio_path = "data/decode/input.wav"
    shutil.copy(audio, audio_path)
    output_text = decode_message(audio_file=audio_path)
    return output_text
# Tạo giao diện Gradio
css = """
.encoder {background: linear-gradient(45deg, #c517abbd, #ff7eb3); padding: 10px;}
.encoder h1, .encoder p {color: white}
.decoder {background-color: #c517abbd; padding: 10px}
.decoder h1, .decoder p {color: white}
"""
def main():
    audio_encode_input = gr.Audio(label="Upload Audio", type="filepath")
    audio_decode_input = gr.Audio(label="Upload Audio", type="filepath")
    text_encode_input = gr.Textbox(label="Enter Text")
    text_decode_input = gr.Textbox(label="Hidden Message")
    audio_encode_output = gr.Audio(label="Encoded Audio")
    with gr.Blocks(css=css) as demo:
        with gr.Row(elem_classes="body"):
            with gr.Column(scale=1, elem_classes="encoder"):
                gr.Interface(
                                fn=process_encode_audio_and_text,
                                inputs=[audio_encode_input, text_encode_input],
                                outputs=audio_encode_output,
                                title="Encoder",
                                description="Upload an audio file and enter some text. The processed audio will be outputted."
                            )
            with gr.Column(scale=1, elem_classes="decoder"):
                gr.Interface(
                                fn=process_decode_audio_and_text,
                                inputs=[audio_decode_input],
                                outputs=text_decode_input,
                                title="Decoder",
                                description="Upload an audio file . The hidden message will be outputted."
                            )
    demo.launch()
if __name__ == "__main__":
    main()
