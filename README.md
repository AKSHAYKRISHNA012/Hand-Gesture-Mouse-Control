<html lang="en">
<body>
    <div class="container">
        <h1>Hand-Gesture Mouse Control</h1>
        <p>This project uses hand gestures to control mouse movements on a computer screen. By leveraging computer vision and hand-tracking technology, this application allows users to interact with their computer using simple hand gestures, effectively turning their webcam into a virtual touchpad.</p>

  <h2>Table of Contents</h2>
        <ul>
            <li><a href="#introduction">Introduction</a></li>
            <li><a href="#features">Features</a></li>
            <li><a href="#requirements">Requirements</a></li>
            <li><a href="#installation">Installation</a></li>
            <li><a href="#usage">Usage</a></li>
            <li><a href="#configuration">Configuration</a></li>
            <li><a href="#credits">Credits</a></li>
        </ul>

  <h2 id="introduction">Introduction</h2>
        
  <p>The Hand-Gesture Mouse Control project enables users to control their computer's mouse cursor through hand gestures captured via a webcam. This is achieved using OpenCV for computer vision tasks, a custom hand-tracking module for detecting and tracking hand landmarks, and <code>autopy</code> for controlling the mouse cursor.</p>

  <h2 id="features">Features</h2>
        <ul>
            <li>Hand detection and tracking using a webcam</li>
            <li>Control mouse movements with the index finger</li>
            <li>Click actions using both index and middle fingers</li>
            <li>Smooth and responsive cursor movements</li>
            <li>Frame rate display for performance monitoring</li>
        </ul>

  <h2 id="requirements">Requirements</h2>
        <ul>
            <li>Python 3.x</li>
            <li>OpenCV</li>
            <li>NumPy</li>
            <li>autopy</li>
            <li>Custom HandTrackingModule</li>
        </ul>

  <h2 id="installation">Installation</h2>
        <p>Clone this repository:</p>
        <pre><code>git clone https://github.com/yourusername/Hand-Gesture-Mouse-Control.git
cd Hand-Gesture-Mouse-Control</code></pre>
        <p>Install the required Python packages:</p>
        <pre><code>pip install opencv-python numpy autopy</code></pre>
        <p>Ensure that you have the HandTrackingModule available. You can either download it separately or ensure it is included in your project directory.</p>

  <h2 id="usage">Usage</h2>
        <p>Run the script:</p>
        <pre><code>python hand_gesture_mouse_control.py</code></pre>
        <p>Ensure your webcam is connected and properly set up.</p>
        <p>Position your hand within the webcam's view. A rectangle frame will guide the hand placement.</p>
        <p>Use the following gestures to control the mouse:</p>
        <ul>
            <li><strong>Index Finger Up:</strong> Move the cursor</li>
            <li><strong>Both Index and Middle Fingers Up:</strong> Click action</li>
        </ul>

  <h2 id="configuration">Configuration</h2>
        <p><code>wcam, hcam:</code> Set the width and height of the webcam frame.</p>
        <p><code>frameR:</code> Frame reduction to define the active area for hand tracking.</p>
        <p><code>smoothening:</code> Value to smoothen cursor movements, making them less jittery.</p>
        <p>These parameters can be adjusted at the beginning of the script:</p>
        <pre><code>wcam, hcam = 680, 450
frameR = 100  # Frame Reduction
smoothening = 20</code></pre>

  <h2 id="credits">Credits</h2>
        <ul>
            <li><strong>OpenCV:</strong> Used for capturing video and image processing.</li>
            <li><strong>NumPy:</strong> For numerical operations.</li>
            <li><strong>autopy:</strong> For controlling the mouse.</li>
            <li><strong>HandTrackingModule:</strong> Custom module for hand landmark detection and tracking.</li>
        </ul>

  <h2 id="license">License</h2>
        <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
    </div>
</body>
</html>
l
