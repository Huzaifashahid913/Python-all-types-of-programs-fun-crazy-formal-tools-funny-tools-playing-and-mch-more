import urllib.request
import webbrowser
import multiprocessing

url = "https://picsum.photos/5000/4000"

for i in range(2):
    output_filename = f"file{i+1}.png"
    urllib.request.urlretrieve(url, output_filename)
    print(f"Download completed of file number {i+1}!")
    # webbrowser.open_new_tab(url)