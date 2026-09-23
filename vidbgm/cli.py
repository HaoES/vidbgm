from pathlib import Path
from vidbgm.ffmpeg import mix_background_audio


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
    video_source = Path(input("Source video path: "))
    audio_source = Path(input("Background music path: "))
    volume = ask_volume()

    print(f"Source video: {video_source}")
    print(f"Source audio: {audio_source}")
    print(f"Volume: {volume}%")

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

    answer = input("Create full video? [y/N]: ")
    answer = answer.strip().lower()
    if answer in ("yes", "y"):
        output_path = Path("outputs/output.mp4")
        output_path.parent.mkdir(exist_ok=True)
        mix_background_audio(video_source, audio_source, output_path, volume)
        print(f"Created full video at: {output_path}")
    else:
        print("Stopped after preview.")


if __name__ == "__main__":
    main()
