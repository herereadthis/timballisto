import os
from ffmpeg import FFmpeg

VIDEO_EXTENSIONS = {'.mpg', '.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.webm'}  # Add more extensions if needed

def get_stem(file_path):
    return os.path.splitext(os.path.basename(file_path))[0]

def make_compressed_video(output_dir, input_file_path, fps):
    stem = get_stem(input_file_path)
    output_path_h265 = os.path.join(output_dir, f"{stem}_{fps}fps_h265.mp4")

    print("output_path_h265: ", output_path_h265)
    ffmpeg = (
        FFmpeg()
        .option("y")
        .input(input_file_path)
        .output(
            output_path_h265,
            {"codec:v": "libx265", "crf": 8, "r": fps},  # Adjust CRF value as needed
            vf="yadif",
            preset="medium"
        )
    )
    ffmpeg.execute()


def make_prores_video(output_dir, input_file_path, fps):
    stem = get_stem(input_file_path)
    output_path_prores = os.path.join(output_dir, f"{stem}_{fps}fps_prores.mov")

    print("output_path_prores: ", output_path_prores)
    ffmpeg = (
        FFmpeg()
        .option("y")
        .input(input_file_path)
        .output(
            output_path_prores,
            {"codec:v": "prores_ks", "profile:v": "3"},
            preset="medium",
            vf="yadif",
            crf=fps,
        )
    )
    ffmpeg.execute()


def process_videos(input_dir):
    if not os.path.isdir(input_dir):
        print("Error: Input directory does not exist.")
        return

    output_dir_24fps = os.path.join(input_dir, "24fps")
    output_dir_30fps = os.path.join(input_dir, "30fps")
    os.makedirs(output_dir_24fps, exist_ok=True)
    os.makedirs(output_dir_30fps, exist_ok=True)

    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)

        if os.path.isfile(file_path) and os.path.splitext(filename)[1].lower() in VIDEO_EXTENSIONS:

            print("file_path: ", file_path)
            make_compressed_video(output_dir_30fps, file_path, 30)
            # make_prores_video(output_dir_30fps, file_path, 30)


if __name__ == "__main__":
    input_dir = input("Enter the directory containing the videos: ")
    process_videos(input_dir)
