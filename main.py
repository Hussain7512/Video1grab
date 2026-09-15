from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import threading
import urllib.request
import os
import re

class VideoGrabApp(App):
    def build(self):
        self.title = "Video1grab"
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        title = Label(text="Video1grab", font_size=40, size_hint=(1, 0.15))
        layout.add_widget(title)
        
        self.link_input = TextInput(
            hint_text="YouTube ya X ka link paste karein",
            multiline=False,
            size_hint=(1, 0.12)
        )
        layout.add_widget(self.link_input)
        
        self.btn = Button(
            text="Download",
            size_hint=(1, 0.15),
            background_color=(0, 0.7, 1, 1)
        )
        self.btn.bind(on_press=self.start_download)
        layout.add_widget(self.btn)
        
        self.status = Label(
            text="Taiyar hai! Link paste karein",
            size_hint=(1, 0.5)
        )
        layout.add_widget(self.status)
        
        return layout
    
    def get_download_path(self):
        paths = [
            '/storage/emulated/0/Download/',
            '/sdcard/Download/',
            os.path.expanduser('~') + '/',
        ]
        for p in paths:
            if os.path.exists(p) and os.access(p, os.W_OK):
                return p
        return paths[0]
    
    def start_download(self, instance):
        link = self.link_input.text.strip()
        if not link:
            self.status.text = "Pehle link paste karein!"
            return
        
        self.status.text = "Download shuru ho raha hai..."
        threading.Thread(target=self.download_video, args=(link,)).start()
    
    def download_video(self, link):
        try:
            # YouTube aur X ke liye simple direct download
            # Note: Ye sirf basic videos ke liye hai
            save_path = self.get_download_path()
            
            # YouTube video ID nikaalein
            yt_match = re.search(r'(?:v=|youtu\.be/|shorts/)([a-zA-Z0-9_-]{11})', link)
            
            if yt_match:
                video_id = yt_match.group(1)
                # YouTube ka direct download URL try karein
                url = f"https://www.youtube.com/watch?v={video_id}"
                self.status.text = f"YouTube video mili: {video_id}\n(Full download feature jald aayega)"
            else:
                # X (Twitter) ke liye
                self.status.text = "Link mila, lekin full download feature abhi kaam nahi kar raha.\nYe basic version hai."
        
        except Exception as e:
            Clock.schedule_once(lambda dt: setattr(self.status, 'text', f'Masla: {e}'))

if __name__ == '__main__':
    VideoGrabApp().run()
