from src.view.song_register_view import SongRegisterView
from src.controllers.song_register_controller import SongRegisterController

    # SongRegisterView -> Pascal Case (Classes)
    # song_register_view -> Snake Case (Funções, métodos, variáveis)

def song_register_process():
    song_register_view = SongRegisterView()
    song_register_controller = SongRegisterController()

    new_song_information = song_register_view.registry_song_initial()
    response = song_register_controller.insert(new_song_information)

    if response["success"]:
        song_register_view.registry_song_success(response)
    else:
        song_register_view.registry_song_fail(response)