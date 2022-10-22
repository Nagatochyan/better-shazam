from shazamio import Shazam
from shazamio import Serialize
import tkinter
from tkinter import filedialog
import asyncio
def main():
    async def file_select():
        idir = 'C:\\'
        filetype = [("music","*.mp3"), ("音楽","*.m4a")]
        fle = filedialog.askopenfilename(filetypes = filetype, initialdir = idir)
        shazam = Shazam()
        out = await shazam.recognize_song(fle)
        result = Serialize.full_track(data=out)
        youtube_data = await shazam.get_youtube_data(link=result.track.youtube_link)
        serialized_youtube = Serialize.youtube(data=youtube_data)
        print(serialized_youtube.uri)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(file_select())


main()