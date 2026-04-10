#!/usr/bin/env python3
import obsws_python as obs
import os
import time

output_dir = os.path.expanduser("~/Movies")
os.makedirs(output_dir, exist_ok=True)

obs1 = obs.ReqClient(host="localhost", port=4455, password="pass11")
obs2 = obs.ReqClient(host="localhost", port=4466, password="pass22")

obs1.set_current_scene_collection("collection-no-cursor")
obs2.set_current_scene_collection("collection-with-cursor")
time.sleep(2)

obs1.set_record_directory(output_dir)
obs2.set_record_directory(output_dir)

obs1.set_profile_parameter("Output", "FilenameFormatting", "cursor-no-%CCYY-%MM-%DD %hh-%mm-%ss")
obs2.set_profile_parameter("Output", "FilenameFormatting", "cursor-yes-%CCYY-%MM-%DD %hh-%mm-%ss")

for client in [obs1, obs2]:
    v = client.get_video_settings()
    client.set_video_settings(v.fps_numerator, v.fps_denominator, 1920, 1080, 1920, 1080)

def set_source_visibility(client, scene_name, source_name, enabled):
    items = client.get_scene_item_list(scene_name).scene_items
    for item in items:
        if item["sourceName"] == source_name:
            client.set_scene_item_enabled(scene_name, item["sceneItemId"], enabled)
            return
    print(f"Warning: source '{source_name}' not found in scene '{scene_name}'")

scene1 = obs1.get_current_program_scene().scene_name
scene2 = obs2.get_current_program_scene().scene_name

set_source_visibility(obs1, scene1, "no-cursor", True)
set_source_visibility(obs2, scene2, "with-cursor", True)
print("Sources configured: obs1=no-cursor, obs2=with-cursor")

print("Connected to both OBS instances. Press ENTER to start both recordings...")
input()

obs1.start_record()
obs2.start_record()
print("Both recordings started!")

print("Press ENTER to stop both recordings...")
input()

r1 = obs1.stop_record()
r2 = obs2.stop_record()
print("Both stopped.")

time.sleep(10)

import subprocess
# for path in [r1.output_path, r2.output_path]:
#     tmp = path + ".tmp.mov"
#     subprocess.run(["ffmpeg", "-i", path, "-vcodec", "copy", "-an", tmp], check=True)
#     os.replace(tmp, path)
#     print(f"Audio stripped: {path}")

subprocess.run(["pkill", "-f", "OBS"])
