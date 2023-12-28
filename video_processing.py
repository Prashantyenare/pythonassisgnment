from moviepy.editor import VideoFileClip


def process_video(input_path, output_path):
    # Load the video clip
    clip = VideoFileClip(input_path)

    # Process the video (e.g., resize, add text, etc.)
    processed_clip = clip.resize(width=480)

    # Write the processed video to the output path
    processed_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')


if __name__ == "__main__":
    # Replace 'input_video.mp4' with your actual input video file
    input_video_path = 'file_example_MP4_480_1_5MG.mp4'

    # Replace 'output_video.mp4' with your desired output video file
    output_video_path = 'output_video.mp4'

    process_video(input_video_path, output_video_path)
