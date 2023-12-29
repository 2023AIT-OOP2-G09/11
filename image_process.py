import os
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from module.cannycontour import apply_canny_edge_detection
from module.face_cascade import detect_and_draw_faces
from module.grayscale import grayscale_and_threshold
from module.mozaiku import apply_mosaic_to_faces

BASEDIR = os.path.abspath(os.path.dirname(__file__))

def get_ext(filename):
    return os.path.splitext(filename)[-1].lower()

class WatchChangeHandler(FileSystemEventHandler):

    def on_modified(self, event):
        if event.is_directory:
            return
        if get_ext(event.src_path) in ('.jpg', '.jpeg', '.png'):
            print('%s has been modified.' % event.src_path)
            
            # 画像処理のプログラムは、Processorディレクトリ以下で管理されており、追加があればここに追加する
            apply_canny_edge_detection(event.src_path)
            detect_and_draw_faces(event.src_path)
            grayscale_and_threshold(event.src_path)
            apply_mosaic_to_faces(event.src_path)


if __name__ == '__main__':
    print('watch on %s' % BASEDIR + "/uploads")

    event_handler = WatchChangeHandler()

    observer = Observer()
    observer.schedule(event_handler, BASEDIR + "/uploads", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
