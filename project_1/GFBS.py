import TDFT
FILENAME = TDFT.FILENAME
sound, frame_rate = TDFT.sound, TDFT.frame_rate
frame_num, channel_num = TDFT.frame_num, TDFT.channel_num
window_width = TDFT.window_width
spectrum = TDFT.get_tdft(sound, window_width, frame_num)
print(spectrum.shape)