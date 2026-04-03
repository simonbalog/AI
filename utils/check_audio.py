import sounddevice as sd

def list_devices():
    print("\n--- AUDIO DEVICES ---")
    devices = sd.query_devices()
    for i, dev in enumerate(devices):
        print(f"ID: {i} | Name: {dev['name']} | Inputs: {dev['max_input_channels']} | Outputs: {dev['max_output_channels']}")
    
    print("\n--- DEFAULT DEVICES ---")
    print(f"Default Input: {sd.default.device[0]}")
    print(f"Default Output: {sd.default.device[1]}")

if __name__ == "__main__":
    list_devices()
