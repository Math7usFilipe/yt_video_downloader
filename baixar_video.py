from yt_dlp import YoutubeDL
import os
from tqdm import tqdm
import sys

def baixar_video():
    # Estilização simples para o título
    print("\033[1;34m=== YouTube Video Downloader ===\033[0m")
    print("")

    # Diretório de download
    folder = input("\033[1;36mEnter the folder name to save the video (leave blank for current folder): \033[0m")
    if folder.strip():
        if not os.path.exists(folder):
            os.makedirs(folder)
        output_path = os.path.join(folder, '%(title)s.%(ext)s')
    else:
        output_path = '%(title)s.%(ext)s'

    # URL do vídeo
    url = input("\033[1;36mEnter the YouTube video URL: \033[0m")

    try:
        # Variável global para a barra de progresso
        pbar = None

        # Função de progresso
        def progress_hook(d):
            nonlocal pbar
            if d['status'] == 'downloading':
                total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
                downloaded_bytes = d.get('downloaded_bytes', 0)
                if total_bytes > 0:
                    if pbar is None:
                        # Inicializa a barra de progresso
                        pbar = tqdm(total=total_bytes, unit='B', unit_scale=True, desc="Downloading", 
                                    bar_format="{l_bar}\033[1;32m{bar}\033[0m {r_bar}")
                    pbar.n = downloaded_bytes  # Atualiza a barra
                    pbar.refresh()
            elif d['status'] == 'finished':
                if pbar is not None:
                    pbar.n = pbar.total  # Completa a barra
                    pbar.refresh()
                    pbar.close()
                print("\033[1;32m\nDownload complete, saving file...\033[0m")

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'quiet': True,
            'no_warnings': True,
            'outtmpl': output_path,
            'progress_hooks': [progress_hook],
        }

        # Extraindo informações do vídeo
        print("\033[1;33mFetching video info...\033[0m")
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get('formats', [])

        # Listando qualidades disponíveis
        print("\033[1;33m\nAvailable qualities:\033[0m")
        quality_options = {}
        for i, fmt in enumerate(formats, 1):
            if fmt.get('vcodec') != 'none' and fmt.get('height'):
                resolution = f"{fmt['height']}p"
                quality_options[str(i)] = fmt['format_id']
                print(f"\033[1;36m{i}. {resolution}\033[0m (Format: {fmt['format_id']})")

        choice = input("\033[1;36mEnter the desired quality number: \033[0m")
        if choice not in quality_options:
            raise ValueError("Invalid choice! Using standard quality.")

        ydl_opts['format'] = quality_options[choice]

        # Iniciando o download
        print("\033[1;33m\nStarting download...\033[0m")
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print(f"\033[1;32mDownload complete! Video saved in: {folder if folder.strip() else 'current folder'}\033[0m")

    except Exception as e:
        if 'pbar' in locals() and pbar is not None:
            pbar.close()
        print(f"\033[1;31mAn error occurred: {e}\033[0m")
        print("\033[1;31mCheck the URL or try again later.\033[0m")

if __name__ == "__main__":
    baixar_video()