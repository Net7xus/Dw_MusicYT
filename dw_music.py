from pytube import YouTube
import os

os.system("clear")
print("\033[1;31m")
print("▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎")
os.system("toilet Dw_music")
print("▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎_______▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎")
print("       \033[1;32m<>___<>       \033[1;31m*/       \*        \033[1;32m<>___<>")
print("        \033[1;32m[^_^]        \033[1;31m||Code by||         \033[1;32m[^_^]")
print("       \033[1;32m/{ - }\       \033[1;31m||Hunt3rX||        \033[1;32m/{ - }\ ")
print("       \033[1;32m(_)_(_)       \033[1;31m*\_______/*        \033[1;32m(_)_(_)")
print("\033[1;31m▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎/       \▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎")
print("|")
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


