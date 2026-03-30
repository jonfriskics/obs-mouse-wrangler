#!/usr/bin/env python3
import obsws_python as obs
import os
import time

output_dir = os.path.expanduser("~/Movies")
obs1_dir = os.path.join(output_dir, "obs1")
obs2_dir = os.path.join(output_dir, "obs2")
os.makedirs(obs1_dir, exist_ok=True)
os.makedirs(obs2_dir, exist_ok=True)

obs1 = obs.ReqClient(host="localhost", port=4455, password="pass11")
obs2 = obs.ReqClient(host="localhost", port=4466, password="pass22")

obs1.set_current_scene_collection("collection-no-cursor")
obs2.set_current_scene_collection("collection-with-cursor")
time.sleep(2)

obs1.set_record_directory(obs1_dir)
obs2.set_record_directory(obs2_dir)

# TODO printing to debug - remove later
for name, client in [("obs1", obs1), ("obs2", obs2)]:
    v = client.get_video_settings()
    print(f"{name}: canvas={v.base_width}x{v.base_height}, output={v.output_width}x{v.output_height}")

def mute_all_audio(client):
    special = client.get_special_inputs()
    for attr in ['desktop_1', 'desktop_2', 'mic_1', 'mic_2', 'mic_3', 'mic_4']:
        name = getattr(special, attr, None)
        if name:
            client.set_input_mute(name, muted=True)
    for inp in client.get_input_list().inputs:
        try:
            client.set_input_mute(inp["inputName"], muted=True)
        except Exception:
            pass # not an audio input

mute_all_audio(obs1)
mute_all_audio(obs2)
print("All audio muted.")

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
set_source_visibility(obs1, scene1, "with-cursor", False)
set_source_visibility(obs2, scene2, "no-cursor", False)
set_source_visibility(obs2, scene2, "with-cursor", True)
print("Sources configured: obs1=no-cursor, obs2=with-cursor")

print("Connected to both OBS instances. Press ENTER to start both recordings...")
input()

obs1.start_record()
obs2.start_record()
print("Both recordings started!")

print("Press ENTER to stop both recordings...")
input()

obs1.stop_record()
obs2.stop_record()
print("Both stopped.")

# TODO: give both instances a moment to finish writing the file - haven't tested if this fails with really large files.
time.sleep(10)

import subprocess
subprocess.run(["pkill", "-f", "OBS"])
