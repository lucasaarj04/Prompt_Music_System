import os

class PlaylistCreatorView:
    def playlist_creator_success(self, controller_response: dict) -> None:
        self.__clear()
        print("Playlist criada com sucesso! \n\n")

        for music in controller_response["playlist"]:
            message = '''
                Titulo da musica: {}
                Artista: {}
                Ano de publicacao: {}

            '''.format(
                music.title,
                music.artist,
                music.year
            )
            print(message)

    def playlist_creator_fail(self, controller_response) -> None:
        self.__clear()

        message = '''
            Erro na criação da playlist:

            * Error: {}
        '''.format(
            controller_response["error"]
        )
        print(message)

    def __clear(self):
        os.system("cls||clear")