from pathlib import Path
import subprocess


def mix_background_audio(
    video_path: Path,
    music_path: Path,
    output_path: Path,
    volume_percent: int,
) -> None:

    volume = volume_percent / 100

    command = [
        "ffmpeg",
        "-y",
        "-i",
        str(video_path),
        "-stream_loop",
        "-1",
        "-i",
        str(music_path),
        "-filter_complex",
        f"[1:a]volume={volume}[music];[0:a][music]amix=inputs=2:duration=first:dropout_transition=0[a]",
        "-map",
        "0:v",
        "-map",
        "[a]",
        "-c:v",
        "copy",
        "-c:a",
        "aac",
        "-shortest",
        str(output_path),
    ]

    subprocess.run(command, check=True)
