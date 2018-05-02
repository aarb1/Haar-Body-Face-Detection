# Haar-Body-Face-Detection

This application is created using OpenCV and incorporates Viola-Jones Object detection framework to detect human faces and bodies.

Viola-Jones framework can be used to detect many kinds of objects, however it was mainly driven by the problem of face detection.

The framework relies on detecting Haar-like features. All human faces are very similar and have similar properties such as eyebrows, mouth, nose-bridge, etc. These features and properties can be matched using Haar features.

The Haar object detection method works great for full frontal face detection. It is harder to detect the human body with this method as human bodies vary a lot due to different features such as clothes, shape, etc.

The application uses Haar cascades provided by OpenCV and detects face, upper body, lower body and full body.

The goal was to successfully and accurately detect any humans present in the webcam feed.