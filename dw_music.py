from pytube import YouTube
import os

os.system("clear")
print("\033[1;31m")
print("▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎")
os.system("toilet Dw_music")
print("▪▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎")
print("                     ||Code by||")
print("                     ||Hunt3rX||")
print("                     *\_______/*")
print("")
# Función para descargar música de YouTube
def download_music(url):
  try:
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    nombre_archivo = input("\033[1;31m[>]Renombre el titulo [mp3]: \033[1;37m")
    video.download(output_path='.', filename=(nombre_archivo))
    print(f"\033[1;31m[>]Musica descargada: \033[1;37m'{nombre_archivo}'")
  except Exception as e:
    print("\033[1;31m[>]Error al descargar la musica:", str(e))

# URL del video de YouTube
url = input("[>]Url: \033[1;37m")

# Descargar música
download_music(url)


