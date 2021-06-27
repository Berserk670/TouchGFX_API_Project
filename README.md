# TouchGFX_API_Project

********************************Project Ideas********************************
For my intitial thougths, I'm thinking of using a mixture of a Rasperry Pi4 
and an ARM based MCU, that has driver/Interface support for a TouchGFX screen 
that is similar to a smartphone, or Smartwatch. My initial thoughts is to use 
the Rasperry Pi 4, for the puplic API and packing the data and transmitting 
it over QSPI, to the Arm MCU, which will then display the image on the 
TouchGFX. 

Something I found online which might be useful:
Video streaming:

"HTTP streaming separates each image into individual HTTP replies on a specified marker. HTTP streaming creates packets of a sequence of JPEG images that can be received by clients such as QuickTime or VLC.

In response to a GET request for a MJPEG file or stream, the server streams the sequence of JPEG frames over HTTP. A special mime-type content type multipart/x-mixed-replace;boundary=<boundary-name> informs the client to expect several parts (frames) as an answer delimited by <boundary-name>. This boundary name is expressly disclosed within the MIME-type declaration itself. The TCP connection is not closed as long as the client wants to receive new frames and the server wants to provide new frames. Two basic implementations of a M-JPEG streaming server are cambozola and MJPG-Streamer. The more robust ffmpeg-server also provides M-JPEG streaming support.

Native web browser support includes: Safari, Google Chrome, Microsoft Edge[5] and Firefox.[6] Other browsers, such as Internet Explorer can display M-JPEG streams with the help of external plugins. Cambozola is an applet that can show M-JPEG streams in Java-enabled browsers. M-JPEG is also natively supported by PlayStation and QuickTime."
  
*****************************************************************************
