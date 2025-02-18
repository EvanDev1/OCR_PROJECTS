import keyboard
import time

def record_key_presses():
    start_time = time.time()
    key_press_data = {}

    def on_key_event(event):
        current_time = time.time() - start_time
        if event.event_type == keyboard.KEY_DOWN:
            if event.name not in key_press_data:
                key_press_data[event.name] = {'start_time': current_time, 'duration': 0}
                # print(f"Pressed '{event.name}' at {current_time:.2f} seconds")
        elif event.event_type == keyboard.KEY_UP:
            if event.name in key_press_data:
                key_press_data[event.name]['duration'] = current_time - key_press_data[event.name]['start_time']
                print(f"Held '{event.name}' for {key_press_data[event.name]['duration']:.2f} seconds")
                del key_press_data[event.name]

    keyboard.hook(on_key_event)
    print("Recording key presses... Press 'ESC' to stop.")
    keyboard.wait('esc')

if __name__ == "__main__":
    record_key_presses()
