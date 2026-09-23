from pathlib import Path

from vidbgm.ffmpeg import mix_background_audio


def ask_existing_path(prompt: str) -> Path:
    while True:
        path = Path(input(prompt))

        if not path.exists():
            print("File does not exist, please try again")
            continue
        if not path.is_file():
            print("Path must point to a file, please try again")
            continue
        return path


def ask_volume() -> int:
    while True:
        raw_volume = input("Please set the volume of the music (between 0 and 100): ")
        try:
            volume = int(raw_volume)
        except ValueError:
            print("Volume must be a whole number, please try again")
            continue
        if volume < 0 or volume > 100:
            print("Volume must be a value between 0 and 100, please try again")
            continue
        return volume


def main() -> None:
    video_source = ask_existing_path("Source video path: ")
    audio_source = ask_existing_path("Background music path: ")
    volume = ask_volume()

    print(f"Source video: {video_source}")
    print(f"Source audio: {audio_source}")
    print(f"Volume: {volume}%")

    while True:
        preview_path = Path("previews/preview.mp4")
        preview_path.parent.mkdir(exist_ok=True)

        mix_background_audio(
            video_source,
            audio_source,
            preview_path,
            volume,
            duration_seconds=10,
        )

        print(f"Created preview: {preview_path}")

        answer = input("Choose: [c]reate full video, [v] change volume, [q] quit: ")
        answer = answer.strip().lower()

        if answer in ("create", "c"):
            output_path = Path("outputs/output.mp4")
            output_path.parent.mkdir(exist_ok=True)
            mix_background_audio(video_source, audio_source, output_path, volume)
            print(f"Created full video at: {output_path}")
            break
        if answer in ("volume", "v"):
            volume = ask_volume()
            continue
        print("Stopped after preview.")
        break


if __name__ == "__main__":
    main()
