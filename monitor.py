# monitor.py
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from send_email import send_alert  # Import the email function

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        alert = f"Changed: {event.src_path}"
        print(alert)
        send_alert(alert)  # Send email

    def on_created(self, event):
        alert = f"New file: {event.src_path}"
        print(alert)
        send_alert(alert)  # Send email

    def on_deleted(self, event):
        alert = f"Deleted: {event.src_path}"
        print(alert)
        send_alert(alert)  # Send email

folder = r"C:\Users\leopa\OneDrive\Desktop"  # Update path!
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder, recursive=True)
observer.start()

print("Guard Dog is active. Press CTRL+C to stop.")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()