import subprocess
from ftplib import print_line

from ffmpeg_progress_yield import FfmpegProgress

def compress_video(input_file, output_file, crf=36, preset='slower'):
    """
    使用 ffmpeg 压缩视频
    :param input_file: 输入视频文件路径
    :param output_file: 输出视频文件路径
    :param crf: 恒定质量参数（0-51，默认值23，值越小质量越高）
    :param preset: 预设参数（如 ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow）
    """
    print(f"开始压缩视频: {input_file}")
    print(f"压缩参数: CRF={crf}, Preset={preset}")

    command = [
        'ffmpeg',
        '-i', input_file,
        '-vcodec', 'libx264',
        '-crf', str(crf),
        '-preset', preset,
        output_file
    ]

    print("压缩任务------------------------------start")

    ff = FfmpegProgress(command)
    for progress in ff.run_command_with_progress():
        print(f"\r压缩进度: {progress:.2f}%", end='', flush=True)

    print("压缩任务------------------------------end")


if __name__ == '__main__':
    input_video = '/Users/andychen/software/programSoftwareSpace/PycharmSpace/DouyinLiveRecorder/downloads/抖音直播/ChiPin/ChiPin_做小红书：如何出爆款、接广告_2024-11-07_10-13-07.mp4'
    output_video = '/Users/andychen/software/programSoftwareSpace/PycharmSpace/DouyinLiveRecorder/downloads/抖音直播/ChiPin/ChiPin_做小红书：如何出爆款、接广告_2024-11-07_10-13-07-压缩.mp4'
    compress_video(input_video, output_video)