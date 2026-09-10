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
    video_source = input("Source video or playlist URL: ")
    audio_source = input("Background music URL: ")
    volume = ask_volume()

    print(f"Source video: {video_source}")
    print(f"Source audio: {audio_source}")
    print(f"Volume: {volume}%")


if __name__ == "__main__":
    main()
