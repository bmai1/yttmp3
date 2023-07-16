from django.shortcuts import render, redirect
from django.http import HttpResponse
import subprocess

# Create your views here.
def index(request):
    if request.method == 'POST':
        youtube_url = request.POST.get('youtube_url')
        print(youtube_url)

        # Execute the Python script with the YouTube URL as a command-line argument
        command = ['python3', 'myapp/scripts/ytmp3.py', youtube_url]
        subprocess.run(command, capture_output=True)
        # return HttpResponse("Conversion started.")
        return redirect('index')
    else:
        return render(request, 'index.html')