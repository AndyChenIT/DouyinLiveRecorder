import subprocess


def compress_video(input_file, output_file, crf=36, preset='slower'):
    """
    使用 ffmpeg 压缩视频
    :param input_file: 输入视频文件路径
    :param output_file: 输出视频文件路径
    :param crf: 恒定质量参数（0-51，默认值23，值越小质量越高）
    :param preset: 预设参数（如 ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow）
    """
    command = [
        'ffmpeg',
        '-i', input_file,
        '-vcodec', 'libx264',
        '-crf', str(crf),
        '-preset', preset,
        output_file
    ]

    subprocess.run(command, check=True)


if __name__ == '__main__':
    input_video = '/Users/andychen/software/programSoftwareSpace/PycharmSpace/DouyinLiveRecorder/downloads/抖音直播/ChiPin/2024-10-13/ChiPin_2024-10-13_19-21-13.mp4'
    output_video = '/Users/andychen/software/programSoftwareSpace/PycharmSpace/DouyinLiveRecorder/downloads/抖音直播/ChiPin/2024-10-13/ChiPin_2024-10-13.mp4'
    compress_video(input_video, output_video)