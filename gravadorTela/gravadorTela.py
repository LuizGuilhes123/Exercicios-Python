import pyautogui
import cv2
import numpy as np
import time

def iniciar_gravacao(filename, codec, fps, frame_size):
    return cv2.VideoWriter(filename, codec, fps, frame_size)

def capturar_tela():
    img = pyautogui.screenshot()
    frame = np.array(img)
    return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

def main():
    resolution = (1920, 1080)
    codec = cv2.VideoWriter_fourcc(*'mp4v')
    filename = 'Recorte.mp4'
    fps = 30.0
    frame_delay = 1 / fps

    print("Pressione Enter para iniciar a gravação...")
    input()

    out = iniciar_gravacao(filename, codec, fps, resolution)
    if not out.isOpened():
        print("Erro ao inicializar o VideoWriter. Verifique os parâmetros.")
        return

    cv2.namedWindow('Live', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Live', 480, 370)

    print("Gravação iniciada. Pressione 'q' para parar...")

    try:
        while True:
            start_time = time.time()

            frame = capturar_tela()
            out.write(frame)
            cv2.imshow('Live', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Pressione Enter novamente para confirmar o encerramento...")
                input()
                break

            elapsed_time = time.time() - start_time
            sleep_time = max(0, frame_delay - elapsed_time)
            time.sleep(sleep_time)

    except KeyboardInterrupt:
        print("Gravação interrompida pelo usuário.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        print("Gravação finalizada. Salvando vídeo...")
        out.release()
        cv2.destroyAllWindows()
        print(f"Vídeo salvo como {filename}")

if __name__ == "__main__":
    main()