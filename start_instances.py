#!/usr/bin/env python3
import subprocess
import time

subprocess.Popen([
    "open", "-n", "-a", "OBS", "--args",
    "--profile", "dual-screencasts",
    "--collection", "collection-no-cursor",
    "--multi",
    "--websocket_port", "4455",
    "--websocket_password", "pass11",
])

time.sleep(2)

subprocess.Popen([
    "open", "-n", "-a", "OBS", "--args",
    "--profile", "dual-screencasts",
    "--collection", "collection-with-cursor",
    "--multi",
    "--websocket_port", "4466",
    "--websocket_password", "pass22",
])
